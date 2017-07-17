import requests
from constants import BASE_URL,APP_ACCESS_TOKEN
from get_users_post import  get_users_post
                                                # Importing functions and constants from other files

def like_a_post(insta_username) :           # Defination of like_a_post() function
    media_id =get_users_post(insta_username)                # Calling of get_users_post() function
    request_url = ('%smedia/%s/likes') % (BASE_URL,media_id)            # Making reques URL


    payload = {"access_token": APP_ACCESS_TOKEN}            # Making payload variable
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()            # Making request to server nad stroeing response in json fromat

    if post_a_like['meta']['code'] == 200:          # Checking response from server
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. (Try again)'
