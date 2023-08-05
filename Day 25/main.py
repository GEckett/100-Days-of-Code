#with open("weather_data.csv") as weather:
#    forecasts = weather.readlines()
#    print(forecasts)

#import csv

#with open("weather_data.csv") as weather:
#    forecasts = csv.reader(weather)
#    temps = []
#    for row in forecasts:
#        if row[1] != "temp":
#            temps.append(int(row[1]))
#    print(temps)

import pandas

data = pandas.read_csv("weather_data.csv")

#data_dict = data.to_dict()
#print(data_dict)

#temp_list_max = data["temp"].max()
#print(temp_list_max)

#print(data["temp"].max())
#print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
monday_temp_c = int(monday.temp)
monday_temp_f = (monday_temp_c * (9/5)) + 32
print(monday_temp_f)










