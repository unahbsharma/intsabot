from constants import APP_ACCESS_TOKEN,BASE_URL
import requests
                    # Importing functions and constants from other files


def recent_media_like():
    request_url='%susers/self/media/liked?access_token=%s' % (BASE_URL,APP_ACCESS_TOKEN)            # Making Request URL
    print "request url is %s" % (request_url)
    media_like = requests.get(request_url).json()           # Requesting from serever and storing response in json format
    print media_like['data'][0]['id']

    media_id = []  # List to store comment id
    a = 0
    while len(media_like['data']) > a:
        media_id.append(media_like['data'][a]['id'])
        a = a + 1
    print "Media ID Are "
    for temp in media_id:
        counter = 1
        print str(counter) + ") " + str(temp)
        counter = counter + 1
    print '\n'
