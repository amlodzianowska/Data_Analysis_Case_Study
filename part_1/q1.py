import csv
def q1_longest_flight():
    with open('airplane.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # To skip header
        next(csv_reader)

        # Setting up variables 
        airline_info = {}
        max = 0
        maxname = ""


        for line in csv_reader:
            flight = line[2]+ " " +line[3]

            #Skipping rows that are missing data in ACTUAL_ELAPSED_TIME column (cancelled flights)
            if line[6] == '':
                continue

            #Collecting data from csv file into an airline_info dictionary
            else:
                if flight in airline_info.keys():
                    total = float(airline_info[flight]["time"]) + float(line[6])
                    number = int(airline_info[flight]["count"]) + 1
                    airline_info[flight] = {
                        "time" : total,
                        "count" : number
                    }
                else:
                    airline_info[flight]= {
                        "time" : float(line[6]),
                        "count" : 1 
                    }

        #Finding out what is the longest flight on average using the data collected in airline_info dictionary
        for flight in airline_info:
            avg = float(airline_info[flight]["time"])/float(airline_info[flight]["count"])
            if avg > max:
                max = avg
                maxname = flight

        print("The longest flight is " + str(maxname) + " " + "{:.2f}".format(max))

q1_longest_flight()