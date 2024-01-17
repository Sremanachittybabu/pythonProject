#Plotting graph excercise

#importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file,show
import pandas

#data read from csv
df = pandas.read_csv("data.csv")
x = df["x"]
y = df["y"]

#output file
output_file("line.html")

#figure chart
f = figure()

#create line plot
f.line(x,y)

show(f)