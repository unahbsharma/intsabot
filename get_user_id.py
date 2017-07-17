# to get id of user
from constants import BASE_URL,APP_ACCESS_TOKEN,insta_username
import requests


                    # Importing functions and constants from other files




def get_user_id(insta_username) :           # Defination of funnction get_user_id()
    insta_username = raw_input("Enter Name of your friend \n")              # Taking friends username as input
    if len(insta_username) == 0:
        get_user_id(insta_username)

    request_url="%susers/search?q=%s&access_token=%s" % (BASE_URL,insta_username,APP_ACCESS_TOKEN)              # Making URL for request
    print "request url is %s" % (request_url)
    user_info=requests.get(request_url).json()          # Requesting to server and storing response in json format

    if user_info['meta']['code'] == 200 :           # Checking response from server
        if  len(user_info['data']):         # Checking data respond from server
            return user_info['data'][0]['id']           # Returning User ID
        else:
            print "User does not exist \n"

    else:
        print("Return code is other than 200 recived \n")
        exit()
