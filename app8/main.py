from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file

end = datetime.date.today()
start = end - datetime.timedelta(days=180)
df = data.DataReader(name="BTC-USD", data_source="yahoo", start=start, end=end)


def inc_dec(c, o):
    if c > o:
        value = "Increase"
    elif c < o:
        value = "Decrease"
    else:
        value = "Equal"
    return value


df["Status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]

df["Middle"] = (df.Open + df.Close) / 2
df["Height"] = abs(df.Close - df.Open)

p = figure(x_axis_type='datetime', width=1000, height=300, sizing_mode="stretch_both")
p.title.text = "Bitcoin Chart"
p.title.align = "center"
p.title.text_font_size = "30pt"
p.xaxis.axis_label = "Date"
p.yaxis.axis_label = "Price ($)"
p.toolbar_location = None
p.grid.grid_line_alpha = 0.7

hours_12 = 12 * 60 * 60 * 1000

p.segment(df.index, df.High, df.index, df.Low, color="Black")

p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"],
       hours_12, df.Height[df.Status == "Increase"], fill_color="#CCFFFF", line_color="black")

p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"],
       hours_12, df.Height[df.Status == "Decrease"], fill_color="#FF3333", line_color="black")

output_file("chart.html")
show(p)
