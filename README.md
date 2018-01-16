
User Creation Module
1. Create User where id is the key and user info is the detail
2. Function to return all the userid so we need to store the user object
3. iterate over user obect to check user details

Cache Module
1. Get
2. Set
3. Delete
3. Print

Operations
1. Create User
2. Delete User
3. Update the User
3. Fetch the User Information


Tasks:

Task 1:

Creating Multiple Users

User Addition in database
User Added -  Piyush
User Added -  Singhai
User Added -  Piyu
User Added -  Jain

Task 2:

Build a cache using above users so get the user

---------------------------------------
|  1  |     User(1)->Singhai          |

|  2  |     User(2)->Piyu             |

|  3  |     User(3)->Jain             |

---------------------------------------

Task 3:

Update and Delte the User, so that if the user exists in cache it should be delted or added back to cache.

User Deleted -  User(2)-Piyu

User Update -  User(1)-Pii

----------------------------------

|  3  |     User(3)->Jain        |

|  1  |     User(1)->Pii         |

----------------------------------

Task 4:

Read the All the Users from the cache and see the LRU Cache output

Reading this User ids [3, 1, 4, 0, 5]

----------------------------------

|  4  |     User(4)->Pi          |

|  0  |     User(0)->Piyush      |

|  5  |     User(5)->Pih         |

----------------------------------


