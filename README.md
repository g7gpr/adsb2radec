# adsb2radec
Convert ADSB (Automatic Dependent Surveillance-Broadcast) bytes from dump1090 to RaDec (right ascension and declination) and issue over a tcp server.

This project takes ADSB strings from a dump1090 server and converts them to RaDec based on the location of the station. 

The output can be read by 

`nc address port`

and sent to a file by 

`nc address port > radec.txt`

It requires https://github.com/wmpg/WesternMeteorPyLib.


