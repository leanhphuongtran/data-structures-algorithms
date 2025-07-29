'''
Question: As a senior backend engineer at Jovian, you are tasked with developing a fast in-memory
        data structure to manage profile information (username, name and email) for 100 million users.
        It should allow the following operations to be performed efficiently:

    1.  INSERT the profile information for a new user.
    2.  FIND the profile information of a user, given their username
    3.  UPDATE the profile information of a user, given their usrname
    4.  LIST ALL the users of the platform, sorted by username

Approach:
Step 1: State the problem
    Create a data structure which can store 100 million records and perform insertion, search, update
    and list operations efficiently.
        
        Identify input and output formats:
    Input: The key input to our data structure are user profiles, which contain the username, name
            and email of a user.

Step 2: Example inputs and outputs
    List some scenarios for testing the class methods:
    1.  Insert:
        - Inserting into an empty database of users
        - Trying to insert a user with a username that already exits
        - Inserting a user with a username that does not exit
        - ???
    2. Find:
    3. Update:
    4. List all:

Step 3: Correct solution in English
    => Use sorted list
    Store the User objects in a list sorted by usernames
    1. Insert: loop through the list and add the new user at a position that keeps the list sorted.
    2. Find: loop through the list and find the user object with the username matching the query.
    3. Update: loop through the list, find the user object matching the query and update the details.
    4. List all: return the list of user objects.

Step 4: Implement the solution and test it using example inputs

Step 5:

Step 6:
'''

class User:
    # Adding a constructor method
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the 1st username greater than the new user's name
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        pass

    def update(self, user):
        pass

    def list_all(self):
        pass
    

# Creating some sample user profiles that can be used to test our functions once we implement them
seungwan = User('seungwan', 'Wendy Son', 'wendy@gmail.com')
irene = User('irene', 'Bae Joo Hyun', 'irene@gmail.com')
tiffany = User('tiffany', 'Hwang Mi Young', 'tifany@seattleu.edu')
yoona = User('yoona', 'Im Yoon A', 'yoona@yahoo.com')

users = [seungwan, irene, tiffany, yoona]

# Viewing a string representation of the object
# print(tiffany)

print('tiffany' < 'yoona')