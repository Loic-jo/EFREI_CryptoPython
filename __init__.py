from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') #comm

key = b'6mC_b4ZmPO_2kFAsqNLfNv5mBeZk3cPTCNfP2doKMGg='
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

@app.route('/decrypt/', methods=['POST'])
def decryptage():
    try:
        data = request.get_json()
        token = data.get("token", "")
        decrypted = f.decrypt(token.encode()).decode()
        return jsonify({"original": decrypted})
    except Exception as e:
        return jsonify({"error": "Échec du déchiffrement", "details": str(e)}), 400

                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
