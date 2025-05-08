from motion_detector import df

from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource 

df["Start_string"]=df["Start"].dt.strftime("%H:%m:%S %d-%m-%Y")
df["End_string"]=df["End"].dt.strftime("%H:%m:%S %d-%m-%Y")

cds=ColumnDataSource(df)

p = figure(x_axis_type='datetime', height=500, width=500, sizing_mode="stretch_width", title="Grafico de movimiento")
p.yaxis.minor_tick_line_color = None
p.yaxis[0].ticker.desired_num_ticks = 1



hover = HoverTool(tooltips=[("Start ","@Start_string"),("End ","@End_string")])
p.add_tools(hover)

q = p.quad(left="Start", right="End", bottom=0, top=1, color="orange", source=cds)

output_file("Grafico.html")

show(p)