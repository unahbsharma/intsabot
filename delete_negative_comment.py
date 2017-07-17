from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import requests
from get_own_post import get_own_post
from get_users_post import get_users_post
from constants import APP_ACCESS_TOKEN,BASE_URL
            # Importing functions and constants from other files



def delete_negative_comment():          # Defination of delete_negative_comment() function
  media_id = get_own_post()             # Calling of get_own_post() function
  request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)            # Making URL for request
  print 'GET request url : %s' % (request_url)
  comment_info = requests.get(request_url).json()           # Requesting by URL and storing response in json format

  comment=[]        # List to store comment id
  a=0
  while len(comment_info['data']) > a :
    comment.append(comment_info['data'][a]['id'])           # Storing comments in list
    a = a + 1


  if comment_info['meta']['code'] == 200:           # Checking response from server
    if len(comment_info['data']):               # Checking for data in response
        a = 0
        while len(comment_info['data']) > a :
           blob = TextBlob(comment_info['data'][a]['text'], analyzer=NaiveBayesAnalyzer())          # Analyzing the data
           if blob.sentiment.classification == 'neg':           # Checking The responce
              request_url='%smedia/%s/comments/%s?access_token=%s' % (BASE_URL,media_id,comment[a],APP_ACCESS_TOKEN)            # Making URL to request
              print "DEL request url : %s" % (request_url)
              del_comment=requests.delete(request_url).json()               # Requesting To server
              if del_comment['meta']['code'] == 200 :           # Cheking response fromm server
                  print "Comment with id %s : %s is deleted" % (comment[a],comment_info['data'][a]['text'])
                  a = a+1
              else:
                print 'There is a problem \n'
           else:
            print "Comment with id %s : %s is a good comment  " % (comment[a],comment_info['data'][a]['text'])
            a = a+1
    else:
      print 'There are no existing comments on the post!'
  else:
    print 'Status code other than 200 received!'
