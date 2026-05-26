import os
from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

# Ta cle API est directement integree ici
VOTRE_CLE =genai.Client(api_key="AIzaSyA759W7Ucv0mGGqm9k081AMhfPuOG_2xJg")

# Initialisation directe du client Google GenAI
client = genai.Client(api_key="AIzaSyA7S9W7Ucv0mGGqm9k08lAMhfPuOG_2xJg")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form.get('message')
    if not user_message:
        return jsonify({'error': 'Vide'}), 400

    try:
        consigne = "Tu es Dieumerci IA. Reponds amicalement en francais."
        texte = f"{consigne}\nUtilisateur: {user_message}\nIA:"
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=texte,
        )
        return jsonify({'response': response.text})
    except Exception as e:
        # Cette ligne va afficher le vrai message de bug dans ta bulle de discussion sur Chrome
        return jsonify({'response': f"Erreur Google : {str(e)}"}), 200
@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory('.', 'manifest.json')

@app.route('/sw.js')
def serve_sw():
    return send_from_directory('.', 'sw.js')
if __name__ == '__main__':
    app.run(debug=True)