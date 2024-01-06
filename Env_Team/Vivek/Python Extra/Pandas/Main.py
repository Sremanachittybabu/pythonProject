import pandas
data = pandas.read_csv("weather_data.csv")
print(data[data.temp == data.temp.max()])

