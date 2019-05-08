import psycopg2
import re
import sys
import geoip2.database

reader = geoip2.database.Reader('./GeoLite2-City_20190423/GeoLite2-City.mmdb')


conn = psycopg2.connect("dbname=msf user=msf password=dTtQ/Gtvxch/Q+IijDuMMCaXaAXg4sEf/nIWlIoDc0I=")
curr = conn.cursor()
curr.execute("SELECT address FROM hosts;")
var = curr.fetchall()

open("../globe/population909500.json", 'w').close()

with open("../globe/population909500.json", "a") as myfile:
    myfile.write("[[\"1990\",[")

for ip in var:
    ip = str(ip)
    translation_table = dict.fromkeys(map(ord, ',()\''), None)
    ip = ip.translate(translation_table)

    if '192.168' in ip or '10.0' in ip:
        print("FOUND AN INVALID ADDRESS")
        continue
  

    response = reader.city(ip)

    longitude = str(response.location.longitude)
    latitude = str(response.location.latitude)

    magnitude = str(1.045)

   
    what_to_write =  latitude + "," + longitude + "," + magnitude + ","



    with open("../globe/population909500.json", "a") as myfile:
        print("writing" + what_to_write + "to file...\n")
        myfile.write(what_to_write)
        myfile.close()


with open("../globe/population909500.json", "a") as myfile:
    myfile.write("]]]")
    myfile.close()

reader.close()




#conn.commit()
