import pandas
#import matplotlib
data = pandas.read_csv("app3//reviews.csv")
print(data.head())
data.hist("Rating")