# Fetch data from Metro Transit
# Author: Vu Tran

# Imports the python requests library
import sys

import requests

# This program will fetch data about bus routes and providers in the form of json objects
# Get request function to get all the providers in metro transit

# Exception handling to take care of all the request exceptions
try:
    provider_request = requests.get("http://svc.metrotransit.org/NexTrip/Providers?format=json")

    # Get request to get the list of the transit routes in service to day
    today_routes = requests.get("http://svc.metrotransit.org/NexTrip/Routes?format=json")

    # User input the direction they want to travel ie. 4 would be north bound
    direction = int(input("Which direction?\n"))

    # Get request to get the direction of specific route
    route_direction = requests.get("http://svc.metrotransit.org/NexTrip/Directions/" + str(direction) + "?format=json")

    # User inputs the route number
    route = input("What is your route?\n")

    # Get request to get the bus stop
    bus_stops = requests.get(
        "http://svc.metrotransit.org/NexTrip/Stops/" + route + "/" + str(direction) + "?format=json")

    # print(route_direction.text)
    # print(route_direction.text)
    print(today_routes.text)
    # print(provider_request.text)
    print(bus_stops.text)

except requests.exceptions.RequestException as e:
    print(e)
    sys.exit(1)
