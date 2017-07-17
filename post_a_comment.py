import requests
from get_users_post import get_users_post
from constants import APP_ACCESS_TOKEN,BASE_URL
                                                    # Importing functions and constants from other files

def post_a_comment(insta_username) :                # definatio of get_users_post() frunction
    media_id = get_users_post(insta_username)               # Calling of get_users_post() function
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)          # Making Request URL
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()         # Requesting from serever and storing response in json format

    comment = []  # List to store comment
    a = 0
    while len(comment_info['data']) > a:
        comment.append(comment_info['data'][a]['text'])             # Appending data in list
        a = a + 1

    print(comment)

    comment_text = raw_input("Your comment : ")
    if len(comment_text) == 0 :
        print "It's not a valid comment"

    payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)             # Making Request URL
    print 'POST request url : %s' % (request_url)
    make_comment = requests.post(request_url, payload).json()           # Requesting from serever and storing response in json format

    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"
