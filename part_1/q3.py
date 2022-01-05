import csv
from collections import defaultdict


def find_most_pop_destination_with_least_flown():
    with open('airplane.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # To skip header
        next(csv_reader)

        # Setting up variables
        airline_info = {}
        min_flights = None
        minname = ""
        dest_values = defaultdict(int)
        max_destinations = None
        destination_name = ""

        # Reading the CSV and getting relevant data
        for line in csv_reader:
            carrier = line[1]
            destination = line[3]
            if carrier not in airline_info:
                airline_info[carrier] = {
                    'destinations': [destination],
                    'count': 1
                }
            else:
                airline_info[carrier]['destinations'].append(destination)
                airline_info[carrier]['count'] += 1

        # Finding out the airline with the least number of flights using 
        # airline_info[carrier]['count']
        for carrier in airline_info:
            if minname == "":
                minname = carrier
                min_flights = airline_info[carrier]['count']
            else:
                if airline_info[carrier]['count'] < min_flights:
                    minname = carrier
                    min_flights = airline_info[carrier]['count']

        for destination in airline_info[minname]['destinations']: 
            dest_values[destination] += 1

        for destination_value in dest_values:
            if destination_name == "":
                destination_name = destination_value
                max_destinations = dest_values[destination_value]
            else:
                if dest_values[destination_value] > max_destinations:
                    destination_name = destination_value
                    max_destinations = dest_values[destination_value]
        print(f"{minname} is the carrier with the least amount of flights ({min_flights}), and their most popular destination is {destination_name}.")
find_most_pop_destination_with_least_flown()