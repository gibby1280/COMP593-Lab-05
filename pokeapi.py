from dad_jokes_api import search_poke_api
from pastebin import post_new_paste
import sys 

def main():
    search_term = get_search_term()
    poke_list = search_poke_api(search_term)
    if poke_list:
        title, body_text = get_paste_content(poke_list, search_term)
        paste_url = post_new_paste(title, body_text)
        print(f'URL of Jokes paste: {paste_url}')

def get_search_term():
    num_params = len(sys.argv) - 1 
    if num_params > 0:
        return sys.argv[1]
    else:
        print('Error: Missing search term')
        sys.exit(1)

def get_paste_content(jokes_list, search_term):


    title = f'Dad Jokes Containing the Term "{search_term}"'

    divider = '-' *20 
    body_text = ''
    for poke in poke_list:
        body_text += poke + '\n'
        body_text += divider + '\n'

    return title, body_text


if __name__ == "__main__":
    main()