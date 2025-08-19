from flask import Flask, render_template  # Importa la clase Flask del paquete flask

app = Flask(__name__)  # Crea una instancia de la aplicación Flask


# Define la ruta principal de la web ('/')
@app.route("/")
def home():
    # Esta función se ejecuta cuando se accede a la página principal
    return render_template("home.html")

# Define la ruta principal de la web ('/')
@app.route("/about/")
def about():
    # Esta función se ejecuta cuando se accede a la página principal
    return render_template("about.html")


# Ejecuta la aplicación solo si este archivo es el principal
if __name__ == "__main__":
    app.run(debug=True)  # Inicia el servidor en modo debug
