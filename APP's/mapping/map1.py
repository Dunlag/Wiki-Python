import folium
import pandas

data = pandas.read_csv("./Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])

map = folium.Map(
    location=[38.58, -99.09],
    zoom_start=6,
    tiles="CartoDB positron",
    attr="Map data © CartoDB contributors",
)

fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    fg.add_child(
        folium.Marker(
            location=[lt,ln],
            popup="Hi I am a Marker",
            icon=folium.Icon(color="green"),
        )
    )


map.add_child(fg)
# Guardar el mapa en un archivo HTML
map.save("./Map1.html")
