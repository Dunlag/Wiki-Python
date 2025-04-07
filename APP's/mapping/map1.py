import folium
import pandas

data = pandas.read_csv("./Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"



map = folium.Map(
    location=[38.58, -99.09],
    zoom_start=6,
    tiles="CartoDB positron",
    attr="Map data © CartoDB contributors",
)

fg = folium.FeatureGroup(name="My Map")

# Agregar marcadores al mapa
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(
        folium.CircleMarker(
            location=[lt, ln],
            popup=folium.Popup(f"Elevation: {el}m", parse_html=True),
            color=color_producer(el), fill=True, fill_color=color_producer(el), fill_opacity=1,        )
    )


fg.add_child(folium.GeoJson(open("./world.json", "r",encoding='utf-8-sig').read()))

map.add_child(fg)
# Guardar el mapa en un archivo HTML
map.save("./Map1.html")
