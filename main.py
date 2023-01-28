import numpy as np
import datetime
import socket
import time

from wmpl.Utils.TrajConversions import geo2Cartesian, eci2RaDec, raDec2AltAz, J2000_JD, date2JD


def parseadsbdata(adsb):
    """ Take a single adsb message and parse it into time and location data 

 Arguments:
 adsb: [str] adsb string from dump1090
 
 
 Return:
 [float, float, float, float] lat, lon , ele, julian date
 """

    # Position fields have 22 fields, field 0 is MSG, field 1 is 3
    #
    # 0   1 2 3 4      5 6          7            8          9            10 11   12 13 14        15
    # MSG,3,1,1,7C7B81,1,2023/01/27,05:59:17.093,2023/01/27,05:59:17.138,  ,2600, ,   ,-32.30930,115.78676,,,0,,0,0

    if len(adsb) != 0:
        split_adsb_data = adsb.split(",")

        if len((split_adsb_data[14])) != 0 and len((split_adsb_data[15])) != 0:
            tar_ele = float(split_adsb_data[11]) / 3.2808399  # convert feet to metres
            tar_lat = float(split_adsb_data[14])
            tar_lon = float(split_adsb_data[15])

            if split_adsb_data[7] != "" and split_adsb_data[8] != "" and split_adsb_data[9] != "":
                #print("real date found")
                split_tar_utc_date = (split_adsb_data[8].split("/"))
                #print("Date " + str(split_tar_utc_date))
                tar_year = int(split_tar_utc_date[0])
                tar_month = int(split_tar_utc_date[1])
                tar_day = int(split_tar_utc_date[2])

                split_tar_utc_time = (split_adsb_data[9].split(":"))

                tar_hour = int(split_tar_utc_time[0])
                tar_minute = int(split_tar_utc_time[1])
                tar_second_ms = float(split_tar_utc_time[2])

                tar_ms = int((tar_second_ms % 1) * 1000)  # just get the millisecond component
                tar_second = int(tar_second_ms - tar_ms / 1000)  # just get the seconds

            else:
                #print("No time information - use computer UTC time")
                tar_year = datetime.datetime.now().year
                tar_month = datetime.datetime.now().month
                tar_day = datetime.datetime.now().day
                tar_hour = datetime.datetime.now().hour
                tar_minute = datetime.datetime.now().minute
                tar_second = datetime.datetime.now().second
                tar_ms = datetime.datetime.now().microsecond / 1000

            tar_jd = date2JD(tar_year, tar_month, tar_day, tar_hour, tar_minute, tar_second, tar_ms)
            #print("Lat {:.4f}, Lon {:.4f}, Altitude {:.0f}m, JD:{:.6f}".format(tar_lat, tar_lon, tar_ele, tar_jd))
            #print("Time {}-{}-{} {}:{}:{}.{} UTC".format(tar_year, tar_month, tar_day, tar_hour, tar_minute, tar_second,
                                                         #tar_ms))
        else:
            tar_lat = 0
            tar_ele = 0
            tar_lon = 0
            tar_jd = 0

        return tar_lat, tar_lon, tar_ele, tar_jd


def adsbToRaDec(sta_lat, sta_lon, sta_ele, adsb):
    """ Convert the lat/lon/alt of a target to the alt/az of a station.

 Arguments:
 sta_lat: [float] Station latitude in degrees.
 sta_lon: [float] Station longitude in degrees.
 sta_ele: [float] Station elevation in meters (MSL).
 adsb: [str] adsb string from dump1090

 Return:
 [float, float] right ascension and declination of the target in degrees.
 """

    # parse the adsb data, use the aircraft's time for the julian date
    tar_lat, tar_lon, tar_ele, tar_jd = parseadsbdata(adsb)

    if tar_jd != 0:
        # Convert the station lat/lon/alt to ECI
        sta_eci = np.array(geo2Cartesian(np.radians(sta_lat), np.radians(sta_lon), sta_ele, tar_jd))

        # Convert the target lat/lon/alt to ECI
        tar_eci = np.array(geo2Cartesian(np.radians(tar_lat), np.radians(tar_lon), tar_ele, tar_jd))

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
    return tar_lat, tar_lon, tar_ele, np.degrees(ra), np.degrees(dec), np.degrees(az), np.degrees(alt), tar_jd


def fake_adsb(length,f):

    return str(f.readline())
    time.sleep(2)


if __name__ == "__main__":

    # ## PARSE INPUT ARGUMENTS ###
    # Init the command line arguments parser
    arg_parser = argparse.ArgumentParser(description=""" Radec coordinate server
           """)

    arg_parser.add_argument('lat', type=float, help="observer latitude(deg)")

    arg_parser.add_argument('lon', type=float, help="observer longtiude(deg)")

    arg_parser.add_argument('alt', type=float, help="observer altitude(m)")

    arg_parser.add_argument('dump1090address', help="Address of dump1090 server, i.e 192.168.1.151")

    arg_parser.add_argument('dump1090port', help="Port of dump1090 server, normally 30003")

    arg_parser.add_argument('-p', '--port', action="store_true",
                            help="""Disable background normalization.""")

    arg_parser.add_argument('-x', '--hideplot', action="store_true",
                            help="""Don't show the stack on the screen after stacking. """)

    arg_parser.add_argument('-o', '--output', type=str,
                            help="""folder to save the image in.""")

    arg_parser.add_argument('-s', '--showers', type=str,
                            help="Show only meteors from specific showers (e.g. URS, PER, GEM, ... for sporadic). Comma-separated list. \
               Note that an RMS config file that matches the data is required for this option.")

    arg_parser.add_argument('-d', '--darkbackground', action="store_true",
                            help="""Darken the background. """)

    # Parse the command line arguments
    cml_args = arg_parser.parse_args()

    sta_lat = -32.354356  # deg
    sta_lon = 115.805961  # deg
    sta_ele = 37  # meters



    #print(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    dumpfile = open(datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".txt", "a")
    dumpfile2 = open(datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".txt2", "a")
    dumpfile3 = open(datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".txt3", "a")
    # ra, dec = adsbToRaDec(sta_lat, sta_lon, sta_ele, adsbtest)
    # print("Ra {:.4f}, Dec {:.4f}".format(ra, dec))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.1.151', 30003))

    adsb_message = ""
    adsb_testing = False

    if adsb_testing:
        f = open("20230128005214.txt2", "r")
    while True:

        if adsb_testing:
            adsb_message = adsb_message + bytes((fake_adsb(100,f))).decode()

        else:
            raw_received = s.recv(100)
            dumpfile3.write(raw_received.decode())
            adsb_message = adsb_message + raw_received.decode()


        if not adsb_testing:
            dumpfile2.writelines(adsb_message)
            #dumpfile.write("Raw output:{}".format(adsb_message))
        #print("Testing to see if newline in message" + str('\n' in adsb_message))
        while '\n' in str(adsb_message):  # there is more to process
            #print('processing')
            first_adsb_message = adsb_message.split("\n")[0]
            #print('len first_adsb_messgae {:.2f}'.format(len(first_adsb_message.split(","))))
            if len(first_adsb_message.split(",")) == 22:       # it looks valid
                if first_adsb_message.split(",")[0] == "MSG":  # it is a message
                  if first_adsb_message.split(",")[1] == "3":  # it is a position message
                    air_lat, air_lon, air_ele, ra, dec, az, alt, jd = adsbToRaDec(sta_lat, sta_lon, sta_ele, first_adsb_message)
                    #print("Valid:{}\n".format(first_adsb_message))
                    print("lat {:.3f}, lon {:.3f}, alt {.0f},Ra {:.3f},dec {:.2f}, jd {:.3f} \n".format(air_lat, air_lon, air_ele, ra, dec, jd))
                    if not adsb_testing:
                        dumpfile.write("Valid:{}\n".format(first_adsb_message))
                        dumpfile.write("lat {:.3f}, lon {:.3f}, alt {.0f},Ra {:.3f},dec {:.2f}, jd {:.3f} \n".format(air_lat, air_lon, air_ele, ra, dec, jd))

            adsb_message = adsb_message.split("\n", 1)[1]
