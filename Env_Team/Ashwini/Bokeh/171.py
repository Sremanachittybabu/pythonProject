import pandas
from bokeh.plotting import figure, output_file, show
 
p=figure(width=500,height=400,tools='pan')
 
p.title ="Earthquake"
p.title.text_color="Red"
p.title.text_font="times"
p.title.text_font_style="bold"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label="Times"
p.yaxis.axis_label="Value"    
 
p.line([1,2,3,4,5],[5,5,5,3],line_width = 2 , color = "red")
output_file("plotter.html")
show(p)