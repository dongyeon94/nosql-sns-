from pymongo import MongoClient
import operator
client  = MongoClient()
db = client.mongoproject_version
client.list_database_names()
user = db.user
post = db.post



def follow(db, user11):  ## follow user
    all1 = list(db.find({},{'_id':0,'user_id':1}))
    fol1 = list(db.find_one({'user_id':user11})['following'])
    for i in range(len(all1)):
        all1[i] = all1[i]['user_id']
    aa  = []
    for i in range(len(fol1)):
        aa.append(set(list(db.find_one({'user_id':fol1[i]})['following'])))
    
    all2 = []
    li = []
    for i in range(len(aa)):
        ass = list(aa[i])
        for j in range(len(ass)):
            li.append(ass[j])
    dic ={}
    for i in range(len(all1)):
        dic[all1[i]] = 0
    for i in range(len(li)):
        dic[li[i]] += 1
    
    print('recommend : ', end="")
    so = sorted(dic.items(),key=operator.itemgetter(1))
    for i in range(1,4):
        print(so[-i][0],', ',end="")
    print()


    
    follow_user = input('whats name follower?? : ')

    user_list = list(db.find())
    user_id = []
    foll = []
    foll1 = list(db.find({'user_id':user11}))
    foll = foll1[0]['following']
    for i in range(len(user_list)):
      
        user_list[i] = user_list[i]['user_id']
        
    if follow_user in user_list and follow_user != user11 and follow_user not in foll:
        try:
            db.update({'user_id': user11}, {'$addToSet': {'following': follow_user}})
            db.update({'user_id': follow_user}, {'$addToSet': {'follower': user11}})
            print('success update follow')
        except:
            print('fail update follow')
    else:
        print('user not exist or already exist oryou insert your id')


def unfollow(db, user11):  ## unfollow user
    follow_user = input('whats name follower?? : ')

    user_list = list(db.find({'user_id': user11}))[0]['following']
    user_id = []

    if follow_user in user_list:
        s2 = input('are you sure unfollow?          [Y/N]')
        s1 = s2.upper()
        if s1 =='Y':
            try:
                db.update({'user_id': user11}, {'$pull': {'following': follow_user}})
                db.update({'user_id': follow_user}, {'$pull': {'follower': user11}})
            except:
                print('connected fail')
        else:
            print('cancel unfollow')
    else:
        print('user not exist')
