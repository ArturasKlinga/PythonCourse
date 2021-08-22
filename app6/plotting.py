from main import df
from bokeh.plotting import figure, show, output_file

p = figure(x_axis_type='datetime', height=100, width=500, title="Motion Graph", sizing_mode='scale_width')
p.yaxis.minor_tick_line_color = None
p.yaxis.ticker.desired_num_ticks = 1
p.title.align = 'center'
p.title.text_font_size = "25px"

q = p.quad(left=df["Start"], right=df["End"], bottom=0, top=1, color="green")

output_file("graph.html")
show(p)
