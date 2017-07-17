from get_user_id  import get_user_id
from constants import BASE_URL,APP_ACCESS_TOKEN
import requests
            # Importing functions and constants from other files

def get_user_info(insta_username):          # Defination of function get_user_info
    user_id = get_user_id(insta_username)               # Calling of get_user_id() function
    if user_id == None:                     # Checking response of get_user_id() function
        print 'User does not exist! \n'
    else:
        request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)             # Making request URL
        print 'GET request url : %s' % (request_url)
        user_info = requests.get(request_url).json()            # Making request to server and storing response in json format

        if user_info['meta']['code'] == 200:            # Checking response from server
            if len(user_info['data']):
                print "Username is : %s" % (user_info['data']['username'])
                print "Number of Posts : %s" % (user_info['data']['counts']['media'])
                print "Followed by : %s" % (user_info['data']['counts']['followed_by'])
                print "Follows : %s" % (user_info['data']['counts']['follows'])
            else:
                print "user  does not exist \n"
        else:
            print "Status code other than 200 received \n"
