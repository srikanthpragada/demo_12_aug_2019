import requests
import sys

user = "scottallen"
resp = requests.get(f"https://api.github.com/users/{user}")
if resp.status_code == 404:
    print("Sorry! User not found!")
    sys.exit(0)


details = resp.json()

print("Name      : ", details['name'])
print("Company   : ", details['company'])
print("Location  : ", details['location'])
print("No. Repos : ", details['public_repos'])

