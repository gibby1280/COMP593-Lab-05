import requests

POKE_API_URL = 'https://pokeapi.co/'
POKE_API_SEARCH = f'{POKE_API_URL}/search'

def main():
    pokemon = search_poke_api('pikachu')
    pass

def search_poke_api(search_term, page=1, limit=20):
    query_params = {
        'page' : page,
        'limit' : limit,
        'term' : search_term
    }

    # Setup the header params 
    header_params = { 
        'Accept' : 'appilcation/json'
    }


    
    # Send a GET for a random dad joke
    print('Getting a random dad joke...', end=" ")

    resp_msg = requests.get(POKE_API_SEARCH, headers=header_params)

    # Check whether the requesr was successful
    if resp_msg.ok:
        print('success')
        body_dict = resp_msg.json()
        poke_portion = body_dict['results']
        poke_list = [p['poke'] for p in poke_portion]
        return poke_list
    else:
        print('failure')
        print(f"Response code {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.text}")