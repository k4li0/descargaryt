from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

@app.route("/descargar", methods=["POST"])
def descargar_video():
    datos = request.get_json()
    url = datos.get("url")

    if not url:
        return jsonify({"error": "Falta la URL"}), 400

    try:
        comando = ["yt-dlp", "-o", "video.%(ext)s", url]
        subprocess.run(comando, check=True)

        return jsonify({"mensaje": "Descarga completada", "archivo": "video.mp4"}), 200

    except subprocess.CalledProcessError:
        return jsonify({"error": "Falló la descarga"}), 500

if __name__ == "__main__":
    app.run(debug=True)
