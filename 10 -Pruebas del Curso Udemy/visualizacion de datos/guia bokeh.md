# Guía Rápida de Bokeh (Python)

Esta chuleta te ayudará a recordar los elementos y atributos principales para crear gráficas interactivas con Bokeh. Úsala como referencia rápida para tus proyectos.

---

## Instalación

```bash
pip install bokeh
```

---

## Estructura Básica

```python
from bokeh.plotting import figure, show, output_file

output_file("mi_grafica.html")
p = figure(title="Título", x_axis_label='X', y_axis_label='Y')
p.line([1, 2, 3], [4, 6, 2], legend_label="Leyenda", line_width=2)
show(p)
```

---

## Elementos Principales (`figure`)

| Elemento     | Descripción                                   |
|--------------|-----------------------------------------------|
| figure()     | Crea la figura/base del gráfico               |
| line()       | Línea                                          |
| scatter()    | Dispersión/puntos                             |
| circle()     | Círculos                                      |
| square()     | Cuadrados                                     |
| triangle()   | Triángulos                                    |
| rect()       | Rectángulos                                   |
| vbar()       | Barras verticales                             |
| hbar()       | Barras horizontales                           |
| patch()      | Polígonos                                     |
| area()       | Área bajo la curva                            |
| step()       | Línea escalonada                              |
| image()      | Imágenes/Matrices                             |

---

## Atributos Comunes de Figuras

| Atributo          | Descripción                  |
|-------------------|-----------------------------|
| title             | Título del gráfico           |
| x_axis_label      | Etiqueta eje X               |
| y_axis_label      | Etiqueta eje Y               |
| width, height     | Dimensiones en pixeles       |
| x_range, y_range  | Rango de los ejes            |
| background_fill_color | Color de fondo           |
| toolbar_location  | Ubicación de la barra de herramientas |

---

## Atributos Comunes de Glyphs (Figuras)

| Atributo       | Descripción                  |
|----------------|-----------------------------|
| line_color     | Color de línea               |
| line_width     | Grosor de línea              |
| fill_color     | Color de relleno             |
| fill_alpha     | Transparencia de relleno     |
| legend_label   | Etiqueta de leyenda          |
| size           | Tamaño (círculos, puntos)    |
| alpha          | Transparencia general        |
| marker         | Tipo de marcador             |

---

## Ejemplos de Glyphs

```python
p.line(x, y, line_width=2, color="navy")
p.circle(x, y, size=10, color="red", alpha=0.5)
p.vbar(x=x, top=valores, width=0.5, color="green")
```

---

## Widgets y Layouts

| Elemento         | Descripción                 |
|------------------|----------------------------|
| Slider           | Deslizador                 |
| Button           | Botón                      |
| Select           | Menú desplegable           |
| CheckboxGroup    | Grupo de checkboxes        |
| TextInput        | Campo de texto             |
| Column, Row      | Layouts de columnas/filas  |

```python
from bokeh.layouts import column, row
from bokeh.models import Slider, Button

slider = Slider(start=0, end=10, value=1, step=0.1, title="Deslizador")
layout = column(p, slider)
show(layout)
```

---

## Herramientas Interactivas

| Herramienta        | Descripción                  |
|--------------------|-----------------------------|
| pan                | Desplazar vista              |
| wheel_zoom         | Zoom con scroll              |
| box_zoom           | Zoom por selección           |
| reset              | Restaurar vista              |
| hover              | Tooltip al pasar el ratón    |
| save               | Guardar gráfico como imagen  |
| tap                | Selección por clic           |

```python
p.add_tools(HoverTool(tooltips=[("x", "$x"), ("y", "$y")]))
```

---

## Fuentes de Datos

| Elemento            | Descripción               |
|---------------------|--------------------------|
| ColumnDataSource    | Fuente de datos principal |

```python
from bokeh.models import ColumnDataSource

source = ColumnDataSource(data=dict(x=[1,2,3], y=[4,5,6]))
p.line('x', 'y', source=source)
```

---

## Guardar y Mostrar

| Función          | Descripción                         |
|------------------|-------------------------------------|
| output_file()    | Guardar como HTML                   |
| show()           | Mostrar en navegador                |
| save()           | Guardar sin mostrar                 |
| output_notebook()| Mostrar en Jupyter                  |

---

## Colores

- Nombres: `"red"`, `"blue"`, `"green"`, etc.
- Hexadecimales: `"#FF0000"`
- RGBA: `"rgba(255,0,0,0.5)"`

---

## Referencias Útiles

- [Documentación Oficial](https://docs.bokeh.org/en/latest/docs/user_guide.html)
- [Galería de Ejemplos](https://docs.bokeh.org/en/latest/docs/gallery.html)

---

¡Feliz visualización de datos con Bokeh!
