def signup(db):  ### registering
    try:
        new = input('Are you joining our webpage?  : [Y/N]')  ## request signin
        new = new.upper()
        if new == 'Y':
            ids = input('Please input your id :   ')
            user_list, user_id = list(db.find()), []
            for i in range(len(user_list)):  ### check already user
                user_list[i] = user_list[i]['user_id']

            if ids not in user_list:
                password = input('Please input your password :   ')
                password2 = input('Please confirm your password :   ')
                profile = input('Please input your profile :  ')
                if password == password2:
                    try:
                        db.insert(
                            {'user_id': ids, 'password': password, 'profile': profile, 'follower': [], 'following': []})
                        print('Your data is successfully stored')
                    except:
                        print('connect fail')
                else:
                    print('Incorrect password')
            else:
                print('Your id already exists')
        else:
            print('Bye! See you next time.')
    except:
        print('Mongo server error has occurred')


def signin(db, user11):  ##login
    try:
        ss = list(db.find({'user_id': user11}))
        u_id = ss[0]['user_id']
        u_pro = ss[0]['profile']
        u_folow = ss[0]['follower']
        u_folowing = ss[0]['following']
        print('Welcome', user11)
    except:
        print('Mongo server error has occurred')


def mystaus(db, user11):  ## user staus
    try:
        print('Your id is : ', list(db.find({'user_id': user11}, {'_id': 0, 'user_id': 1}))[0]['user_id'])
        print('Your proflie is : ', list(db.find({'user_id': user11}, {'_id': 0, 'profile': 1}))[0]['profile'])
        print('Your following : ', len(list(db.find({'user_id': user11}, {'_id': 0, 'following': 1}))[0]['following']))
        print('Your follower : ', len(list(db.find({'user_id': user11}, {'_id': 0, 'follower': 1}))[0]['follower']))
    except:
        print('Mongo server error has occurred')


def userpage(db, user11):  ## user page
    try:
        print()
        print('-' * 50)
        print('Please select your work')
        print('1 . My staus ')
        print('2 . News feed')
        print('3 . Wall')
        print('4 . Post')
        print('5 . Follow')
        print('6 . Unfollow')
        print('7 . Logout')
        print('-' * 50)
    except:
        print('connect fail')


