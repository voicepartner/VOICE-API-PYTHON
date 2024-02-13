import requests
import json

# Activer l'affichage des erreurs pour le débogage
# En Python, les erreurs sont affichées par défaut lorsqu'elles se produisent.

# L'URL de l'API pour envoyer le message vocal
url = 'http://api.voicepartner.fr/v1/tts/send'

# Les données à envoyer en JSON
data = {
    'apiKey': 'YOUR_API_KEY',  # Remplacez par votre clé API réelle
    'phoneNumbers': '06XXXXXXXX',  # Remplacez par le(s) numéro(s) de téléphone réel(s)
    'text': 'Mon premier test',  # Remplacez par le texte que vous souhaitez convertir en parole
    # 'speed': '1',  # Optionnel: Vitesse de la parole
    # 'notifyUrl': 'http://...',  # Optionnel: URL de notification
    # 'scheduledDate': 'YYYY-mm-dd H:i:00',  # Optionnel: Date prévue pour l'envoi
}

# Encodage des données en JSON
data_json = json.dumps(data)

# Configuration des en-têtes HTTP
headers = {
    'Content-Type': 'application/json',
    'Cache-Control': 'no-cache'
}

# Exécution de la requête POST avec les données JSON
response = requests.post(url, data=data_json, headers=headers)

# Vérification s'il y a eu des erreurs pendant l'exécution de la requête
if response.status_code != 200:
    print(f'Erreur cURL : {response.status_code}')
else:
    # Affichage de la réponse
    print(f'Réponse : {response.text}')
