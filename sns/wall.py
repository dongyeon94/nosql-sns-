from datetime import  datetime , timedelta
import time

def getPost(db, user_id):
    try:
        print('your post')
        mypost = list(db.find({'$or': [{'user_id': user_id}, {'follower_comment.user_id': user_id}]},
                              {'_id': 0, 'comment': 1, 'user_id': 1, 'follower_comment': 1, 'date_time': 1}).
                      sort([('date_time', 1)]))

    except:
        print('connect fail')

    while True:
        try:
            print('[page_number/%s]' % str(int(len(mypost) / 5 + 1)))
            page_num = int(input('please input page number     (exit: 0)'))

            if page_num == 0:
                break
            print('')
            print('-' * 100)
            for i in range(5 * (page_num - 1), 5 * (page_num)):
                try:
                    print(mypost[i])
                except:
                    pass
            print('-' * 100)
            print()

        except:
            print('connect fail')
