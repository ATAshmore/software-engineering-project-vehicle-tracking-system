####################################################################################################################
'''
////////////////
PROGRAM readJson:   
imports modules and defines four functions that load data from JSON files and create objects, including Car, Employee, Admin, Order, and Customer objects.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu
DOCUMENTOR: Alexander Ashmore atashmore@usf.edu

////////////////
VERSION 1: written 13 March 2023 by E. Aseghehey
REVISION: revision history can be found on the project GitHub

////////////////
PURPOSE:
The code consists of four functions that load data from JSON files in order to create objects for a vehicle inventory, users, orders, and customers

Methods:
Each function and their description, typcial calling example, accessibility, and prototype information can be found in documentation_functionDescription.txt
    
////////////////
DATA STRUCTURES:
DataStructures:
List of Car objects: Created by the LoadInventory() function, this data structure holds Car objects based on car inventory data read from a JSON file.
Two lists of Employee and Admin objects: Created by the LoadUsers() function, these data structures hold Employee and Admin objects based on user data read from a JSON file.
List of Order objects: Created by the LoadOrders() function, this data structure holds Order objects based on order data read from a JSON file.
List of Customer objects: Created by the LoadCustomers() function, this data structure holds Customer objects based on customer data read from a JSON file.

Attributes:
vehicles: a module that contains the Car class used to create Car objects.
users: a module that contains the Employee, Admin, and Customer classes used to create User objects.
orders: a module that contains the Order class used to create Order objects.
json: a module that allows the reading of JSON files.
INVENTORY_PATH: a string that holds the path to the JSON file that contains inventory data.
USERS_PATH: a string that holds the path to the JSON file that contains user data.
ORDERS_PATH: a string that holds the path to the JSON file that contains order data.
CUSTOMER_PATH: a string that holds the path to the JSON file that contains customer data.

////////////////
ALGORITHM:
None

////////////////
ERROR HANDLING:
No explicit error handling.

////////////////
'''
####################################################################################################################



from PigeonBox import vehicles, users, orders
import json

INVENTORY_PATH = "data/inventory.json"
USERS_PATH = "data/users.json"
ORDERS_PATH = "data/orders.json"
CUSTOMER_PATH = "data/customers.json"


def LoadInventory():
    """Loads the car inventory data from a JSON file and creates a list of Car objects."""
    cars = []
    with open(INVENTORY_PATH, 'r') as jsonFile:
        carsJson = json.load(jsonFile)
        for car in carsJson:
            current_car = vehicles.Car(vin=car['vin'], info=car['info'][0], performance=car['performance'][0],
                              design=car['design'][0], handling=car['handling'], comfort=car['comfort'],
                              entertainment=car['audio'], status= car['status'], protection=car['protection'][0], package=car['package'],
                              price=car['price'])
            cars.append(current_car)
    return cars

def LoadUsers():
    """Loads user data from a JSON file and creates Employee and Admin objects accordingly."""
    employees, admins = [], []
    with open(USERS_PATH, 'r') as jsonFile:
        usersJson = json.load(jsonFile)
        for i in range(len(usersJson)):
            currentUser = usersJson[i]
            name = currentUser['name'][0]
            userType = currentUser["type"].lower()
            if userType == 'employee':
                employee = users.Employee(username=currentUser['username'], password=currentUser['password'],
                                first_name=name['firstName'], last_name=name['lastName'], 
                                date_joined=currentUser['dateJoined'])
                employees.append(employee)
            else:
                admin = users.Admin(username=currentUser['username'], password=currentUser['password'],
                                first_name=name['firstName'], last_name=name['lastName'], 
                                date_joined=currentUser['dateJoined'])
                admins.append(admin)
    return employees, admins

def LoadOrders():
    """Loads a list of orders from a JSON file."""
    orderList = []
    with open(ORDERS_PATH, 'r') as jsonFile:
        ordersJson = json.load(jsonFile)
        for i in range(len(ordersJson)):
            currentOrder = ordersJson[i]
            # order = orders.Order(id=id, car=car, buyer=buyer, employee=sellingUser, dateBought=when)
            orderList.append(currentOrder)
    return orderList



def LoadCustomers():
    """Loads and returns a list of Customer objects from a JSON file."""
    customers = []
    with open(CUSTOMER_PATH, 'r') as jsonFile:
        customersJson = json.load(jsonFile)
        for i in range(len(customersJson)):
            currentCustomer = customersJson[i]
            emailAddress = currentCustomer['email']
            name = currentCustomer['name'][0]
            firstName, lastName = name['first'], name['last']
            creditCard = currentCustomer['card']
            homeAddress = currentCustomer['address']
            # add customer
            customer = users.Customer(firstName, lastName, creditCard, emailAddress, homeAddress)
            customers.append(customer)
    return customers
