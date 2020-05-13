import csv
import random

# write co-ordinates in csv file
def writeCsv(filename, data):
    with open(filename, 'w') as f:
        csv_write = csv.writer(f)

        for i in range(len(data)):
            latitude = data[i][0]

            longitude = data[i][1]

            d = [latitude, longitude]

            # writing in csv
            csv_write.writerow(d)
        
def loadData(filename):
    # intializing list for storing co-ordinates of cities(or nodes)
    cityList = []
    
    with open(filename, 'r') as f:
        csvreader = csv.reader(f)

        for row in csvreader:
            cityList.append(tuple(map(float, row)))
    
    return cityList