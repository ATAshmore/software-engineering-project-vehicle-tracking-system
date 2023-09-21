####################################################################################################################
'''
////////////////
PROGRAM orders:   
The code defines a class called "Order" representing an order made by a buyer for a car,
containing information such as the buyer, car, salesperson, date of purchase, and order ID,
with various methods to manipulate and retrieve information about the order.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu
DOCUMENTOR: Alexander Ashmore atashmore@usf.edu

////////////////
VERSION 1: written 13 March 2023 by E. Aseghehey
REVISION: revision history can be found on the project GitHub

////////////////
PURPOSE:
The purpose of the code is to implement a class Order that represents an order made by a buyer for a car,
containing information such as the buyer, car, salesperson, date of purchase, and order ID.
The class provides several methods to get the details of the order,
such as the buyer, car, salesperson, date of purchase, and order ID.

Methods:
Each function and their description, typcial calling example, accessibility, and prototype information can be found in documentation_functionDescription.txt

////////////////
DATA STRUCTURES:
DataStructures:
- self.id: An integer variable used to store the unique ID of an order.
- self.car: An object variable of the Car class, used to store the details of the car ordered in the order.
- self.buyer: An object variable of the User class, used to store the details of the buyer who placed the order.
- self.salesBy: An object variable of the Employee class, used to store the details of the salesperson who made the sale.
- self.when: A datetime variable, used to store the date and time of the order.

Attributes:
- id: a unique identifier for the order.
- car: an object of the Car class representing the car ordered by the buyer.
- buyer: an object of the User class representing the buyer who placed the order.
- when: a datetime object representing the date and time when the order was made.
- salesBy: an object of the Employee class representing the salesperson who sold the car.

////////////////
ALGORITHM:
None

////////////////
ERROR HANDLING:
No explicit error handling.

////////////////
'''
####################################################################################################################



from datetime import datetime
from PigeonBox.bcolors import bcolors


class Order():
    """ Class represents orders made, works like a database one-to-one relationship with a buyer and a car"""

    def __init__(self, id, car=None, buyer=None, dateBought=None, employee=None) -> None:
        """Initializes an object of the Sale class with specified attributes including car, buyer, sales employee, and date of sale."""

        self.id = id 
        #  set car status to ordered
        if car:  car.SetStatus('ordered')
        self.car = car        
        self.buyer = buyer #the user id
        self.salesBy = employee

        # if a date is not specified, it will be set to today's date
        if not dateBought: dateBought = datetime.today()
        else: dateBought = datetime.strptime(dateBought, "%Y-%m-%d")
        self.when = dateBought

    def getUser(self):
        """Returns the ID of the user who bought the car."""
        return self.buyer

    def getCar(self):
        """Returns the car associated with the order object."""
        return self.car
    
    def getSeller(self):
        """Returns the employee who sold the car in the order."""
        return self.salesBy
    
    def getDate(self):
        """Returns the date when the car was bought."""
        return self.when
    
    def getId(self):
        """Returns the ID of a car order."""
        return self.id

    def getDateJoined(self):
        """Returns the date the user joined in the format "YYYY-MM-DD"."""
        return self.when.strftime("%Y-%m-%d")
    
    def to_dict(self):
        """Convert the Order object to a dictionary format."""
        return {
            "id": self.id,
            "carVin": self.car.getVin(),
            "buyer": self.buyer.getEmail(),
            "soldBy": self.salesBy.getUsername(),
            "dateBought": self.when.strftime("%Y-%m-%d")
        }
    
    def serialize(order):
        """Serializes an Order object to a JSON-compatible format."""
        if isinstance(order, Order):
            return order.to_dict()
        raise TypeError("Object of type 'Order' is not JSON serializable")

    def RemoveOrder(self):
        """Removes an order and sets the car status to available."""
        self.buyer.orders.remove(self)
        self.car.SetStatus("available")
    
    def orderDetails(self):
        """Generates a string containing the details of the order."""
        toret = f"\nCar:\n{self.car.getDetails()}\n\nSales by: {self.salesBy}\n\nCustomer {self.buyer.getDetails()}\n"
        return toret

    def __str__(self):
        """Returns a string representation of the order object."""
        salesBy = self.salesBy.__str__()
        salesBy = " ".join(salesBy.split(" ")[:3])
        return f"Order #{self.id} {bcolors.BOLD}Made by {salesBy}{bcolors.ENDC}: {self.car.getCarInfo()['make']} {self.car.getCarInfo()['model']} for {bcolors.BOLD}{self.buyer.getLastName()}, {self.buyer.getFirstName()}{bcolors.ENDC}"
    
    def __eq__(self, value) -> bool:
        """Check equality of two Order objects."""
        if isinstance(value, Order):
            return value.id == self.id
        return False

    def __repr__(self) -> str:
        """Returns the string representation of the car object."""
        return f"{self.car}"
