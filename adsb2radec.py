import numpy as np
import datetime
import socket
import threading
import argparse

from wmpl.Utils.TrajConversions import geo2Cartesian, eci2RaDec, raDec2AltAz, J2000_JD, date2JD

subscribers = []  # holds the connection objects for each subscriber to the data feed


def connection_detect(output_port):
    """ Threaded* monitors for a new connection and adds to the subscriber list

 Arguments:
 output_port: [int] port on which to listen for connections and serve data



 """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", output_port))

        while True:
            s.listen()
            (connection, subscriber_address) = s.accept()
            print("Accepted connection on Connection {} ".format(connection))
            print("From address {} ".format(subscriber_address))
            subscribers.append(connection)
            data = bytes("ADSB to RaDec server connection accepted at {}".format(datetime.datetime.now()) + "\n",
                         "utf-8")
            connection.send(data)
            data = bytes("You are subscriber {}".format(len(subscribers)) + "\n", "utf-8")
            connection.send(data)



def parseadsbdatatype3(adsb):
    """ Take a complete adsb data string and parse it into time and location data

 Arguments:
 adsb: [str] adsb string from dump1090
 
 
 Return:
 [float, float, float, float] lat, lon , ele, julian date
 """
    # set everything to zero
    air_lat = 0
    air_ele = 0
    air_lon = 0
    air_jd = 0
    air_icao = ""


    if len(adsb) != 0:
        split_adsb_data = adsb.split(",")

        if len((split_adsb_data[14])) != 0 and len((split_adsb_data[15])) != 0:
            air_ele = float(split_adsb_data[11]) / 3.2808399  # convert feet to metres
            air_lat = float(split_adsb_data[14])
            air_lon = float(split_adsb_data[15])
            air_icao = split_adsb_data[4]
            if split_adsb_data[7] != "" and split_adsb_data[8] != "" and split_adsb_data[9] != "":


                #if aircraft time is available then use it
                split_tar_utc_date = (split_adsb_data[8].split("/"))
                air_year = int(split_tar_utc_date[0])
                air_month = int(split_tar_utc_date[1])
                air_day = int(split_tar_utc_date[2])
                split_air_utc_time = (split_adsb_data[9].split(":"))
                air_hour = int(split_air_utc_time[0])
                air_minute = int(split_air_utc_time[1])
                air_second_ms = float(split_air_utc_time[2])
                air_ms = int((air_second_ms % 1) * 1000)  # just get the millisecond component
                air_second = int(air_second_ms - air_ms / 1000)  # just get the seconds

            else:
                #use UTC computer time
                air_year = datetime.datetime.now().year
                air_month = datetime.datetime.now().month
                air_day = datetime.datetime.now().day
                air_hour = datetime.datetime.now().hour
                air_minute = datetime.datetime.now().minute
                air_second = datetime.datetime.now().second
                air_ms = datetime.datetime.now().microsecond / 1000

            air_jd = date2JD(air_year, air_month, air_day, air_hour, air_minute, air_second, air_ms)

        else:
            pass

        return air_lat, air_lon, air_ele, air_jd, air_icao


def adsbToRaDec(sta_lat, sta_lon, sta_ele, adsb):
    """ Convert the ADSB aircraft data stream to the RaDec from the station location

 Arguments:
 sta_lat: [float] Station latitude in degrees.
 sta_lon: [float] Station longitude in degrees.
 sta_ele: [float] Station elevation in meters (MSL).
 adsb: [str] adsb string from dump1090

 Return:
 [float, float] right ascension and declination of the target in degrees.
 """

    # parse the adsb data, use the aircraft's time for the julian date
    air_lat, air_lon, air_ele, tar_jd, air_icao = parseadsbdatatype3(adsb)

    if tar_jd != 0:
        # Convert the station lat/lon/alt to ECI
        sta_eci = np.array(geo2Cartesian(np.radians(sta_lat), np.radians(sta_lon), sta_ele, tar_jd))

        # Convert the target lat/lon/alt to ECI
        tar_eci = np.array(geo2Cartesian(np.radians(air_lat), np.radians(air_lon), air_ele, tar_jd))

        # Compute direction vector from station to target
        sta_tar_vec = tar_eci - sta_eci

        # Convert the direction vector to RA/Dec
        ra, dec = eci2RaDec(sta_tar_vec)

        # Convert the RA/Dec to alt/az
        az, alt = raDec2AltAz(ra, dec, tar_jd, np.radians(sta_lat), np.radians(sta_lon))
    else:
        ra = 0
        dec = 0
        az = 0
        alt = 0
    return air_lat, air_lon, air_ele, np.degrees(ra), np.degrees(dec), np.degrees(az), np.degrees(alt), tar_jd, air_icao


def handle_adsb(dump1090_address, dump1090_port, sta_lat, sta_lon, sta_ele):
    """ Given station location wait for ADSB data to arrive, and then serve to subscribers

 Arguments:
 dump1090_address: [str] address of dump1090 server
 dump1090_port: [int] port of dump1090 server
 sta_lat: [float] Station latitude in degrees.
 sta_lon: [float] Station longitude in degrees.
 sta_ele: [float] Station elevation in meters (MSL).
 adsb: [str] adsb string from dump1090

 Return:
 [float, float] right ascension and declination of the target in degrees.
 """

    incoming = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    incoming.connect((dump1090_address, int(dump1090_port)))
    print("Connected to {}:{}".format(dump1090_address, int(dump1090_port)))
    adsb_message = ""

    while True:
        raw_received = incoming.recv(200)
        adsb_message = adsb_message + raw_received.decode()
        while '\n' in str(adsb_message):  # there is more to process
            # print('processing')
            first_adsb_message = adsb_message.split("\n")[0]
            # print('len first_adsb_messgae {:.2f}'.format(len(first_adsb_message.split(","))))
            if len(first_adsb_message.split(",")) == 22:  # it looks valid
                if first_adsb_message.split(",")[0] == "MSG":  # it is a message
                    if first_adsb_message.split(",")[1] == "3":  # it is a position message
                        air_lat, air_lon, air_ele, ra, dec, az, alt, jd, air_icao = adsbToRaDec(sta_lat, sta_lon,
                                                                                                sta_ele,
                                                                                                first_adsb_message)
                        # print("Valid:{}\n".format(first_adsb_message))
                        result = "lat {:.3f}, lon {:.3f}, alt {:.0f}, ra {:.5f}, dec {:.5f}, alt {:.3f}, az {:.2f}, jd {:.3f}, icao {} \n".format(
                            air_lat, air_lon, air_ele, ra, dec, alt, az, jd, air_icao)
                        print(result)
                        data = bytes(result + "\n", "utf-8")
                        print("Sending to {}".format(len(subscribers)))
                        for connection in subscribers:
                            try:
                                connection.send(data)
                            except:
                                print("lost a subscriber")
                                subscribers.remove(connection)

            adsb_message = adsb_message.split("\n", 1)[1]


if __name__ == "__main__":
    # ## PARSE INPUT ARGUMENTS ###
    # Init the command line arguments parser

    arg_parser = argparse.ArgumentParser(description=""" Radec coordinate server""")
    arg_parser.add_argument('sta_lat', type=float, help="observer latitude(deg)")
    arg_parser.add_argument('sta_lon', type=float, help="observer longtiude(deg)")
    arg_parser.add_argument('sta_alt', type=float, help="observer altitude(m)")
    arg_parser.add_argument('dump1090', type=str, help="address:port of dump1090 server, i.e 192.168.1.151:30003")
    arg_parser.add_argument('output_port', type=int, help="port to send data, i.e. 30004")

    # Parse the command line arguments

    cml_args = arg_parser.parse_args()

    # station coordinates
    sta_lat, sta_lon, sta_ele = cml_args.sta_lat, cml_args.sta_lon, cml_args.sta_alt

    # dunp1090 server
    dump1090_address, dump1090_port = cml_args.dump1090.split(':')[0], cml_args.dump1090.split(':')[1]

    # output_port
    output_port = cml_args.output_port

    # start the threads

    adsb_thread = threading.Thread(target=handle_adsb,
                                   args=(dump1090_address, dump1090_port, sta_lat, sta_lon, sta_ele))
    adsb_thread.start()

    connection_detect_thread = threading.Thread(target=connection_detect, args=(output_port,))
    connection_detect_thread.start()

    adsb_thread.join()
