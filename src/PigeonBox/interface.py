####################################################################################################################
'''
////////////////
PROGRAM interface:   contains classes and functions to manage the car dealership's interface,
                     allowing employees and admins to view, manage, and 
                     update car inventory, customers, orders, and user accounts.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu
DOCUMENTOR: Alexander Ashmore atashmore@usf.edu

////////////////
VERSION 1: written 13 March 2023 by E. Aseghehey
REVISION: revision history can be found on the project GitHub

////////////////
PURPOSE:
- InterfaceObjects is a base class that manages the interface objects and mapping functions.

- Interface is a subclass of InterfaceObjects and contains all the methods for managing the 
  system's car, customer, users, and orders. 

Methods:
Each function and their description, typcial calling example, accessibility, and prototype information can be found in documentation_functionDescription.txt

////////////////
DATA STRUCTURES:
DataStructures:
- Lists: uses lists to store data such as inventory, orders, customers, employees, and admins.
- Dictionaries: uses dictionaries to store orders, with the order ID as the key 
                and the order details as the value.
- Tuples: uses tuples to store information such as the make, model, and year of a car.

Attributes:
No explicit attributes
- self.inventory: a list of vehicle objects representing the current inventory.
- self.customers: a list of customer objects representing the current customers.
- self.employees: a list of employee objects representing the current employees.
- self.admins: a list of admin objects representing the current admins.
- self.__users__: a list of all users (i.e., employees and admins), used as a helper.
- self.ordersDict: a dictionary representing the current orders (loaded from JSON).
- self.orders: a list of order objects representing the current orders.
- self.isObjListUpdated: a list of boolean values indicating whether a certain object list 
                         has been updated (e.g., the inventory, orders, etc.).
                         The list is indexed as follows: 0 = inventory, 1 = orders, 2 = users, 3 = customers.

////////////////
ALGORITHM:
algorithms used are simple. focused more on implementing logic for the system.
- Linear Search Algorithm: usernameToUser, vinToCar, emailToCustomer, searchInventory.
- Conditional Statemetns: ViewByStatus, inInventory, UserExists, UsernameExists, vinExists.
- Iteration: ViewAvailableInventory, getCustomerList, getEmployeeList, ViewUsers.

////////////////
ERROR HANDLING:
No explicit error handling.

////////////////
'''
####################################################################################################################

from parsers import *
from PigeonBox import session, status, orders, users, vehicles


class InterfaceObjects():
    """A class for managing the interface objects and mapping functions."""

    def __init__(self) -> None:
        """ Initializes an instance of a class with inventory, customers, employees, admins, and users."""
        self.inventory = readJson.LoadInventory()
        self.customers = readJson.LoadCustomers()
        self.employees = session.Session().ReturnEmployees()
        self.admins = session.Session().ReturnAdmins()
        self.__users__ = self.employees + self.admins # helper


    '''mapper functions'''
    def usernameToUser(self, username):
        """Converts a given username to a corresponding user object if it exists in the system."""
        for user in self.__users__:
            if user.getUsername() == username:
                return user
    
    def vinToCar(self, vin):
        """This function returns a Car object based on its Vehicle Identification Number (VIN)."""
        for car in self.inventory:
            if car.getVin() == vin:
                return car
    
    def emailToCustomer(self, emailAddress):
        """Get customer object by email address."""
        for customer in self.customers:
            if customer.getEmail() == emailAddress:
                return customer
    
    def getCustomerList(self):
        """Returns the list of all customers."""
        return self.customers
    
    def getEmployeeList(self):
        """Returns a list of all employees."""
        return self.employees

    def isEmployee(self, user):
        """Checks whether the given user is an employee or not."""
        return user in self.employees

    def ViewUsers(self):
        """Returns the list of all users in the system."""
        return self.__users__
    
    def vinExists(self, vin):
        """Check if a VIN (Vehicle Identification Number) exists in the inventory."""
        for car in self.inventory:
            if car.getVin() == vin:
                return True
        return False
    
    def inInventory(self, car):
        """Check if a car is in the inventory."""
        if isinstance(car, str):
            return self.vinExists(car)

        for vehicle in self.inventory:
            if vehicle == car:
                return True
        return False 
    
    def ViewByStatus(self, statusToViewBy):
        """Returns a list of vehicles filtered by their status."""
        statusToViewBy = statusToViewBy.lower()

        if (statusToViewBy == 'available'):
            return self.ViewAvailableInventory()

        viewStatus = status.strToStatus(statusToViewBy)
        filteredByStatus = []
        for car in self.inventory:
            if car.getStatus() == viewStatus:
                filteredByStatus.append(car)

        return filteredByStatus
    
    def GetInventory(self):
        """Get the inventory of the car dealership."""
        return self.inventory
    
    def searchInventory(self, model, make, year):
        """ Search inventory by car model, make, and year and return car object if found."""
        for car in self.inventory:
            info = car.getCarInfo()
            if model == info['model'] and make == info['make'] and year == info['year']:
                return car
    
    def ViewAvailableInventory(self):
        """Returns a list of available vehicles in the inventory."""
        available = []
        for vehicle in self.inventory:
            if vehicle.getStatus() == status.Status.AVAILABLE:
                available.append(vehicle)
        return available
    
    def UserExists(self, checkUser):
        """ Checks if a user exists in the list of users..Useful for when we want to add or remove an employee"""
        if (isinstance(checkUser, str)):
            return self.UsernameExists(checkUser)
        
        for user in self.__users__:
            if user == checkUser:
                return True
        return False
    
    def UsernameExists(self, username):
        """Checks if a username already exists in the list of users."""
        for user in self.__users__:
            if user.getUsername() == username:
                return True
        return False



class Interface(InterfaceObjects):
    """Interface is the class that contains all the methods for managing the system's car, customer, users, and orders."""

    def __init__(self) -> None:
        """Initializes an object of the class and loads orders from a JSON file."""
        super().__init__()
        #   loads orders from json
        self.ordersDict = readJson.LoadOrders() # have to pass customers and car functionality to correctly add to buyers list and such
        self.orders = []
        for order in self.ordersDict:
            self.orders.append(orders.Order(id=order['id'], 
                                            car=self.vinToCar(order['carVin']), 
                                            buyer=self.emailToCustomer(order['buyer']), 
                                            employee=self.usernameToUser(order['soldBy']), 
                                            dateBought=order['dateBought']))
        # 0: inv, 1: order, 2: users, 3: customer
        self.isObjListUpdated = [False] * 4
        # loading customer orders if there's any
        for order in self.orders:
            currentCustomer = order.getUser()
            for customer in self.customers:
                if customer == currentCustomer:
                    customer.orders.append(order)

    def changeCarStatus(self, car, status):
        """Change the status of a car and mark the inventory list as updated."""
        car.SetStatus(status)
        self.isObjListUpdated[0] = True

    def changeCarPrice(self, car, newPrice):
        """Update the price of a car and set a flag for the inventory list as updated."""
        car.UpdatePrice(newPrice)
        self.isObjListUpdated[0] = True
    
    def changeCarMileage(self, car, newMileage):
        """ Update mileage of a car object and set isObjListUpdated flag to True."""
        car.UpdateMileage(newMileage)
        self.isObjListUpdated[0] = True

    def changeCustomerEmail(self, customer, newEmail):
        """Update the email of a given customer object."""
        customer.setEmail(newEmail)
        self.isObjListUpdated[3] = True

    def changeCustomerCard(self, customer, newCard):
        """Change a customer's credit card information"""
        customer.setCard(newCard)
        self.isObjListUpdated[3] = True
    
    def changeCustomerAddress(self, customer, newAddress):
        """Updates the address of a customer and sets a flag to indicate that the customer list has been updated."""
        customer.setAddress(newAddress)
        self.isObjListUpdated[3] = True

    def changeUserPassword(self, user, newPassword):
        """Changes the password of an admin or employee user."""
        for admin in self.admins:
            if admin == user:
                admin.UpdatePassword(newPassword)
                self.isObjListUpdated[2] = True
                return
        
        for employee in self.employees:
            if employee == user:
                employee.UpdatePassword(newPassword)
                self.isObjListUpdated[2] = True
                return
            
    def changeUserUsername(self, user, newUsername):
        """A function to change the username of an admin or an employee in a car dealership system."""
        for admin in self.admins:
            if admin == user:
                admin.UpdateUserName(newUsername)
                self.isObjListUpdated[2] = True
                return
        
        for employee in self.employees:
            if employee == user:
                employee.UpdateUserName(newUsername)
                self.isObjListUpdated[2] = True
                return
    
    def viewOrders(self):
        """Returns the list of orders."""
        return self.orders
    
    def getOrderslist(self):
        """Returns the list of orders."""
        return self.orders
    



    def isCarOrdered(self, car) -> bool:
        """Check if a car has been ordered by a customer."""
        for order in self.orders:
            if order.getCar() == car:
                return True
        return False
    
    def doesOrderExist(self, checkOrder) -> bool:
        """Checks if a car has been ordered."""
        for order in self.orders:
            if order == checkOrder:
                return True
        return False
    
    def MakeOrder(self, customer, vehicle, seller):
        """Creates an order object for a given customer, vehicle, and seller and adds it to the order list."""
        # check that a vehicle is available before making an order
        if not vehicle.isAvailable(): return
        id = self.orders[-1].getId() + 1 if self.orders else 1
        order = orders.Order(id, vehicle, customer, employee=seller) # create order object
        # add order to order list and deal with the customer dependency
        self.orders.append(order)
        customer.orders.append(order)
        self.isObjListUpdated[1] = True # to write to json -- orders have been updated
        return order
    
    def UndoOrder(self, order):
        """Remove an order from the orders list and update the car status."""
        # also removes order from the users.orders list
        if not self.doesOrderExist(order): 
            return
        
        self.orders.remove(order)
        order.RemoveOrder()
        del order # delete order object and free up memory

        self.isObjListUpdated[1] = True

    def emailExists(self, email):
        """Checks if an email exists in the customer list."""
        for customer in self.customers:
            if customer.getEmail() == email:
                return True
        return False

    def isCustomer(self, newCustomer):
        """Check if a given customer exists in the list of customers."""
        if isinstance(newCustomer, str):
            return self.emailExists(newCustomer)

        for customer in self.customers:
            if customer == newCustomer:
                return True
        return False
    
    def AddCustomer(self, first, last, card, email, address):
        """Adds a new customer to the list of customers."""
        if self.isCustomer(email):
            return
        newCustomer = users.Customer(first, last, card, email, address)
        self.customers.append(newCustomer)
        self.isObjListUpdated[3] = True
        return newCustomer

    def RemoveCustomer(self, customer):
        """Removes a given customer and their orders from the system, and sets any ordered car that has not been delivered to backorder status.
            delete from orders if they exist AND set car to available if customer has been deleted """
        # grab customer orders
        customerOrders = []
        for order in self.orders:
            if order.getUser() == customer:
                customerOrders.append(order)
                if order.getCar().getStatus() != status.Status.ORDERED: # if car has not been delivered yet
                    order.getCar().setStatus(status.Status.BACKORDER)
        # delete orders for customers:
        while customerOrders:
            order = customerOrders.pop()
            self.UndoOrder(order)
        # delete customer
        self.customers.remove(customer)
        del customer
        self.isObjListUpdated[3] = True

    def LogOut(self):
        """Saves changes to JSON files and logs the user out of the system."""
        if self.isObjListUpdated[0]:
            writeJson.writeJson(self.inventory)
        if self.isObjListUpdated[1]:
            writeJson.writeJson(self.orders)
        if self.isObjListUpdated[2]:
            allUsers = self.admins + self.employees
            writeJson.writeJson(allUsers)
        if self.isObjListUpdated[3]:
            writeJson.writeJson(self.customers)




class AdminInterface(Interface):
    """ Admin can do everything an employee can do and MORE, hence why it has its own class, which inherits all the methods from Interface
        but an admin can add and remove employees, and add and remove cars from inventory """

    def AddAdmin(self, username, passwd, fname, lname, dateJoined=None):
        """Add a new admin user to the system."""
        if self.UserExists(username):
            return False
        newAdmin = users.Admin(username, passwd, fname, lname, date_joined=dateJoined)
        self.admins.append(newAdmin)
        self.isObjListUpdated[2] = True
        return True

    def AddEmployee(self, username, passwd, fname, lname, dateJoined=None) -> None:
        """Adds a new employee user to the system."""
        if self.UserExists(username):
            return False
        
        newEmployee = users.Employee(username, passwd, fname, lname, date_joined=dateJoined)
        self.employees.append(newEmployee)
        self.isObjListUpdated[2] = True
        return True

    def ordersMadeByUser(self, user):
        """Returns a list of orders made by a given user."""
        orders = []
        for order in self.orders:
            if order.getSeller() == user:
                orders.append(order)
        return orders

    def RemoveUser(self, userToRemove) -> bool:
        """Removes a user from the system and all orders made by that user."""
        if not self.UserExists(userToRemove):
            return False

        # remove all orders made by that user
        userOrders = self.ordersMadeByUser(userToRemove)
        if userOrders:
            for order in userOrders:
                self.UndoOrder(order)

        if (isinstance(userToRemove, users.Admin)):
            self.admins.remove(userToRemove)
        else:
            self.employees.remove(userToRemove)

        self.__users__.remove(userToRemove)
        self.isObjListUpdated[2] = True
        return True

    def AddInventory(self, vin, info, performance, design, handling, comfort, entertainment, protection, package, price, status=None) -> bool:
        """  Add a new car to the inventory if it doesn't already exist."""
        if self.inInventory(vin): 
            return False 
        
        newCar = vehicles.Car(vin=vin, info=info, performance=performance, design=design, handling=handling, comfort=comfort, entertainment=entertainment, protection=protection, package=package, price=price, status=status)
        self.inventory.append(newCar) 
        self.isObjListUpdated[0] = True 
        return True 
    
    def RemoveInventory(self, car) -> bool:
        """ checks if car exists, if it does, checks the status of the car, if it is ordered then it also removes the order
        then proceeds by removing the car entirely from the system"""
        if not self.inInventory(car): return False
        if car.getStatus() == status.Status.ORDERED:
            currentOrder = None
            for order in self.orders:
                if order.getCar() == car: 
                    currentOrder = order 
                    break
            if currentOrder: self.UndoOrder(currentOrder)
        self.inventory.remove(car)
        self.isObjListUpdated[0] = True
        return True
