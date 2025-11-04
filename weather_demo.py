import requests

cities = input("enter the city names:").split()
for city in cities:
    url = f"https://wttr.in/{city}?format=3"
    report = requests.get(url)
    print("weather:", report.text)