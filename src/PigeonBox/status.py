####################################################################################################################
'''
////////////////
PROGRAM status:   defines an Enum class to represent the status of a car(available, ordered, backoreded, delivered).
                  These are used to organize vehicles by their status.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu
DOCUMENTOR: Alexander Ashmore atashmore@usf.edu

////////////////
VERSION 1: written 13 March 2023 by E. Aseghehey
REVISION: revision history can be found on the project GitHub

////////////////
PURPOSE:
The purpose of this code is to provide a convenient way to represent
and manipulate the status of cars in a car sales inventory system,
and to allow for easy conversion between string representations and enum values.

Methods:
Each function and their description, typcial calling example, accessibility, and prototype information can be found in documentation_functionDescription.txt

////////////////
DATA STRUCTURES:
DataStructures:
- Enum: to define the various status values of a car.
- Dictionary: to store the string representation of the status and its corresponding enum value.

Attributes:
None

////////////////
ALGORITHM:
None

////////////////
ERROR HANDLING:
No explicit error handling.

////////////////
'''
####################################################################################################################

from enum import Enum


class Status(Enum):
    """ Enum class that defines the status of a car, and two functions that convert 
        between the string representation of a status and its corresponding enum value."""
    
    AVAILABLE = 1   # When a car is added to the inventory and is available for purchase
    ORDERED = 2     # When a customer orders a car and it is not yet delivered
    BACKORDER = 3   # when car is out of stock -- could be a customer ordered, then got removed, set car to backorder status rather than available
    DELIVERED = 4   # when a car is delivered to a customer #TODO: add this functionality in the car sales menu

STATUS_DICT = { "available": Status.AVAILABLE,
                "ordered": Status.ORDERED,
                "backorder": Status.BACKORDER,
                "delivered": Status.DELIVERED}

def strToStatus(status: str):
    """Convert a string representation of car status to its corresponding enum value."""
    if status not in STATUS_DICT: return
    return STATUS_DICT[status]

def StatusToStr(status: Status):
    """Converts a Status enum value to its string representation."""
    for key, value in STATUS_DICT.items():
        if value == status:
            return key