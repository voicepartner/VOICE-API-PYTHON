import requests

# Activer l'affichage des erreurs pour le débogage
# En Python, les erreurs sont affichées par défaut lorsqu'elles se produisent.

# L'URL de l'API pour annuler la campagne
apiKey = 'YOUR_API_KEY'  # Remplacez par votre clé API réelle
campaignId = 'CAMPAIGN_ID'  # Remplacez par l'ID de campagne réel

# Construction de l'URL avec la clé API et l'ID de campagne
url = f"https://api.voicepartner.fr/v1/campaign/cancel/{apiKey}/{campaignId}"

# Configuration des en-têtes HTTP
headers = {
    'Cache-Control': 'no-cache'
}

# Exécution de la requête DELETE
response = requests.delete(url, headers=headers)

# Vérification s'il y a eu des erreurs pendant l'exécution de la requête
if response.status_code != 200:
    print(f'Erreur cURL : {response.status_code}')
else:
    # Affichage de la réponse
    print(f'Réponse : {response.text}')
