import requests

# L'URL de l'API où vous voulez envoyer la requête
url = 'http://api.voicepartner.fr/v1/audios/YOUR_API_KEY'

# Configuration des en-têtes HTTP
headers = {
    'Cache-Control': 'no-cache'
}

# Exécution de la requête GET et enregistrement de la réponse
response = requests.get(url, headers=headers)

# Vérification du statut de la réponse
if response.status_code == 200:
    # Affichage de la réponse
    print(response.text)
else:
    # Gérer l'erreur ici
    print(f"Erreur lors de la requête: {response.status_code}")
