from get_user_id import get_user_id
import requests
import urllib
from constants import BASE_URL,APP_ACCESS_TOKEN
                                                        # Importing functions and constants from other files

def get_users_post(insta_username) :            # Defination of function get_users_post()
    user_id=get_user_id(insta_username)             # Calling of function get_user_id()
    if user_id == None :                # Checking response From get_userId() function
        print "User does not exist \n"
    else:
        request_url='%susers/%s/media/recent/?access_token=%s' % (BASE_URL,user_id,APP_ACCESS_TOKEN)            # Making request URL
        print "GET request URL is %s" % (request_url)
        user_media=requests.get(request_url).json()         # Meking request to server and storing response in json format


        if user_media['meta']['code'] == 200:           # Checking respose from server
            if len(user_media['data']):             # Checking data responded form server
                choice = 1
                while True:
                    choice = raw_input(" 1) To get recent Post id \n 2) To get Max liked post ID\n 3) To get Min liked post \n"
                                       " 4) To get Max commented Post \n 5) To get Min Commented Post \n 6) To exit \n ENTER YOUR CHOICE : ")
                        # asking input from user
                    if choice.isdigit() == True:
                        choice = int(choice)
                    if choice == 1:
                        image_name = user_media['data'][0]['id'] + '.jpeg'
                        image_url = user_media['data'][0]['images']['standard_resolution']['url']
                        urllib.urlretrieve(image_url, image_name)           # Saving image to the system
                        return user_media['data'][0]['id']              # Returning post ID
                    elif choice == 2:
                        count = 1
                        post_id = user_media['data'][0]['id']
                        while len(user_media['data']) > count:
                            if user_media['data'][count - 1]['likes']['count'] < user_media['data'][count]['likes']['count']:           # Checking condition according to requirement
                                post_id = user_media['data'][count]['id']

                            count = count + 1
                        image_name = user_media['data'][0]['id'] + '.jpeg'
                        image_url = user_media['data'][0]['images']['standard_resolution']['url']
                        urllib.urlretrieve(image_url, image_name)           # Saving image to the system
                        return post_id              # Returning post ID
                    elif choice == 3:
                        count = 1
                        post_id = user_media['data'][0]['id']
                        while len(user_media['data']) > count:
                            if user_media['data'][count - 1]['likes']['count'] > user_media['data'][count]['likes']['count']:           # Checking condition according to requirement
                                post_id = user_media['data'][count]['id']

                            count = count + 1
                        image_name = user_media['data'][0]['id'] + '.jpeg'
                        image_url = user_media['data'][0]['images']['standard_resolution']['url']
                        urllib.urlretrieve(image_url, image_name)           # Saving image to the system
                        return post_id              # Returning post ID
                    elif choice == 4:
                        count = 1
                        post_id = user_media['data'][0]['id']
                        while len(user_media['data']) > count:
                            if user_media['data'][count - 1]['comment']['count'] < user_media['data'][count]['comment']['count']:           # Checking condition according to requirement
                                post_id = user_media['data'][count]['id']

                        count = count + 1
                        image_name = user_media['data'][0]['id'] + '.jpeg'
                        image_url = user_media['data'][0]['images']['standard_resolution']['url']
                        urllib.urlretrieve(image_url, image_name)               # Saving image to the system
                        return post_id              # Returning post ID
                    elif choice == 5:
                        count = 1
                        post_id = user_media['data'][0]['id']
                        while len(user_media['data']) > count:
                            if user_media['data'][count - 1]['comment']['count'] > user_media['data'][count]['comment']['count']:           # Checking condition according to requirement
                                post_id = user_media['data'][count]['id']

                            count = count + 1
                        image_name = user_media['data'][0]['id'] + '.jpeg'
                        image_url = user_media['data'][0]['images']['standard_resolution']['url']
                        urllib.urlretrieve(image_url, image_name)           # Saving image to the system
                        return post_id              # Returning post ID
                    elif choice == 6:
                        break
                    else:
                        print "\n\n[[Select From Valid Options]]"
            else:
                print "User does not exists \n"
        else:
            print "Status code other than 200 recived \n"
            return None
