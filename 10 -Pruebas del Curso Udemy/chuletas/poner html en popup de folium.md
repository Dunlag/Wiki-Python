## 🧾 Folium: Popups con HTML

### 🧩 ¿Para qué sirve?
Puedes personalizar los popups de tus mapas en **Folium** usando **HTML**, para mostrar texto con estilo, enlaces, y más.

---

### ✅ Ejemplo 1: Texto HTML básico en el popup

```python
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# HTML para mostrar la altura del volcán
html = """<h4>Volcano information:</h4>
Height: %s m
"""

# Crear el mapa
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")

# Añadir marcadores con popups
for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    popup = folium.Popup(iframe)
    fg.add_child(folium.Marker(location=[lt, ln], popup=popup, icon=folium.Icon(color="green")))

map.add_child(fg)
map.save("Map_html_popup_simple.html")
```

🧠 *Este ejemplo muestra una ventana emergente con el texto "Volcano information" y la altura del volcán en metros.*

---

### 🔗 Ejemplo 2: Nombre con enlace a Google

```python
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

# HTML con enlace al nombre del volcán
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=100)
    popup = folium.Popup(iframe)
    fg.add_child(folium.Marker(location=[lt, ln], popup=popup, icon=folium.Icon(color="green")))

map.add_child(fg)
map.save("Map_html_popup_advanced.html")
```

🔍 *En este caso, el nombre del volcán aparece como un enlace que abre una búsqueda en Google en una nueva pestaña.*

---

### 📌 Detalles útiles

- `folium.IFrame`: Permite incrustar HTML personalizado dentro del popup.
- `target="_blank"`: Hace que el enlace se abra en una nueva pestaña.
- Puedes personalizar aún más el popup con CSS dentro del HTML si lo necesitas.

---
