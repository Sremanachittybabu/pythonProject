#Plotting graph excercise

#importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file,show

#data
x = [1,2,3,4,5]
y = [6,7,8,9,10]

#output file
output_file("circle.html")

#figure chart
f = figure()

#create circle plot
f.circle(x,y)

show(f)