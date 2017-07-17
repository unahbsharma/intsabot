from compare_comments import compare_comments
from self_info import self_info
from get_own_post import get_own_post
from get_user_info import get_user_info
from recent_media_like import recent_media_like
from like_a_post import like_a_post
from post_a_comment import post_a_comment                           # Importing functions and constants from other files
from delete_negative_comments import delete_negative_comment
from constants import insta_username
from get_user_id import get_user_id
from comment_list import comment_list
from get_users_post import get_users_post
from sub_trends import sub_trends


def menu():
    while True:
        choice = raw_input(             # Asking for inputs from user
            " 1) To get own info  \n 2) To get own post \n 3) To get friends id \n 4) To get friends info \n 5) To Get friend post id \n 6) To Like post \n 7) To comment on post \n "
            "8) To Delete negative comments from your post\n 9) To view recent Media id like by You\n 10) To view comment of the your friends post \n 11) To find the Sub-trends of an event\n 12) To compare Pos and Neg comments of your post\n 13) To exit application\n ENTER YOUR CHOICE  :- ")
        if choice.isdigit() == True:
            choice=int(choice)
        if choice == 1:
            self_info()         # Calling of self_info() function
        elif choice == 2:
            print "Post Id : %s \n"% get_own_post()         # Calling of get_own_post() function
        elif choice == 3:
            print "User ID : %s \n" % get_user_id(insta_username)           # Calling of get_user_id() function
        elif choice == 4:
            get_user_info(insta_username)           # Calling of get_user_info function
        elif choice == 5:
            print "Post ID : %s \n"% get_users_post(insta_username)         # Calling of get_users_post() function
        elif choice == 6:
            like_a_post(insta_username)         # Calling of like_a_post() function
        elif choice == 7:
            post_a_comment(insta_username)              # Calling of post_a_comment() function
        elif choice == 8:
            delete_negative_comment()           # Calling of delete_negative_comment() function
        elif choice == 9:
            recent_media_like()             # Calling of recent_media_like() function
        elif choice == 10:
            comment_list()             # Calling of comment_list() function
        elif choice == 11:
            sub_trends()            # Calling of sub_trends() function
        elif choice == 12:
            compare_comments()              # Calling of compare_comments() function
        elif choice == 13:
            break
        else:
            print "\n\n[[Select From Valid Options]]"

menu()
