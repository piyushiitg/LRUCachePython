######################User Addition in database###########################
User Added -  Piyush
User Added -  Singhai
User Added -  Piyu
User Added -  Jain
key 0 Cache Miss, add the entry into the cache Cache is [OrderedDict()]
key 1 Cache Miss, add the entry into the cache Cache is [OrderedDict([(0, User(0)->Piyush)])]
key 2 Cache Miss, add the entry into the cache Cache is [OrderedDict([(0, User(0)->Piyush), (1, User(1)->Singhai)])]
key 3 Cache Miss, add the entry into the cache Cache is [OrderedDict([(0, User(0)->Piyush), (1, User(1)->Singhai), (2, User(2)->Piyu)])]
----------------------------------
|  1  |     User(1)->Singhai          |
|  2  |     User(2)->Piyu          |
|  3  |     User(3)->Jain          |
----------------------------------
Cache is OrderedDict([(1, User(1)->Singhai), (2, User(2)->Piyu), (3, User(3)->Jain)])
User Added -  Pi
User Added -  Pih
---------------------Print Users------------
User(0)->Piyush
User(1)->Singhai
User(2)->Piyu
User(3)->Jain
User(4)->Pi
User(5)->Pih
-------------------User Deletion----------------------------
User Deleted -  User(2)->Piyu
----------------------------------
|  1  |     User(1)->Singhai          |
|  3  |     User(3)->Jain          |
----------------------------------
Cache is OrderedDict([(1, User(1)->Singhai), (3, User(3)->Jain)])
-----------------------User Update-------------------------
User Update -  User(1)->Pii
----------------------------------
|  3  |     User(3)->Jain          |
|  1  |     User(1)->Pii          |
----------------------------------
Cache is OrderedDict([(3, User(3)->Jain), (1, User(1)->Pii)])
------------------- Shuffle the User like Query for User -----------------
[5, 0, 1, 4, 3]
key 5 Cache Miss, add the entry into the cache Cache is [OrderedDict([(3, User(3)->Jain), (1, User(1)->Pii)])]
key 0 Cache Miss, add the entry into the cache Cache is [OrderedDict([(3, User(3)->Jain), (1, User(1)->Pii), (5, User(5)->Pih)])]
key 4 Cache Miss, add the entry into the cache Cache is [OrderedDict([(5, User(5)->Pih), (0, User(0)->Piyush), (1, User(1)->Pii)])]
key 3 Cache Miss, add the entry into the cache Cache is [OrderedDict([(0, User(0)->Piyush), (1, User(1)->Pii), (4, User(4)->Pi)])]
----------------------------------
|  1  |     User(1)->Pii          |
|  4  |     User(4)->Pi          |
|  3  |     User(3)->Jain          |
----------------------------------
Cache is OrderedDict([(1, User(1)->Pii), (4, User(4)->Pi), (3, User(3)->Jain)])
