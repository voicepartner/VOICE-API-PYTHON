import requests
import json

# L'URL de l'API où vous voulez envoyer la requête
url = 'https://api.voicepartner.fr/v1/audio-file/rename'

# Les données que vous souhaitez envoyer en JSON
data = {
    'apiKey': 'YOUR_API_KEY',
    'tokenAudio': 'TOKEN_DU_FICHIER_AUDIO',
    'filename': 'Nom du fichier'
}

# Encodage des données en JSON
data_json = json.dumps(data)

# Envoi de la requête POST avec les données JSON
headers = {
    'Content-Type': 'application/json'
}
response = requests.post(url, data=data_json, headers=headers)

# Affichage de la réponse
print(response.text)
