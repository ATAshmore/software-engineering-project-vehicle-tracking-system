####################################################################################################################
'''
////////////////
PROGRAM vehicles:  define a class called Car with various attributes and methods to 
                   represent a vehicle in the PigeonBox system and manipulate its properties.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu
DOCUMENTOR: Alexander Ashmore atashmore@usf.edu

////////////////
VERSION 1: written 13 March 2023 by E. Aseghehey
REVISION: revision history can be found on the project GitHub

////////////////
PURPOSE:
The purpose of the class is to provide a blueprint for creating car objects and defining their 
properties and behaviors.

Methods:
Each function and their description, typcial calling example, accessibility, and prototype information can be found in documentation_functionDescription.txt

////////////////
DATA STRUCTURES:
DataStructures:
- Dictionary: The class Car takes in several dictionaries as input parameters like info, performance, design, protection, and others.
- List: The class Car takes in several lists as input parameters like handling, comfort, entertainment, and others.

Attributes:
- vin (str): vehicle identification number
- info (dict): car information, containing keys: year, make, model, and mileage
- performance (dict): car performance information, containing keys: engine and transmission
- design (dict): car design information, containing keys: interior and exterior
- handling (list): a list of car handling features
- comfort (list): a list of car comfort features
- entertainment (list): a list of car entertainment features
- protection (dict): car protection information, containing keys: maintenance and warranty
- package (str): car package information
- status (Status): car availability status (enum type)
- price (int/float): car price

////////////////
ALGORITHM:
None

////////////////
ERROR HANDLING:
No explicit error handling.

////////////////
'''
####################################################################################################################

import locale
import PigeonBox.status as st
from PigeonBox.bcolors import bcolors



class Car ():
    """Class that represents a car with various attributes and methods."""

    def __init__(self, vin='', info={}, performance={}, design={}, handling=[], comfort=[], entertainment=[], protection={}, package='', status=None, price=0):
        """ A class constructor that initializes an object with various attributes such as vehicle information, performance, design, handling, comfort, entertainment, protection, package, status, and price."""
        self.vin = vin
        self.info = info
        self.performance = performance
        self.design = design
        self.handling = handling
        self.comfort = comfort
        self.entertainment = entertainment
        self.protection = protection
        self.package = package
        # Set default status to AVAILABLE if not provided
        if status is None:
            status = st.Status.AVAILABLE
        # Convert status string to Status enum if a string is provided
        if isinstance(status, str):
            status = st.strToStatus(status)
        self.status = status
        self.price = price

    def UpdateMileage(self, newMileage):
        """Update the mileage of a vehicle object."""
        self.info['mileage'] = newMileage

    def UpdateWarranty(self, newWarranty):
        """Update the warranty information of a car object."""
        self.protection['warranty'].append(newWarranty)

    def getVin(self):
        """Returns the vehicle identification number (VIN) of a vehicle object."""
        return self.vin
    
    def getStatus(self):
        """Returns the current status of a vehicle object."""
        return self.status
    
    def getStatusStr(self):
        """A method to get the string representation of the car's status"""
        return st.StatusToStr(self.status)
    
    def getCarInfo(self):
        """A method to get the string representation of the car's status."""
        return self.info

    def SetStatus(self, updated_status):
        """Sets the status of a car object either by passing in a Status enum or a string representation of a status."""
        if not isinstance(updated_status, str):
            self.status = updated_status
            return
        self.status = st.strToStatus(updated_status.lower())

    def to_dict(self):
        """"Convert object data to a dictionary format."""
        return {
            "vin": self.vin,
            "status": st.StatusToStr(self.status),
            "info": [self.info],
            "performance": [self.performance],
            "design": [self.design],
            "handling": self.handling,
            "comfort": self.comfort,
            "audio": self.entertainment,
            "protection": [self.protection],
            "package": self.package,
            "price": self.price
        }

    def serialize(car):
        """JSON serialization of Car object"""
        if isinstance(car, Car):
            return car.to_dict()
        raise TypeError("Object of type 'Car' is not JSON serializable")

    def isAvailable(self):
        """Checks if the car is available."""
        return self.status == st.Status.AVAILABLE
    
    def UpdatePrice(self, newprice):
        """"Update the price of a Car object."""
        self.price = newprice

    def getDetails(self):
        """Returns the details of a car object in a formatted string."""
        # Define a string containing the details of the car, including the VIN, package, performance, design, extras, and protection plans
        res = f"""\n{bcolors.BOLD}{self.vin}{bcolors.ENDC} with {self.package} package
        Performance
        Engine: {self.performance['engine']}, Transmission: {self.performance['transmission']}
        Mileage: {self.info['mileage']} miles
        {bcolors.BOLD}Design{bcolors.ENDC}
        Interior design: {self.design['interior']}
        Exterior design: {self.design['exterior']}
        {bcolors.BOLD}Extras{bcolors.ENDC}
        Comfort: {self.comfort}
        Entertainment {self.entertainment}
        {bcolors.BOLD}Protection plans{bcolors.ENDC}
        Maintenance {self.protection['maintenance']}
        Warranty plans {self.protection['warranty']}"""
        # Return the string representation of the car along with its details
        return self.__str__() + res
    
    def __eq__(self, __o: object) -> bool:
        """Compares two instances of the Car class for equality based on their VINs."""
        if isinstance(__o, Car):
            return self.vin == __o.vin
    
    def __str__(self) -> str:
        """Returns a string representation of a car object including its year, make, model, price, and status."""
        locale.setlocale( locale.LC_ALL, '' )
        return f"{self.info['year']} {bcolors.BOLD}{self.info['model']} {self.info['make']}{bcolors.ENDC} {bcolors.OKGREEN}{locale.currency(self.price, grouping=True )}{bcolors.ENDC} {bcolors.UNDERLINE}{self.status}{bcolors.ENDC}"

    def __repr__(self) -> str:
        """Returns a string representation of the car object including its model and make."""
        return f"{self.info['model']} {self.info['make']}"
