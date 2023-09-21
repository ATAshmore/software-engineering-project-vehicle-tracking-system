####################################################################################################################
'''
////////////////
PROGRAM users:   The purpose of the classes(User,Admin,employee,Customer) is to provide a framework for 
                 managing users(Admins,employees) and customers in the system.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu
DOCUMENTOR: Alexander Ashmore atashmore@usf.edu

////////////////
VERSION 1: written 13 March 2023 by E. Aseghehey
REVISION: revision history can be found on the project GitHub

////////////////
PURPOSE:
This code defines a User class that represents a user with basic information like username, password, and date joined.
It defines two classes Admin and Employee, both inherit from the User class and define their own functionalities.
It defines a Customer class with attributes first and last name, card, email, address, and orders.

Methods:
Each function and their description, typcial calling example, accessibility, and prototype information can be found in documentation_functionDescription.txt


////////////////
DATA STRUCTURES:
DataStructures:
- Lists: Lists are used to store name information as a list of dictionaries in the to_dict() method of the Admin and Employee classes.
- Dictionaries: In the code, they are used to store information about users in the to_dict() method of the Admin and Employee classes. The Customer class also stores orders in a list of dictionaries.

Attributes:
- username: a string representing the username of the user.
- password: a string representing the password of the user.
- first_name: a string representing the first name of the user.
- last_name: a string representing the last name of the user.
- date_joined: a datetime object representing the date the user joined.
- categoryType: a string representing the type of user (Admin or Employee).
- firstName: a string representing the first name of the customer.
- lastName: a string representing the last name of the customer.
- card: a string representing the credit card information of the customer.
- email: a string representing the email address of the customer.
- address: a string representing the physical address of the customer.
- orders: a list of orders associated with the customer.

////////////////
ALGORITHM:
None

////////////////
ERROR HANDLING:
No explicit error handling.
Validation check in User for date_joined to make sure its a valid datetime object.

////////////////
'''
####################################################################################################################

from datetime import datetime

class User():
    """A class that represents a user with basic information like username, password, and date joined."""

    def __init__(self, username='', password='', first_name='', last_name='', date_joined=None) -> None:
        """Initializes a User object with a username, password, first name, last name, and date joined."""
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        # validate date. if date is not given, set it to today's date.
        if not date_joined: 
            date_joined = datetime.today()
        else:
            date_joined = datetime.strptime(date_joined, "%Y-%m-%d")
        self.date_joined = date_joined

    def getFirstName(self):
        """Returns the first name of the user."""
        return self.first_name

    def getLastName(self):
        """Returns the last name of a user."""
        return self.last_name

    def UpdatePassword(self, newpassword):
        """Updates the password of the user."""
        self.password = newpassword

    def UpdateUserName(self, newusername):
        """Updates the username attribute of a user object with a new username."""
        self.username = newusername

    def getUsername(self):
        """Returns the username of a user."""
        return self.username

    def getPassword(self):
        """Returns the password of a User instance."""
        return self.password

    def serialize(user):
        """A function to serialize a User object to a JSON-serializable format."""
        if isinstance(user, User):
            return user.to_dict()
        raise TypeError("Object of type 'User' is not JSON serializable")
    
    def __eq__(self, __o):
        """Determines whether two users are equal by comparing their usernames."""
        if isinstance(__o, User) or isinstance(__o, Admin) or isinstance(__o, Employee):
            return __o.username == self.username
        
    def __str__(self):
        """Returns a string representation of a User object."""
        return f"User {self.first_name} {self.last_name} Joined in {self.date_joined}"

    def __repr__(self) -> str:
        """Return a string representation of a User object."""
        return f"{self.first_name} {self.last_name}"






class Admin(User):
    """class inherits from the User class and defines an Admin user type.An Admin user can delete or add inventory, add or delete employees."""

    def __init__(self, username='', password='', first_name='', last_name='', date_joined=None, categoryType="Admin") -> None:
        """Initializes an instance of the Admin class, inheriting from the User class and setting the category type to "Admin"."""
        super().__init__(username, password, first_name, last_name, date_joined)
        self.categoryType = categoryType

    def getCategory(self):
        """Returns the category type of an object."""
        return self.categoryType

    def __str__(self):
        """Returns a string representation of an Admin instance."""
        return f"{self.categoryType} {self.first_name} {self.last_name}"
    
    def getDetails(self):
        """Get user details."""
        date = self.date_joined.strftime("%Y-%m-%d")
        return f"Joined in {date}"
    
    def to_dict(self):
        """Returns a dictionary with user information."""
        return {
            "username": self.username,
            "password": self.password,
            "name": [{"firstName": self.first_name, "lastName": self.last_name}],
            "dateJoined": self.date_joined.strftime("%Y-%m-%d"),
            "type": self.categoryType # default
        }




class Employee(User):
    """This class inherits from the User class and defines an Employee user type.An Employee user manages sales and can update inventory but cannot add or delete."""

    def __init__(self, username='', password='', first_name='', last_name='', date_joined=None, categoryType="Employee") -> None:
        """Initializes an Employee object with a specified username, password, first and last name, date joined, and category type."""
        super().__init__(username, password, first_name, last_name, date_joined)
        self.categoryType = categoryType

    def __str__(self):
        """Returns a string representation of the Employee object including category, first name, and last name."""
        return f"{self.categoryType} {self.first_name} {self.last_name}"
    
    def getDetails(self):
        """Returns the details of the employee's joining date in a formatted string."""
        date = self.date_joined.strftime("%Y-%m-%d")
        return f"Joined in {date}"

    def getCategory(self):
        """Returns the category type of the user."""
        return self.categoryType
    
    def to_dict(self):
        """Returns a dictionary representation of the user object."""
        return {
            "username": self.username,
            "password": self.password,
            "name": [{"firstName": self.first_name, "lastName": self.last_name}],
            "dateJoined": self.date_joined.strftime("%Y-%m-%d"),
            "type": self.categoryType # default
        }





class Customer:
    """Defines a Customer object."""

    def __init__(self, first, last, card, email, address) -> None:
        """Constructor for a Customer class with attributes such as first and last name, card, email, address and an empty list for orders."""
        self.firstName = first
        self.lastName = last
        self.card = card
        self.email = email
        self.address = address
        self.orders = []

    def getFirstName(self):
        """Returns the first name of a customer."""
        return self.firstName
    
    def getLastName(self):
        """Get the last name of a customer."""
        return self.lastName

    def getEmail(self):
        """Returns the email of a customer."""
        return self.email

    def setCard(self, new_card):
        """Sets the value of the card attribute for the instance of the class."""
        self.card = new_card

    def setAddress(self, new_address):
        """Method to set a new address for a user profile."""
        self.address = new_address

    def setEmail(self, new_email):
        """Setter function to update the email address of a user."""
        self.email = new_email

    def getDetails(self):
        """Returns a string containing the user's email, address, and list of orders."""
        return f"\nEmail: {self.email} \nAddress: {self.address}\nList of all orders: {self.orders}"

    def to_dict(self):
        """Returns the dictionary representation of the customer object."""
        return {
            "email": self.email,
            "name": [{ "first": self.firstName, "last": self.lastName }],
            "card": self.card,
            "address": self.address
        }

    def serialize(customer):
        """Function that serializes a Customer object into a JSON serializable dictionary."""
        if isinstance(customer, Customer):
            return customer.to_dict()
        raise TypeError("Object of type 'Customer' is not JSON serializable")
    
    def __str__(self) -> str:
        """This method returns a string representation of the object instance."""
        return f"{self.lastName}, {self.firstName}"

    def __repr__(self) -> str:
        """Returns a string representation of the customer object."""
        return f"{self.email}"

    def __eq__(self, value) -> bool:
        """Check if two Customer objects are equal by comparing their email addresses."""
        if isinstance(value, Customer):
            return value.email == self.email
        return False