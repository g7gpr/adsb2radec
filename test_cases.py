def test_cases():
    # test cases
    print("")
    print("Test case S1: Southern hemisphere meteor north and east of station")
    sta_lat = -32.3  # deg
    sta_lon = 115.8  # deg
    sta_ele = 37  # meters
    tar_lat = -31.908  # deg
    tar_lon = 116.156  # deg
    tar_ele = 81.1 * 1000
    azimuth, elevation, distance = latlonaltlatlonalt2azel(sta_lat, sta_lon, sta_ele, tar_lat, tar_lon, tar_ele)
    print("Azimuth {:.2f}, Elevation {:.2f}, Distance {:.2f}km".format(azimuth, elevation, distance / 1000))
    print("")
    print("Station Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(sta_lat, sta_lon, sta_ele))
    print("Target  Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(tar_lat, tar_lon, tar_ele))
    print("Azimuth {:.2f}, Elevation {:.2f}, Distance {:.2f}km".format(azimuth, elevation, distance / 1000))
    print("")
    print("")
    print("Test case S2: Southern hemisphere meteor south and east of station")
    sta_lat = -32.3  # deg
    sta_lon = 115.8  # deg
    sta_ele = 37.0  # meters
    tar_lat = -32.4  # deg
    tar_lon = 116.156  # deg
    tar_ele = 81.1 * 1000
    azimuth, elevation, distance = latlonaltlatlonalt2azel(sta_lat, sta_lon, sta_ele, tar_lat, tar_lon, tar_ele)
    print("")
    print("Station Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(sta_lat, sta_lon, sta_ele))
    print("Target  Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(tar_lat, tar_lon, tar_ele))
    print("Azimuth {:.2f}, Elevation {:.2f}, Distance {:.2f}km".format(azimuth, elevation, distance / 1000))
    print("")
    print("")
    print("Test case S3: Southern hemisphere meteor south and west of station")
    sta_lat = -32.3  # deg
    sta_lon = 115.8  # deg
    sta_ele = 37  # meters
    tar_lat = -32.4  # deg
    tar_lon = 115.356  # deg
    tar_ele = 81.1 * 1000
    azimuth, elevation, distance = latlonaltlatlonalt2azel(sta_lat, sta_lon, sta_ele, tar_lat, tar_lon, tar_ele)
    print("")
    print("Station Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(sta_lat, sta_lon, sta_ele))
    print("Target  Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(tar_lat, tar_lon, tar_ele))
    print("Azimuth {:.2f}, Elevation {:.2f}, Distance {:.2f}km".format(azimuth, elevation, distance / 1000))
    print("")
    print("")
    print("Test case S4: Southern hemisphere meteor north and west of station")
    sta_lat = -32.3  # deg
    sta_lon = 115.8  # deg
    sta_ele = 37  # meters
    tar_lat = -31.908  # deg
    tar_lon = 115.356  # deg
    tar_ele = 81.1 * 1000
    azimuth, elevation, distance = latlonaltlatlonalt2azel(sta_lat, sta_lon, sta_ele, tar_lat, tar_lon, tar_ele)
    print("")
    print("Station Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(sta_lat, sta_lon, sta_ele))
    print("Target  Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(tar_lat, tar_lon, tar_ele))
    print("Azimuth {:.2f}, Elevation {:.2f}, Distance {:.2f}km".format(azimuth, elevation, distance / 1000))
    print("")
    print("")
    print("Test case N1: Northern hemisphere meteor south and east of station")
    sta_lat = 32.3  # deg
    sta_lon = 115.8  # deg
    sta_ele = 37  # meters
    tar_lat = 31.908  # deg
    tar_lon = 116.156  # deg
    tar_ele = 81.1 * 1000
    azimuth, elevation, distance = latlonaltlatlonalt2azel(sta_lat, sta_lon, sta_ele, tar_lat, tar_lon, tar_ele)
    print("")
    print("Station Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(sta_lat, sta_lon, sta_ele))
    print("Target  Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(tar_lat, tar_lon, tar_ele))
    print("Azimuth {:.2f}, Elevation {:.2f}, Distance {:.2f}km".format(azimuth, elevation, distance / 1000))
    print("")
    print("")
    print("Test case N2: Northern hemisphere meteor north and east of station")
    sta_lat = 32.3  # deg
    sta_lon = 115.8  # deg
    sta_ele = 37  # meters
    tar_lat = 32.4  # deg
    tar_lon = 116.156  # deg
    tar_ele = 81.1 * 1000
    azimuth, elevation, distance = latlonaltlatlonalt2azel(sta_lat, sta_lon, sta_ele, tar_lat, tar_lon, tar_ele)
    print("")
    print("Station Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(sta_lat, sta_lon, sta_ele))
    print("Target  Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(tar_lat, tar_lon, tar_ele))
    print("Azimuth {:.2f}, Elevation {:.2f}, Distance {:.2f}km".format(azimuth, elevation, distance / 1000))
    print("")
    print("")
    print("Test case N3: Northern hemisphere meteor north and west of station")
    sta_lat = 32.3  # deg
    sta_lon = 115.8  # deg
    sta_ele = 37  # meters
    tar_lat = 32.4  # deg
    tar_lon = 115.356  # deg
    tar_ele = 81.1 * 1000
    azimuth, elevation, distance = latlonaltlatlonalt2azel(sta_lat, sta_lon, sta_ele, tar_lat, tar_lon, tar_ele)
    print("")
    print("Station Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(sta_lat, sta_lon, sta_ele))
    print("Target  Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(tar_lat, tar_lon, tar_ele))
    print("Azimuth {:.2f}, Elevation {:.2f}, Distance {:.2f}km".format(azimuth, elevation, distance / 1000))
    print("")
    print("")
    print("Test case N4: Northern hemisphere meteor south and west of station")
    sta_lat = 32.3  # deg
    sta_lon = 115.8  # deg
    sta_ele = 37  # meters
    tar_lat = 31.908  # deg
    tar_lon = 115.356  # deg
    tar_ele = 81.1 * 1000
    azimuth, elevation, distance = latlonaltlatlonalt2azel(sta_lat, sta_lon, sta_ele, tar_lat, tar_lon, tar_ele)
    print("")
    print("Station Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(sta_lat, sta_lon, sta_ele))
    print("Target  Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(tar_lat, tar_lon, tar_ele))
    print("Azimuth {:.2f}, Elevation {:.2f}, Distance {:.2f}km".format(azimuth, elevation, distance / 1000))
    print("")
    print("")
    print("Test case Flying Doctor: from Baldivis")
    sta_lat = -32.354356  # deg
    sta_lon = 115.805961  # deg
    sta_ele = 37  # meters
    tar_lat = -32.3912  # deg
    tar_lon = 115.8351  # deg
    tar_ele = 1.943 * 1000
    azimuth, elevation, distance = latlonaltlatlonalt2azel(sta_lat, sta_lon, sta_ele, tar_lat, tar_lon, tar_ele)
    print("")
    print("Station Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(sta_lat, sta_lon, sta_ele))
    print("Target  Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(tar_lat, tar_lon, tar_ele))
    print("Azimuth {:.2f}, Elevation {:.2f}, Distance {:.2f}km".format(azimuth, elevation, distance / 1000))
    print("")
    print("")

    print("Test case Meteor")

    sta_lat = -32.3  # deg
    sta_lon = 115.8  # deg
    sta_ele = 37  # meters

    tar_lat = -31.908  # deg
    tar_lon = 116.156  # deg
    tar_ele = 81.1 * 1000
    azimuth, elevation, distance = latlonaltlatlonalt2azel(sta_lat, sta_lon, sta_ele, tar_lat, tar_lon, tar_ele)
    print("")
    print("Station Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(sta_lat, sta_lon, sta_ele))
    print("Target  Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(tar_lat, tar_lon, tar_ele))
    print("Azimuth {:.2f}, Elevation {:.2f}, Distance {:.2f}km".format(azimuth, elevation, distance / 1000))
    print("")
    print("")

    print("Test case reciprocal of meteor")

    tar_lat = -32.3  # deg
    tar_lon = 115.8  # deg
    tar_ele = 37  # meters

    sta_lat = -31.908  # deg
    sta_lon = 116.156  # deg
    sta_ele = 81.1 * 1000

    azimuth, elevation, distance = latlonaltlatlonalt2azel(sta_lat, sta_lon, sta_ele, tar_lat, tar_lon, tar_ele)
    print("")
    print("Station Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(sta_lat, sta_lon, sta_ele))
    print("Target  Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(tar_lat, tar_lon, tar_ele))
    print("Azimuth {:.2f}, Elevation {:.2f}, Distance {:.2f}km".format(azimuth, elevation, distance / 1000))
    print("")
    print("")

    print("Test case zero elevation - east")

    tar_lat = 0  # deg
    tar_lon = 45  # deg
    tar_ele = 6371000 / np.cos(np.radians(45)) - 6371000  # meters

    sta_lat = 0  # deg
    sta_lon = 0  # deg
    sta_ele = 0

    azimuth, elevation, distance = latlonaltlatlonalt2azel(sta_lat, sta_lon, sta_ele, tar_lat, tar_lon, tar_ele)
    print("")
    print("Station Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(sta_lat, sta_lon, sta_ele))
    print("Target  Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(tar_lat, tar_lon, tar_ele))
    print("Azimuth {:.2f}, Elevation {:.2f}, Distance {:.2f}km".format(azimuth, elevation, distance / 1000))
    print("")
    print("")

    print("Test case zero elevation - west")

    tar_lat = 0  # deg
    tar_lon = 315  # deg
    tar_ele = 6371000 / np.cos(np.radians(45)) - 6371000  # meters

    sta_lat = 0  # deg
    sta_lon = 0  # deg
    sta_ele = 0

    azimuth, elevation, distance = latlonaltlatlonalt2azel(sta_lat, sta_lon, sta_ele, tar_lat, tar_lon, tar_ele)
    print("")
    print("Station Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(sta_lat, sta_lon, sta_ele))
    print("Target  Lat: {:.3f} Lon: {:.3f} Ele: {:.1f}".format(tar_lat, tar_lon, tar_ele))
    print("Azimuth {:.2f}, Elevation {:.2f}, Distance {:.2f}km".format(azimuth, elevation, distance / 1000))
    print("")
    print("")
