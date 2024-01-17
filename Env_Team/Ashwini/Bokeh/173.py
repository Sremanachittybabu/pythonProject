from bokeh.plotting import figure , show , output_file
import pandas

df = pandas.read_csv("Bokeh\\timeplot.txt")
p= figure(x_axis_type = 'datetime' , height = 100, width = 500)
#pip3.9 install justpy==0.1.5p.yaxis_minor_tick_color = None
q=p.quad(left=df["Start"],right=df["End"],bottom = 0 , top = 1, color = "green")

output_file("Graph.html")
show(p)