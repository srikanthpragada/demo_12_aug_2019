import requests
import sys

resp = requests.get("https://restcountries.eu/rest/v2/all")
if resp.status_code != 200:
    print("Sorry! Could not get countries details!")
    sys.exit(0)

countries = resp.json()

for c in sorted(countries, key=lambda country: country['population'], reverse=True)[:10]:
    print(f"{c['name']:60s} {c['population']}")

print("\nHighly dense countries\n")

countries2 = filter(lambda c: c['population'] != 0 and c['area'] is not None, countries)

for c in sorted(countries2, key=lambda country: float(country['population']) / float(country['area']), reverse=True)[:10]:
    print(f"{c['name']:60s} {float(c['population']) / float(c['area'])}")
