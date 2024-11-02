from geotext import GeoText

text = "I have been to New York and Paris, but I have never been to Japan."

places = GeoText(text)

places(text)

print(places.cities)

print(places.countries)

print(places.country_mentions)


