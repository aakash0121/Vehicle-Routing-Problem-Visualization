import csv
import random


FILE_NAME = 'data.csv'
CITY_COUNT = 25

# write co-ordinates in csv file
def writeCsv(filename, city_count):
    # fields = ['latitudes', 'longitudes']

    with open(filename, 'w') as f:
        csv_write = csv.writer(f)

        # write headers
        # csv_write.writerow(fields)

        # write rows with co-ordinates choosen at random
        for i in range(city_count):
            # range of latitudes are -85 to 85
            latitude = random.random()*(170) - 85

            # range of longitudes are -180 to 180
            longitude = random.random()*(360) - 180

            data = [latitude, longitude]

            # writing in csv
            csv_write.writerow(data)
        
def loadData():
    global FILE_NAME
    # intializing list for storing co-ordinates of cities(or nodes)
    cityList = []

    with open(FILE_NAME, 'r') as f:
        csvreader = csv.reader(f)

        for row in csvreader:
            cityList.append(tuple(map(float, row)))
    
    return cityList

if __name__ == "__main__":
    writeCsv(FILE_NAME, CITY_COUNT)