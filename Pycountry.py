import pycountry

countries = list(pycountry.countries)
# print(c)

for country in countries:
    print(country.name,country.code)