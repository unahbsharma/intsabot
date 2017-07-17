from constants import BASE_URL,APP_ACCESS_TOKEN
import requests
import urllib
                        # Importing functions and constants from other files


def get_own_post():         # Defination of function get_own_post
    request_url = ('%susers/self/media/recent/?access_token=%s') % (BASE_URL,APP_ACCESS_TOKEN)          # Making requs URL
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()            # Requesting to server and storing responce in json formet


    if own_media['meta']['code'] == 200:            # Checking response from server
        if len(own_media['data']):          # Checking data from server
            choice = 1
            while True:
                choice = raw_input(" 1) To get recent Post id \n 2) To get Max liked post ID\n 3) To get Min liked post \n"
                                       " 4) To get Max commented post \n 5) To get Min commented post\n 6) To exit \n ENTER YOUR CHOICE : ")
                                                        # Asking for input From user
                if choice.isdigit() == True:
                    choice = int(choice)
                if choice == 1:
                    image_name = own_media['data'][0]['id'] + '.jpeg'
                    image_url = own_media['data'][0]['images']['standard_resolution']['url']
                    urllib.urlretrieve(image_url, image_name)               # Saving image to the system
                    return own_media['data'][0]['id']           # Returning Post ID
                elif choice == 2:
                    count = 1
                    post_id = own_media['data'][0]['id']
                    while len(own_media['data']) > count:
                        if own_media['data'][count - 1]['likes']['count'] < own_media['data'][count]['likes']['count']:             # Checking condition according to requirement
                            post_id = own_media['data'][count]['id']

                        count = count + 1
                    image_name = own_media['data'][0]['id'] + '.jpeg'
                    image_url = own_media['data'][0]['images']['standard_resolution']['url']
                    urllib.urlretrieve(image_url, image_name)           # Saving image to the system
                    return post_id              # Returning Post ID
                elif choice == 3:
                    count = 1
                    post_id = own_media['data'][0]['id']
                    while len(own_media['data']) > count:
                        if own_media['data'][count - 1]['likes']['count'] > own_media['data'][count]['likes']['count']:             # Checking condition according to requirement
                            post_id = own_media['data'][count]['id']

                        count = count + 1
                    image_name = own_media['data'][0]['id'] + '.jpeg'
                    image_url = own_media['data'][0]['images']['standard_resolution']['url']
                    urllib.urlretrieve(image_url, image_name)           # Saving image to the system
                    return post_id              # Returning Post ID
                elif choice == 4:
                    count = 1
                    post_id = own_media['data'][0]['id']
                    while len(own_media['data']) > count:
                        if own_media['data'][count - 1]['comments']['count'] > own_media['data'][count]['comments']['count']:  # Checking condition according to requirement
                            post_id = own_media['data'][count]['id']

                        count = count + 1
                    image_name = own_media['data'][0]['id'] + '.jpeg'
                    image_url = own_media['data'][0]['images']['standard_resolution']['url']
                    urllib.urlretrieve(image_url, image_name)  # Saving image to the system
                    return post_id
                elif choice == 5:
                    count = 1
                    post_id = own_media['data'][0]['id']
                    while len(own_media['data']) > count:
                        if own_media['data'][count - 1]['comments']['count'] > own_media['data'][count]['comments']['count']:             # Checking condition according to requirement
                            post_id = own_media['data'][count]['id']

                        count = count + 1
                    image_name = own_media['data'][0]['id'] + '.jpeg'
                    image_url = own_media['data'][0]['images']['standard_resolution']['url']
                    urllib.urlretrieve(image_url, image_name)           # Saving image to the system
                    return post_id              # Returning Post ID
                elif choice == 6:
                    break
                else:
                    print "\n\n[[Select From Valid Options]]"
        else:
            print "User does not exists \n"
    else:
        print "Status code other than 200 recived \n"
        return None
