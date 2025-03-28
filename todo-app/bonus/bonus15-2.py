import csv

with open("files/weather.csv", 'r') as file:
    data = list(csv.reader(file))

print(data)

city = input("Enter a city: ")

for station, temp in data[1:]:
    # print(station + " " + temp)
    if station == city:
        print(temp)