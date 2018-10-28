from datetime import  datetime , timedelta
import time
import re

def insertPost(db, user_id):
    
    comment=input('please write down your comment')
    ##hash_tag = input('please write down your hash tag')
    ###hash_tag_fin = hash_tag.split(' ')
    hash_tag_fin = re.findall(r'#\w+',comment)
    try:
        db.insert({'user_id':user_id,'comment':comment,'Hash_tag':hash_tag_fin,'follower_comment':[],'date_time':datetime.today()})
        print('success - insert post')
    except:
        print('fail - insert')
    

def deletePost(db, user_id):
    function = int(input('please select your function : 1.post  2.review  3.out'))

    ##post
    if function == 1:
        try:
            ## list reset
            user_list = list(db.find({'user_id': user_id}))
            comment = []
            time_list = []
            for i in range(len(user_list)):
                comment.append(user_list[i]['comment'])
                time_list.append(user_list[i]['date_time'])
                print('posting_number) ', i, '    posting content : ', user_list[i]['comment'])

            numbers = int(input('please select number '))
            check = input('are you sure?   : [y/n]')
            check = check.upper()
            if check == 'Y':
                try:
                    db.delete_one({'date_time': time_list[numbers]})
                    print('delete success')
                except:
                    print('fail delete')
            else:
                print('cancel delete')

        except:
            print('connect fail please retry')

    ## review
    if function == 2:
        try:
            ## if user id is user_id
            user_list = list(db.find({'follower_comment.user_id': user_id}))
            post_time = []
            user_time = []
            num = 0
            for i in range(len(user_list)):
                post_time.append(user_list[i]['date_time'])
                for j in range(len(user_list[i]['follower_comment'])):
                    ids = user_list[i]['follower_comment'][j]['user_id']
                    if ids == user_id:
                        user_time.append(user_list[i]['follower_comment'][j]['date_time'])
                        print(num, 'user_post_id : ', user_list[i]['user_id'], 'user_post_comment :  ',
                              user_list[i]['comment'],
                              '   your_id : ', ids, '   your comment  : ',
                              user_list[i]['follower_comment'][j]['comment'])

                        num += 1

            numbers = int(input('please select button'))
            check = input('are you sure?   : [y/n]')
            check = check.upper()
            if check == 'Y':
                try:
                    db.update({'date_time': post_time[numbers]},
                              {'$pull': {'follower_comment': {'date_time': user_time[numbers]}}})
                    print('delete success')
                except:
                    print('fail delete review')
            else:
                print('ok')

        except:
            print('fail connect')

    ## exit
    if function == 3:
        print('byebye')


def newsfeed(db1, db2, user_ids):
    following = list(db1.find({'user_id': user_ids}, {'_id': 0, 'following': 1}))
    following_list = following[0]['following']
    news = list(
        db2.find({'$or': [{'user_id': user_ids}, {'user_id': {'$in': following_list}}]}, {'_id': 0, 'date_time': 0}))

    while True:
        print('[page_number/%s]' % str(int(len(news) / 5 + 1)))
        pagenum = int(input('please intput page number     (exit : 0)'))

        if pagenum == 0:
            break

        print()
        print('-' * 100)

        for i in range(5 * (pagenum - 1), 5 * (pagenum)):
            try:
                print(news[i])
            except:
                pass
        print('-' * 100)
        print()


def postInterface(db, user_id):
    while True:
        try:

            newsfeed = list(db.find({'user_id': user_id}, {'_id': 0, 'user_id': 1, 'comment': 1, 'date_time': 1}))
            timedate = []
            for i in range(len(newsfeed)):
                print(i, 'your id :', newsfeed[i]['user_id'], 'your posting :', newsfeed[i]['comment'])
                timedate.append(newsfeed[i]['date_time'])
            print()
            print('-' * 100)
            print('1.show detail   2.insert newsfeed   3.search hash tag    4.delete   5.comment other post   6.exit ')
            
            
            
            functions = int(input('please write down your function  : '))

        except:
            print('connect fail 1')

        ## show detail
        if functions == 1:
            try:
                numbers = int(input('please select number'))
                detail = list(db.find({'date_time': timedate[numbers]}))
                print('-' * 100)
                print('your id : ', detail[0]['user_id'])
                print('your comment : ', detail[0]['comment'])
                for i in range(len(detail[0]['follower_comment'])):
                    print(detail[0]['follower_comment'][i])

                print('your hash tag : ', detail[0]['Hash_tag'])
                print('-' * 100)

                ##time.sleep(1)

            except:
                print('connect fail 2')

        ## insert newsfeed
        if functions == 2:
            try:
                insertPost(db, user_id)
            except:
                print('fail insert')
          

        ## search newsfeed
        if functions == 3:
            hash_tag = input('please write down your hash tag')
            hash_tag_fin = hash_tag.split(' ')
            hash_list = list(db.find({'Hash_tag':{'$in':hash_tag_fin}},{'_id':0,'date_time':0}))
            print()
            print('-'*50)
            for i in range(len(hash_list)):
                print('user_id : ',hash_list[i]['user_id'], 'comment : ',hash_list[i]['comment'] ,'hash_tag : ', hash_list[i]['Hash_tag'])
            print()
            print('-'*50)
        ## delete
        if functions == 4:
            try:
                deletePost(db, user_id)
                ##time.sleep(1)
            except:
                print('connect fail 4')
        ## commnet other post
        if functions == 5:
            try:

                other_id_list = list(
                    db.find({'user_id': {'$ne': user_id}}, {'_id': 0, 'user_id': 1, 'comment': 1, 'date_time': 1}).sort(
                        [('date_time', 1)]))
                other_id_fin = []
                other_time = []
                for i in range(len(other_id_list)):
                    other_id_fin.append(other_id_list[i]['user_id'])
                    other_time.append(other_id_list[i]['date_time'])
                    print(i, 'other user_id :', other_id_list[i]['user_id'], '   other user posting : ',other_id_list[i]['comment'])
                ## others id
                other_id = input('please input other user_id :')
                if other_id in other_id_fin:
                    try:
                        number = int(input('select number : '))
                        coment = input('insert your comment : ')

                        db.update({'user_id': other_id, 'date_time': other_time[number]}, {'$push': {'follower_comment':{'user_id':user_id, 'comment': coment,'date_time':datetime.today()}}})
                        print('update complete')
                    except:
                        print('fail update')
                else:
                    print('id does not exist')
                ##time.sleep(1)
            except:
                print('connect fail 5')
        ## exit
        if functions == 6:
            break


