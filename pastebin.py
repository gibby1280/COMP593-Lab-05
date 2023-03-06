import requests

API_POST_URL = 'https://pastebin.com/api/api_post.php'
DEV_KEY = '5uqgt2OfkwVjF4KEwUkqRSzBG1_Q4ylG'

def main():
    paste_url = post_new_paste('Whatever paste', 'a bunch of crap')
    pass

def post_new_paste(title, body_text, experation, listed): 
    """Creates a new public PasteBin paste

    Args:
        title (str): Paste title
        body_text (str): Paste body 
        experation (str, optional): How long the paste will last 
        listed (bool, optional) : Whether the paste is listed or not


    Returns:
        str: URL of  the new paste. None if unsuccessful.
    """
    
    # Create dictionary of param values 
    params = {
        'api_dev_kev' : '5uqgt2OfkwVjF4KEwUkqRSzBG1_Q4ylG',
        'api_option' : 'paste', 
        'api_paste_code' : body_text,
        'api_paste_expire_date' : experation, 
        'api_paste_private' : 0 if listed else 1 
    }

    # Send the POST request to the PasteBin API
    print("Posting a new paste to PasteBin...", end=" ")
    resp_msg = requests.posts(API_POST_URL, data=params)
    
    # Check if paste was created successfully 
    if resp_msg.ok:
        print('success')
        print(f'URL of the new paste: {resp_msg.text}')
        return resp_msg.text
    else:
        print('failure')
        print(f"Response code {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.text}")
    
    pass

if __name__ == "__main__":
    main()