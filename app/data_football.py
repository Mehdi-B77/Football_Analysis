import requests
import json 

API_KEY = 'c2528d08fe92421b9126ee4c4c3a9d9b'
BASE_URL = 'https://api.football-data.org/v4/matches'


def get_football_data():

    headers = {'X-Auth-Token': API_KEY}

    print('Récupération des données de football en cours...')

    response = requests.get(BASE_URL, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Erreur: {response.status_code}")
        return None
    


data = get_football_data()
if data:
    with open('football_data.json', 'w') as f:
        json.dump(data, f, indent=4)
    print('Données de football récupérées et enregistrées dans football_data.json')    
else:
    print('Aucune donnée récupérée , test.')

    