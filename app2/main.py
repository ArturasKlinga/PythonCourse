import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09], zoom_start=6)

fg = folium.FeatureGroup(name="My map")

for lt, ln, el, na in zip(lat, lon, elev, name):
    fg.add_child(folium.CircleMarker(location=[lt, ln], fill=True, radius=6, popup=str(na) + "\n" + str(el) + " m.",
                                     fill_color=color_producer(el), color='grey', fill_opacity=0.7))

map.add_child(fg)

map.save("Map1.html")
