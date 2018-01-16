
# TODO
"""
User Creation Module
1. Create User where id is the key and user info is the detail
2. Function to return all the userid so we need to store the user object
3. iterate over user obect to check user details 

Cache Module
1. Get
2. Set 
3. Print

Operations
1. Create User
2. Delete User
3. Update the User
3. Fetch the User Information

"""
import collections
import itertools
from random import shuffle
class User(object):
    uid = itertools.count().next
    def __init__(self, name):
        self.userid = User.uid()
        self.user_name = name

    def __repr__(self):
        return "User(%s)->%s" %(self.userid, self.user_name)

class UserDatabase(object):
    def __init__(self):
        # User list can be dict or list
        # Just to make Cache is important I make it list
        self.users_list = []

    def create_user(self, name):
        user = User(name)
        self.users_list.append(user)
        print "User Added - ", name
        return user.userid
   
    def delete_user(self, user_id):
        success = False
        for user in self.users_list:
            if user.userid == user_id:
                self.users_list.remove(user)
                print "User Deleted - ", user
                lru.delete(user_id)
                success = True
        return success

    def update_user(self, user_id, updated_name):
        success = False
        for user in self.users_list:
            if user.userid == user_id:
                user.user_name = updated_name
                print "User Update - ", user
                lru.set(user.userid, user)
                success = True
        return success

    def get_user(self, user_id):
        user_obj = None
        for user in self.users_list:
            if user.userid == user_id:
                user_obj = user
        return user_obj

    def print_users(self):
        for user in self.users_list:
            print user

    def all_user_ids(self):
        uids = []
        for user in self.users_list:
            uids.append(user.userid)
        return uids

class LRUCache(object):
    """ This class stores the data in cache
    """
    def __init__(self, size, user_db):
        self.size = size
        self.cache = collections.OrderedDict()
        self.userdb = user_db

    def get(self, key):
        """ Check user is present in the Cache or not
            if yes then return the user from cache but remove user from current
            position to back of the OrderedDict
            if not then get the user from database and set entry in the cache
        """
        user = None
        if self.cache.has_key(key):
            # We donot need to go to Database
            user = self.cache[key]
            self.set(key, user)
        else:
            # Visiting to Database
            print "key %s Cache Miss, add the entry into the cache Cache is [%s]" %(key, self.cache)
            user = self.userdb.get_user(key) 
            self.set(uid, user)
        return user

    def set(self, key, value):
        """ LRU Algorithm
            Check the User present in the database
            if yes then pop the element from the current position
            and add it back to dict in last position
            if no then check the cache size is greater then total size then
            pop the first item from the cache and add new entry into the cache
        """
        if self.cache.has_key(key):
            self.cache.pop(key)
        else:
            if len(self.cache) >= self.size:
                self.cache.popitem(0)
        self.cache[key] = value

    def delete(self, key):
        if self.cache.has_key(key):
            self.cache.pop(key)

    def setMaxsize(self, size):
        self.size = size

    def __repr__(self):
        print "----------------------------------"
        for key, value in self.cache.iteritems():
            print "| ", key, " |    ", value, "         |" 
        print "----------------------------------"
        return  "Cache is %s"%self.cache

#TODO Below thing we can do it in command line also but it is sample
########################### Creating User Database #############
user_db = UserDatabase()
global lru
size = 3
lru = LRUCache(size, user_db)
print "User Addition in database"
u1 = user_db.create_user("Piyush")
u2 = user_db.create_user("Singhai")
u3 = user_db.create_user("Piyu")
u4 = user_db.create_user("Jain")
uids = user_db.all_user_ids()
for uid in uids:
    lru.get(uid)
print lru
u5 = user_db.create_user("Pi")
u6 = user_db.create_user("Pih")

print "Print Users"
user_db.print_users()

print "User Deletion"
user_db.delete_user(u3)
print lru

print "User Update"
user_db.update_user(u2, "Pii")
print lru


print " Shuffle the User like Query for User "
uids = user_db.all_user_ids()
shuffle(uids)
print uids
##########################################

################### Cache and User Search ########
for uid in uids:
    lru.get(uid)
##################################################
# Current cache    
print lru

