import requests

# URL de l'API à laquelle effectuer la requête POST
url = 'https://api.voicepartner.fr/v1/campaign/send'

# Les données à envoyer en JSON
data = {
    'apiKey': 'YOUR_API_KEY',  # Remplacez par votre clé API réelle
    'tokenAudio': 'TOKEN_AUDIO',  # Remplacez par le token audio réel
    'emailForNotification': 'email@example.com',  # Remplacez par l'email de notification souhaité
    'phoneNumbers': '06xxxxxxxx',  # Remplacez par le(s) numéro(s) de téléphone réel(s)
    # Ajoutez les autres paramètres optionnels si nécessaire
    # 'sender': 'VotreNuméro',  # Optionnel
    # 'scheduledDate': 'YYYY-mm-dd H:i:s',  # Optionnel
    # 'notifyUrl': 'https://your.notify.url',  # Optionnel
}

# Configuration des en-têtes HTTP
headers = {
    'Content-Type': 'application/json',
    'Cache-Control': 'no-cache'
}

# Exécution de la requête POST avec les données JSON
response = requests.post(url, json=data, headers=headers)

# Vérification s'il y a eu des erreurs pendant l'exécution de la requête
if response.status_code != 200:
    print(f'Erreur cURL : {response.status_code}')
else:
    # Affichage de la réponse
    print(f'Réponse : {response.text}')
