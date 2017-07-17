# to get info of our self
import requests
from constants import BASE_URL,APP_ACCESS_TOKEN
                                                    # Importing functions and constants from other files

def self_info():                # Defination of self_info() function
    request_url="%susers/self/?access_token=%s"% (BASE_URL,APP_ACCESS_TOKEN)            # MAking request URL
    print "request url is %s" % (request_url)
    user_info = requests.get(request_url).json()                 # Requesting from serever and storing response in json format

    if user_info['meta']['code'] == 200 :               # Checking response from server
        if len(user_info['data']):
            print "Username : %s" % (user_info['data']['username'])
            print "Number of posts : %s" % (user_info['data']['counts']['media'])
            print "Followed by : %s " % (user_info['data']['counts']['followed_by'])
            print "Follows : %s \n" % (user_info['data']['counts']['follows'])
        else:
            print("User does not exist \n")
    else:
        print "Status code other than 200 received \n"
