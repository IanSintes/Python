# app6_web.py
from flask import Flask

def iniciar_web():
    print("\n--- APLICACIÓ 6: Servidor web Flask ---")

    app = Flask(__name__)

    @app.route("/")
    def index():
        return "<h1>Benvingut al projecte 76!</h1><p>Aquesta és una web feta amb Flask.</p>"

    print("Obre http://127.0.0.1:5000 al navegador.")
    app.run()

