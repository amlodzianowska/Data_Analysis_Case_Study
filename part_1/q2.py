import csv
def q2_delay_type():
    with open('airplane.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # To skip header
        next(csv_reader)

        # Setting up variables
        max = 0
        delays = {
            "carrier" : 0,
            "weather" : 0,
            "nas" : 0,
            "security" : 0,
            "late_aircraft" : 0,
            }

        for line in csv_reader:
            #Skipping rows in csv pile that contain no delay data
            if line[8] == '':
                continue
            #Calculating totals for each delay type
            else:
                delays = {
                    "carrier" : delays["carrier"] + float(line[8]),
                    "weather" : delays["weather"] + float(line[9]),
                    "nas" : delays["nas"] + float(line[10]),
                    "security" : delays["security"] + float(line[11]),
                    "late_aircraft" : delays["late_aircraft"] + float(line[12]),
                }
        
        #Finding out the delay type that caused the most time delay
        for key in delays.keys():
            if delays[key] > max:
                max = delays[key]
                maxname = key
        
        print("The longest delay time: " + str(max))
        print("Delay cause: " + maxname)

q2_delay_type()