####################################################################################################################
'''
////////////////
PROGRAM writeJson:
The purpose of the code is to write data to a JSON file based on the object type in an array, 
and it determines the file path based on the object type, and serializes the data using the object's 
serialization function before writing it to the file. 

writes on customers, inventory, orders, users json files

////////////////
PROGRAMMER: Kate Anderson katemakenzie@usf.edu
DOCUMENTOR: Alexander Ashmore atashmore@usf.edu

////////////////
VERSION 1: written 6 April 2023 by K. Anderson
REVISION: revision history can be found on the project GitHub

////////////////
PURPOSE:
The general purpose of this code is to provide a function called writeJson that writes data to a JSON file based on the type of object passed in the data parameter. 
It determines the appropriate file path and serializes the data before writing it to the file. 
This function is used to save various data types such as inventory, orders, customers, and users to their respective JSON files in the program.

Methods:
Each function and their description, typcial calling example, accessibility, and prototype information can be found in documentation_functionDescription.txt

////////////////
DATA STRUCTURES:
DataStructures:
Arrays: the input data parameter in the writeJson() function is an array.
JSON Objects: the serialized variable in the writeJson() function is a JSON object created from the data array using the json.dumps() function.

Attributes:
INVENTORY_PATH: A string representing the file path for the inventory JSON file.
ORDERS_PATH: A string representing the file path for the orders JSON file.
CUSTOMER_PATH: A string representing the file path for the customer JSON file.
USERS_PATH: A string representing the file path for the users JSON file.
INDENTATION: An integer representing the number of spaces to use for indentation in the serialized JSON output.

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
from parsers.readJson import INVENTORY_PATH, ORDERS_PATH, CUSTOMER_PATH, USERS_PATH
import json
INDENTATION = 2



def writeJson(data):
    """
    This function writes data to a json filePath, it will determine what kind of data is being loaded and write to 
    the appopriate json filePath with the proper formatting
    """
    # decide which filePath based on objct type in array
    dataType = None
    if isinstance(data[0], vehicles.Car):
        filePath = INVENTORY_PATH
        dataType = vehicles.Car
    elif isinstance(data[0], orders.Order):
        dataType = orders.Order
        filePath = ORDERS_PATH
    elif isinstance(data[0], users.Customer):
        dataType = users.Customer
        filePath = CUSTOMER_PATH
    elif isinstance(data[0], users.User):
        dataType = users.User
        filePath = USERS_PATH
    else:
        raise TypeError("Incorrect object list")

    #serialize the array and write it to the appropriate json filePath
    with open(filePath, 'w') as f:
        serialized = json.dumps(data, default=dataType.serialize, ensure_ascii=False, indent=INDENTATION)
        f.write(serialized)