import geoip2.database

reader = geoip2.database.Reader('./GeoLite2-City_20190423/GeoLite2-City.mmdb')
response = reader.city('47.145.125.28')

print(response.country.iso_code)  # US
print(response.subdivisions.most_specific.name)  # Hawaii
print(response.subdivisions.most_specific.iso_code)  # HI
print(response.city.name)  # Kailua
print(response.postal.code)  # 96734
print(response.location.longitude)
print(response.location.latitude)
reader.close()
