import csv
def q4_most_expensive_day():
    with open('airplane.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # To skip header
        next(csv_reader)

        # Setting up variables 
        flight_info = {}
        max = 0
        min = None
        maxday = ""
        minday = ""

        delay = []
        cancellation = []
        weighted = []
        days = []


        for line in csv_reader:
            day = line[0]
            
            if day not in flight_info.keys():
                if line[4] == '':
                    flight_info[day] = {
                        "delay" : 0,
                        "cancellation" : 1,
                        "weighted" : 0 
                    }
                    flight_info[day]['cancellation'] = 1
                elif line[4] != '' and float(line[4]) > 0:
                    flight_info[day] = {
                        "delay" : 1,
                        "cancellation" : 0,
                        "weighted" : 0
                    }
            else:
                if line[4] == '':
                    flight_info[day]['cancellation'] += 1
                elif line[4] != '' and float(line[4]) > 0:
                    flight_info[day]['delay'] += 1
        #Finding out the most and least expensive days in the dataset
        for item in flight_info.items():
            weighted_value = item[1]['delay'] + item[1]['cancellation'] * 8
            item[1]['weighted'] = weighted_value
            if item[1]['weighted'] > max:
                max = item[1]['weighted']
                maxday = item[0]
            if min == None:
                min = item[1]['weighted']
                minday = item[0]
            elif min > item[1]['weighted']:
                min = item[1]['weighted']
                minday = item[0]
        for day in flight_info.keys():
            delay.append(flight_info[day]['delay'])
            cancellation.append(flight_info[day]['cancellation'])
            weighted.append(flight_info[day]['weighted'])
            days.append(day)
        print("Outputs for vizualization:")
        print(delay)
        print(cancellation)
        print(weighted)
        print(days)
        print(f"The most expensive day was {maxday} at {max}.")
        print(f"The least expensive day was {minday} at {min}.")

q4_most_expensive_day()