

from follow import *
from user import *
from post import *
from wall import *
from datetime import  datetime , timedelta
import time
from pymongo import MongoClient
import re


def mainpage():


    client  = MongoClient()
    db = client.mongoproject_version
    client.list_database_names()
    user = db.user
    post = db.post

    while True:
    ### id of list
    
        try:
            user_list = list(user.find())
            user_id =[]
            for i in range(len(user_list)):
                user_list[i] = user_list[i]['user_id']     ## user_id list  -> follow , unfollow 사용 예정
            print()
            print('-'*50)
            print('Please select your job')
            print('1. Sign in')
            print('2. Sign up')
            print('3 . Exit')
            print('-'*50)
            fun_num = int(input())
            ### function list
            ### 1. sign in
            ### 2. sign up
            ### 3. exit
            if fun_num == 1:   ### sign up    ### login
                ids = input('Please input your id :   ')
                password = input('Please input your password :   ')
                if ids in user_list:
                    user_s = list(user.find({'user_id':ids}))   ## get user id
                    pas = user_s[0]['password']                 ## get user password
                    if pas == password:
                        print('Your password is correct!')
                        try:
                            signin(user,ids)
                        except:
                            print('signin fail')

                        ## inner function  list
                        ## 1 . my staus
                        ## 2 . news feed
                        ## 3 . wall
                        ## 4 . post
                        ## 5 . follow
                        ## 6 . nufollow
                        ## 7 . logout
                        while True:
                            userpage(user, ids)
                            in_fun_num = int(input())

                            if in_fun_num ==1:
                                try:
                                    mystaus(user,ids)
                                except:
                                    print('mystaus fail')

                            ## newsfeed
                            if in_fun_num ==2:
                                try:
                                    newsfeed(user,post, ids)
                                except:
                                    print('newsfeed fail')
                            ## getPost
                            if in_fun_num ==3:
                                try:
                                    getPost(post, ids)
                                except:
                                    print('getPost fail')
                            ## postInterface
                            if in_fun_num ==4:
                                try:
                                    postInterface(post, ids)
                                except:
                                    print('postInterface fail')
                            if in_fun_num ==5:
                                try:
                                    follow(user, ids)
                                except:
                                    print('follow fail')
                            if in_fun_num ==6:
                                try:
                                    unfollow(user, ids)
                                except:
                                    print('unfollow fail')
                            if in_fun_num ==7:
                                break



                    else:
                        print('Your password is incorrect')
                else : 
                    print('Your id does not exist. Please join our web page')


            if fun_num == 2:   ## regist  user
                try:
                    signup(user)
                except:
                    print('signup fail')

            if fun_num == 3:
                print()
                print('Byebye!')
                break
        
        except:
            print('please rewrite')
        

            
            
 


            
       
if __name__ == '__main__':
    mainpage()
            
 


