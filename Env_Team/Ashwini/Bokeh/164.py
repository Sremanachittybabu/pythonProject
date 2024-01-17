#Plotting graph excercise

#importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file,show
import pandas

#data read from csv
df = pandas.read_csv("bachelors.csv")
x = df["Year"]
y = df["Engineering"]

#output file
output_file("bachelor.html")

#figure chart
f = figure()

#create line plot
f.line(x,y)

show(f)