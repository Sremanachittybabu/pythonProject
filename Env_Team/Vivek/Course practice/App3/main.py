from bokeh.plotting import figure, show
from bokeh.io import output_file
import pandas as pd

df = pd.read_csv('data.csv')
x = df["x"]
y = df["y"]

# Specify the output file (optional)
output_file("line_plot.html")

# Create a figure
p = figure(title="Simple Line Plot", x_axis_label='X-axis', y_axis_label='Y-axis')

# Add a line to the figure
p.line(x, y, line_width=2)

# Show the plot
show(p)

# df1 = pd.read_csv('adbe.csv')