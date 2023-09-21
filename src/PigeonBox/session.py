####################################################################################################################
'''
////////////////
PROGRAM session:   Handle session management and authentication of users.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu
DOCUMENTOR: Alexander Ashmore atashmore@usf.edu

////////////////
VERSION 1: written 13 March 2023 by E. Aseghehey
REVISION: revision history can be found on the project GitHub

////////////////
PURPOSE:
The purpose of this code is to handle session management and authentication of users.

The Session class loads the users from a JSON file and initializes two lists to store employees and admins.
It also provides two functions to return the lists of employees and admins respectively.

The Auth class extends the Session class to add authentication functionality.
It combines the lists of employees and admins into a single list of users and provides a function Authenticate 
to authenticate user logged in with username and password.
The Authenticate function iterates over the list of users to find a matching username and password 
and returns the user object if found.

Methods:
Each function and their description, typcial calling example, accessibility, and prototype information can be found in documentation_functionDescription.txt

////////////////
DATA STRUCTURES:
DataStructures:
- Lists: store the employees and admins data retrieved from a JSON file in the Session class, and 
         also to combine the employees and admins lists in the Auth class.
- Dictionaries: map string representations of status values to their corresponding enum values in the Status class.

Attributes:
- self.__employees__: A list attribute in the Session class that stores the employees loaded from a JSON file.
- self.__admins__: A list attribute in the Session class that stores the admins loaded from a JSON file.
- self.__users__: A list attribute in the Auth class that stores the combined list of employees and admins. 

////////////////
ALGORITHM:
None

////////////////
ERROR HANDLING:
No explicit error handling.
The calling code will raise these exceptions.

////////////////
'''
####################################################################################################################



from parsers import readJson, writeJson


class Session:
    """handles the session management and authentication of users."""

    def __init__(self) -> None:
        """ Initializes an object of the class with two private attributes containing employee and admin data from a JSON file."""
        self.__employees__, self.__admins__ = readJson.LoadUsers()

    def ReturnEmployees(self):
        """Return the list of employees."""
        return self.__employees__

    def ReturnAdmins(self):
        """Returns a list of administrator users."""
        return self.__admins__


class Auth(Session):
    """Extends the Session class to add authentication functionality."""

    def __init__(self) -> None:
        """Initializes an object of a class and creates a combined list of employees and admins as a list of users."""
        super().__init__()
        # Combines the lists of employees and admins into a single list of users
        self.__users__ = self.__employees__ + self.__admins__

    def Authenticate(self, username, password):
        """Authenticate a user with their username and password."""
        # Iterates over the list of users to find a matching username and password
        for user in self.__users__:
            if user.getUsername() == username and user.getPassword() == password:
                return user
    
