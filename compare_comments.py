from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import requests
from get_own_post import get_own_post
import matplotlib.pyplot as plt
from constants import APP_ACCESS_TOKEN,BASE_URL





def compare_comments():
            media_id = get_own_post()  # Calling of get_own_post() function
            request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (
            media_id, APP_ACCESS_TOKEN)  # Making URL for request
            print 'GET request url : %s' % (request_url)
            comment_info = requests.get(request_url).json()  # Requesting by URL and storing response in json format

            pos = 0
            neg = 0

            comment = []  # List to store comment id
            a = 0
            while len(comment_info['data']) > a:
                comment.append(comment_info['data'][a]['id'])  # Storing comments in list
                a = a + 1

            if comment_info['meta']['code'] == 200:  # Checking response from server
                if len(comment_info['data']):  # Checking for data in response
                    a = 0
                    while len(comment_info['data']) > a:
                        blob = TextBlob(comment_info['data'][a]['text'],analyzer=NaiveBayesAnalyzer())  # Analyzing the data
                        if blob.sentiment.classification == 'neg':  # Checking The responce
                            neg=neg+1
                            a=a+1
                        else:
                            pos = pos+1
                            a = a + 1
                else:
                    print 'There are no existing comments on the post!'
            else:
                print 'Status code other than 200 received!'

            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            labels = 'Positive', 'Negative'
            sizes = [pos,neg,]
            explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            plt.show()
