
####################################################################################################################
'''
////////////////
PROGRAM main:   provide a menu based interface for managing dealership inventory and orders. main meat of system.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu
DOCUMENTOR: Alexander Ashmore atashmore@usf.edu

////////////////
VERSION 1: written 13 March 2023 by E. Aseghehey
REVISION: revision history can be found on the project GitHub

////////////////
PURPOSE:
Manges user accounts and provides interfcae for users to interact with their account. the meat of the system.
Works as a command line interface.

Methods:
Each function and their description, typcial calling example, accessibility, and prototype information can be found in documentation_functionDescription.txt

////////////////
DATA STRUCTURES:
DataStructures:
-Lists: Used to store and manipulate data such as displaying data, validating user input, and selecting objects.
- Dictionary: A dictionary is used to store a set of responses to confirmation requests.
- Sets: used to validate the user's input and actions.

Attributes:
- data: an array of user accounts, used as input to the displayData() function to print out each element in the array.
- Auth: an object that handles user authentication.
- bcolors: a module that defines ANSI escape sequences for colored terminal output.
- newPassword: a string variable that holds the new password entered by the user.
- confirmPassword: a string variable that holds the password confirmation entered by the user.
- newUsername: a string variable that holds the new username entered by the user.
- response: a set containing the possible responses ("yes" or "no") to a confirmation prompt.
- msg: a string variable that holds a confirmation prompt.
- confirm: a string variable that holds the user's confirmation response ("yes" or "no").
- userInput: a string variable that holds the user's input.
- action: a string variable that holds the user's selected action.
- validSet: a set containing the possible values for the action variable.
- arr: an array of elements from which the user can select.
- arrLength: an integer variable that holds the length of the arr array.
- index: an integer variable that holds the index of the selected element in the arr array.
- inpt: a string variable that holds user input to be separated into an array using SeparateInputToList() function.
- objectList: a list of objects from which the user can select.
- objIndex: an integer variable that holds the index of the selected object in the objectList list.
- car: A parameter of the SearchCarMenu function, represents the car to be searched.
- searchOptions: A list that contains the search options for the car in the SearchCarMenu function.
- formattedOptions: A string representation of the searchOptions list, with each element separated by a newline character.
- validate: A set containing the valid actions for the search menu.
- action: A variable that represents the action selected by the user in the SearchCarMenu function.
- inventory: A list that contains all the cars in the inventory in the InventoryMenu function.
- options: A list that contains the options for the inventory menu in the InventoryMenu function.
- isAdmin: A boolean variable that represents whether the current user is an admin or not in the InventoryMenu function.
- carToView: A variable that represents the car selected by the user to view in the InventoryMenu function.
- confirmMsg: A string that contains the confirmation message to be displayed to the user in the InventoryMenu function.
- carToOrder: A variable that represents the car selected by the user to order in the InventoryMenu function.
- validateSet: A set containing the valid actions for the inventory menu in the InventoryMenu function.
- make_model_year: A list containing the make, model, and year of the car to be added in the AddCar function.
- mileage_color: A list containing the mileage and color of the car to be added in the AddCar function.
- engine_transmission: A list containing the engine and transmission of the car to be added in the AddCar function.
- interior_external_design: A list containing the interior and external design of the car to be added in the AddCar function.
- warranty_maintenance: A list containing the warranty and maintenance of the car to be added in the AddCar function.
- info: A dictionary that contains the basic information about the car to be added in the AddCar function.
- performance: A dictionary that contains the performance information about the car to be added in the AddCar function.
- design: A dictionary that contains the design information about the car to be added in the AddCar function.
- protection: A dictionary that contains the protection information about the car to be added in the AddCar function.
- status: A variable that represents the status of the car to be added in the AddCar function.
- creditCard: string variable used to store the credit card number entered by the user.
- customer: an optional argument used in the modifyCustomerDetails function. It is an object of the Customer class that represents a customer in the system.
- options: a list of strings that contains the options displayed to the user in various menus.
- formattedOptions: a string variable that contains the formatted version of options to be displayed to the user.
- action: string variable that stores the user's choice from the menu options.
- validSet: a set of valid input values for the getAction() function.
- customers: a list of Customer objects representing all the customers in the system.
- confirmMessage: a string variable used to store the confirmation message displayed to the user.
- address: a string variable used to store the new home address entered by the user.
- email: a string variable used to store the new email address entered by the user.
- cardNum: a string variable used to store the new credit card number entered by the user.
- user: an object of the User class that represents the user currently logged into the system.
- interface: an object of the Interface or AdminInterface class, depending on whether the user is an admin or not.
- isAdmin: a boolean variable that is True if the user is an admin and False otherwise.

////////////////
ALGORITHM:
- Enumeration: This algorithm is used in the displayData() function to iterate over 
                an array and print out each element in the array along with its index.
- Linear search: This algorithm is used in the validateUsername() function
                 to search through a list of users and check if a new username entered by the user already exists.
- Regular expressions: This algorithm is used in the ValidateUserInput()
                     function to check if the user input matches certain patterns, such as being a number or a valid email address.
- Splitting strings: This algorithm is used in the SeparateInputToList() function 
                    to split a comma-separated string into an array of values.
- The SearchCarMenu function: This function provides two options to the user, one is to order a car and the other is to modify an existing car
     It takes input from the user and then calls either the addOrderMenu function or the modifyCarMenu function depending on the user's choice.
- The InventoryMenu function: This function provides several options to the user, including viewing car details, searching for a car, filtering the inventory,
     making a customer order, and modifying the inventory (if the user is an admin). It takes input from the user and then calls the appropriate function based on the user's choice.
- The AddCar function: This function takes input from the user to create a new car and adds it to the inventory. It prompts the user for various details about the car, such as the VIN,
     make, model, year, mileage, color, price, engine, transmission, interior and exterior design, paint, handling, audio, comfort features, package, warranty, and maintenance. 
    It validates the user's input and creates a dictionary object representing the new car. The interface.AddInventory function is then called to add the new car to the inventory.

////////////////
ERROR HANDLING:
Mainly input validation
- ValueError: if the user inputs a non-integer value for the n variable,
             the program will raise a ValueError and print an error message.
- ZeroDivisionError: if the user inputs 0 as the value for n, the program 
                    will raise a ZeroDivisionError and print an error message.
- FileNotFoundError: if the program cannot find the specified file, 
                     it will raise a FileNotFoundError and print an error message.
- PermissionError: if the program does not have permission to read
                  the specified file, it will raise a PermissionError and print an error message.
- Exception: if any other unexpected error occurs, the program will 
             catch it as a generic Exception and print an error message.
- SearchCarMenu(): if the car is already ordered, it prints an error message and returns.
- InventoryMenu(): if the user inputs an invalid option, it breaks out of the loop.
- AddCar() : if the user inputs an invalid value for make, model, year, mileage, color,
            price, engine, transmission, interior, external design, package, warranty, or maintenance, 
            it prints an error message and prompts the user to input a valid value.



////////////////
'''
####################################################################################################################



from PigeonBox.interface import *
from PigeonBox.session import Auth
from PigeonBox.bcolors import *





''' Command line interface '''
def displayData(data):
    """Display an array of data along with their index."""
    if isEmpty(data): return
    #   Iterate through each element in the array and display it along with the index
    for i, val in enumerate(data):
        print(f"{i}: {val}")

def StallUntilUserInput():
    """ Stalls the program and waits for the user to press Enter to continue execution."""
    input(f"{bcolors.HEADER}\nPress any key to continue {bcolors.ENDC}")

def isEmpty(arr):
    """Checks if an array is empty and displays a warning message if it is."""
    if not arr:
        PrintFormat("Warning", "No data to display")
        return True
    return False

def validatePassword():
    """Function to validate a new password entered by the user, with confirmation."""
    # Get new password from user and return if input is empty
    newPassword = ValidateUserInput('new password')
    if not newPassword: return
    # Get confirmed password from user and return if input is empty
    confirmPassword = ValidateUserInput('confirm password')
    if not confirmPassword: return
    # Check if the passwords match, print error message and return if they don't
    if confirmPassword != newPassword:
        PrintFormat("Invalid", "Passwords do not match")
        return
    # Check if new password is same as old password, print error message and return if they are
    if newPassword == user.getPassword():
        PrintFormat("Invalid", "New password cannot be the same as old password")
        return
    
    return newPassword




''' User account details'''
def ChangePasswordMenu():
    """A function to change the password of a user through an interface."""
    # Get validated new password from user and return if input is empty
    newPassword = validatePassword()
    if not newPassword: return
    # Change user password using the new password
    interface.changeUserPassword(user, newPassword)
    PrintFormat("Success", "Password changed successfully")

def validateUsername():
    """Validates user input for a new username and checks if it is already taken or the same as the old username."""
    # Get new username from user and return if input is empty
    newUsername = ValidateUserInput('new username')
    if not newUsername: return
    # Check if new username is same as old username, print error message and return if they are
    if newUsername == user.getUsername():
        PrintFormat("Invalid", "New username cannot be the same as old username")
        return
    
    # Check if the new username is already taken, print error message and return if it is
    for usr in interface.ViewUsers():
        if usr.getUsername() == newUsername:
            PrintFormat("Invalid", "Username already taken")
            return
    return newUsername

def ChangeUsernameMenu():
    """Changes the username for a user by taking input from the user."""
    # Get validated new username from user and return if input is empty
    newUsername = validateUsername()
    if not newUsername: return
    # Change user username using the new username
    interface.changeUserUsername(user, newUsername)
    PrintFormat("Success", "Username changed successfully")






''' Checkers and validators '''
def ConfirmSelection(response = {"y", "yes", "n", "no"}, msg="") -> bool:
    """A function to confirm a user's selection through a prompt, returning a boolean value."""
    if not msg: 
        msg = "\nAre you sure you want to proceed?"
    PrintFormat("Warning", msg)
    confirm = ""
    while True:
        confirm = input("Enter [y/n] to confirm: ").lower()
        if confirm not in response:
            PrintFormat("Invalid", "Answer needs to be y/n")
            continue
        break

    if confirm in {"n", "no"}:
        return False
    PrintFormat("Success", "Action confirmed")
    return True

def ValidateUserInput(action="action", isNum=False, isEmail=False):
    """Validates user input based on certain conditions like being a number or an email address."""
    PrintFormat("Important", "\nPress 'q' to exit")
    while True:
        userInput = input(f"Enter {action}: ")
        if userInput.lower() == 'q':
            PrintFormat("Warning", "Exiting\n")
            return
        if not userInput: 
            PrintFormat("Invalid", "Bad input")
            continue
        if isNum and (not userInput.isdigit()):
            PrintFormat("Invalid", "Must be a number")
            continue
        if isEmail and ("@" not in userInput or "." not in userInput):
            PrintFormat("Invalid", "Must be a valid email address")
            continue

        PrintFormat("Success", userInput)
        return int(userInput) if isNum else userInput






''' General helper functions '''
def getAction(validSet={"1", "2", "3"}, msg="Enter action:"):
    """A function to get user input for a valid action from a set of options."""
    PrintFormat("Important", "\nPress 'q' to exit")
    action = input(f"{bcolors.UNDERLINE}{msg}{bcolors.ENDC} ").lower()
    if action == "q":
        PrintFormat("Warning", "Exiting\n")
        return
    if action not in validSet:
        PrintFormat("Invalid", "Invalid action")
        return getAction(validSet, msg)
    return action

def PickIndex(arr):
    """  Displays an array of elements and prompts the user to pick an index to select an element./
        Will display elements in array and ask user to pick one, will return the index of the element picked
        Useful for when choosing an element to view or remove. Like when removing a car, this will point to its index in the list
        and the user will be able to remove it by index."""
    arrLength = len(arr) - 1 # length to give user bounds to pick from
    while True:
        displayData(arr) # displays with (index: element) pair
        PrintFormat('Action', '\nPick index from the dislayed list above')
        index = input(f"Enter index [0-{arrLength}] OR enter 'q' to exit: ")
        if index == 'q': 
            PrintFormat("Warning", "Exiting\n")
            return # Exiting
        
        # validation
        if not index.isdigit():
            PrintFormat('Invalid',f"Invalid index! Must be a number")
            StallUntilUserInput()
            continue

        index = int(index)
        if index < 0 or index > arrLength:
            PrintFormat('Invalid',f"Invalid index! Must be greater than 0 AND smaller than maximum length")
            StallUntilUserInput()
            continue

        return index

def SeparateInputToList(inpt):
    """ Takes in a string and returns an array of the string separated by commas"""
    inpt = inpt.split(',')
    inpt = list(map(lambda x: x.strip(), inpt))
    return inpt

def GetObject(objectList):
    """ selects and returns an object once user chooses it from a list (calls on PickIndex)"""
    index = PickIndex(objectList)
    if index is None: return # Exiting

    object = objectList[index]
    PrintFormat('Success',f"\nPicked: {object}") # success message for user
    return object

def updateCarStatus(car):
    """ Update the status of a car in the inventory."""
    statuses = {"0": "available", "1": "ordered", "2": "backorder", "3": "delivered"}
    statusChoice = displayStatusOptions()
    if not statusChoice: 
        return
    
    interface.changeCarStatus(car, statuses[statusChoice])
    PrintFormat("Success", f"{car}")
    




''' helper menus'''
def AddEmployee():
    """Function to add a new employee with username, password, first name, and last name and grant admin privileges if desired."""
    username = ValidateUserInput("Enter username")
    if not username: return
    password = ValidateUserInput(f"Enter password for new user {username}")
    if not password: return
    firstName = ValidateUserInput("Enter first name")
    if not firstName: return
    lastName = ValidateUserInput("Enter last name")
    if not lastName: return
    addEmployee = None
    confirmMessage = f"Do you wish to grant Admin priviledges to {firstName}?"

    if ConfirmSelection(msg=confirmMessage):
        addEmployee = interface.AddAdmin(username, password, firstName, lastName)
    else:
        addEmployee = interface.AddEmployee(username, password, firstName, lastName)
    # check if employee was added and notify user
    if not addEmployee:
        PrintFormat("Invalid", f"User {firstName, lastName} already exists")
        return
    PrintFormat("Success", f"User {firstName, lastName} successfully added")

def RemoveEmployeeMenu():
    """ 'Menu' for removing an employee, will ask user to pick from a list of employees
    and then confirm the selection. If the user confirms, the employee will be removed"""
    employeeToDelete = GetObject(interface.getEmployeeList()) # select employee to delete
    if not employeeToDelete:
        return
    
    confirmMessage = f"\nAre you sure you want to delete {employeeToDelete}."
    confirmMessage += " They may have made orders, which will be deleted with them."
    if not ConfirmSelection(msg=confirmMessage): 
        return
    
    isRemoved = interface.RemoveUser(employeeToDelete) # remove employee
    if not isRemoved: # check if employee was removed and notify user
        PrintFormat("Invalid", "Employee not found")
        return

    PrintFormat("Success", "Removed employee successfully")

def displayStatusOptions():
    """Displays the available status options for an inventory and prompts the user to choose one."""
    options = ["Available", 
               "Ordered", 
               "BackOrder", 
               "Delivered"]
    displayData(options)
    # get user's choice of action
    action = getAction({"0","1","2","3"}, msg="Pick a status:")
    if not action: return
    return action

def CarSearch():
    """A function that searches for a car in the inventory based on the model, make, and year entered by the user."""
    print('\nSearch car in inventory')
    searchMessage = "Enter model, make and year separated by commas\n"
    searchDecision = SeparateInputToList(input(searchMessage))
    if len(searchDecision) != 3: 
        PrintFormat('Invalid', '\nCar not found, make sure you entered the correct model, make and year')
        return

    model, make, year = searchDecision[0], searchDecision[1], searchDecision[2]
    # validate input
    if not year.isdigit(): 
        PrintFormat('Invalid', '\nYear must be a number!')
        return

    car = interface.searchInventory(model, make, int(year))
    # check car exists
    if not car: 
        PrintFormat('Invalid', '\nNo car match :(')
        return
    
    PrintFormat('Success', f"\nCar details:\n{car.getDetails()}")
    return car

def filterByMenu():
    """Displays a menu to filter cars by their status and displays the filtered data."""
    filterOptions = ["Filter by Status:",
                     "1. Available",
                     "2. Ordered",
                     "3. Backorder",
                     "4. Delivered"]
    displayFilterOptions = "\n" + "\n".join(filterOptions)
    PrintFormat("Action", displayFilterOptions)
    statuses = {"1": "available", "2": "ordered", "3": "backorder", "4": "delivered"}
    filterDecision = getAction(validSet=set(statuses.keys()))
    # validate input
    if not filterDecision: return

    {"1": displayData,
    "2": displayData,
    "3": displayData,
    "4": displayData}[filterDecision](interface.ViewByStatus(statuses[filterDecision]))

def modifyInventoryMenu():
    """Allows an administrator to add or remove a car from the inventory."""
    if not isAdmin: return

    modifyCarOptions = ["1. Add car","2. Remove car"]
    formattedOptions ="\n".join(modifyCarOptions)
    PrintFormat("Action", formattedOptions)
    modifyChoice = getAction(validSet={"1","2"})
    if not modifyChoice: return

    if modifyChoice == '1': 
        AddCar()
        return
    
    RemoveCar()




''' Customer Management helper functions'''
def AddCustomer():
    """Adds a new customer with their personal and credit card details to the system."""
    PrintFormat("Important", "\nEnter customer details\n")
    firstName = ValidateUserInput("First Name")
    if not firstName: return
    lastName = ValidateUserInput("Last Name")
    if not lastName: return
    emailAddress = ValidateUserInput("email address", isEmail=True)
    if not emailAddress: return
    creditCard = validateCreditCard()
    if not creditCard: return
    homeAddress = ValidateUserInput("Home address")
    if not homeAddress: return
    # Add the customer to the interface
    customer = interface.AddCustomer(firstName, lastName, creditCard, emailAddress, homeAddress)
    if not customer: 
        PrintFormat("Invalid", "Customer already exists or email already exists")
        return

    PrintFormat('Success',f"\nAdded {customer} with success")
    return customer

def DeleteCustomerMenu(customerToDelete):
    """Deletes a customer from the system."""
    numOrders = len(customerToDelete.orders)
    confirmMessage = f"\nAre you sure you want to delete {customerToDelete}? "
    if numOrders >= 1:
        confirmMessage += f"They have {numOrders} order(s)."

    # Confirm customer deletion with user
    if not ConfirmSelection(msg=confirmMessage): 
        return
    
    #   Remove the customer from the interface
    interface.RemoveCustomer(customerToDelete)
    PrintFormat("Success", "Removed customer successfully")






''' Main menus '''
def Login():
    """ This function takes care of the login page,
      it will ask for username and password and will return the user object if the user is authenticated"""
    PrintFormat("Important", "\nLogin page")
    PrintFormat("Important", "\nWelcome to PigeonBox")
    user, attempt = None, 0
    # give the user 3 attempts to get the correct username and password
    while (user is None and attempt < 3):
        attempt+=1
        if attempt > 1:
            PrintFormat("Warning",f"\nAttempt {attempt}")
        # Employee: gkubach0 2nBztx3qzXV
        # crapinett1 KcZy6yQfn
        usr_name = input("Enter username: ")
        pwd = input("Enter password: ")
        user = Auth().Authenticate(usr_name, pwd)
        
    if not user: # if user is still None, then the user failed all 3 attempts
        PrintFormat("Invalid",'\nFailed all 3 attempts, sorry')
        return
    # user has successfully logged in
    return user

def modifyCarMenu(car):
    """Modifies car status, price, mileage, and warranty plans."""
    PrintFormat("Success", car)
    options = ["1. Change car status",
               "2. Change car price",
               "3. Change car mileage",
               "4. Change car warranty plans"]
    formattedOptions ="\n".join(options)
    PrintFormat('Action', formattedOptions)
    action = getAction(validSet={"1","2","3","4"})

    if not action: return
    elif action == "1": 
        updateCarStatus(car)
    elif action == "2":
        newPrice = ValidateUserInput("new price", True)
        if not newPrice: return
        interface.changeCarPrice(car, newPrice)
    elif action == "3":
        newMileage = ValidateUserInput("new mileage", True)
        if not newMileage: return
        interface.changeCarMileage(car, newMileage)
    else:
        newWarranty = ValidateUserInput("new warranty plans")
        if not newWarranty: return
        car.UpdateWarranty(newWarranty)

def SearchCarMenu(car=None):
    """Function to handle searching for cars in the inventory and providing actions for the search result."""
    # If a car object is not provided, prompt user to search for one.
    if not car:
        car = CarSearch()
    if car is None: return
    searchOptions = ["1. Order car",
                     "2. Modify car (status, price, mileage, warranty plans)"]

    formattedOptions ="\n".join(searchOptions)
    validate = {"1","2"}
    # Print the available options and get the user's choice of action.
    PrintFormat("Action",formattedOptions)
    action = getAction(validSet=validate)
    if not action: return
    if action == "1": 
        # If the car is already ordered, inform the user and return.
        if car.getStatusStr().lower() == "ordered":
            PrintFormat("Invalid", "Car is already ordered")
            return
        # Prompt user to add order and provide list of customers to choose from.
        addOrderMenu(car, interface.getCustomerList())
    else:
        modifyCarMenu(car)

def InventoryMenu():
    """Display an inventory menu with options to view car details, search, filter, make customer orders, and modify inventory (admin-only)."""
    PrintFormat("Purple", 'Inventory Menu')
    options = ["0. View car details",
               "1. Search",
               "2. Filter by", 
               "3. Make a customer order"]
    if isAdmin: 
        options.append("4. Add/Remove Cars")

    formattedOptions ="\n".join(options)

    while True:
        inventory = interface.GetInventory()
        displayData(inventory)
        PrintFormat("Action", formattedOptions)
        validateSet = {"0", "1", "2", "3", "4"}
        action = getAction(validateSet)
        if not action: break
        if action == '0':
            carToView = GetObject(inventory)
            print(f"\n{carToView.getDetails()}")
            confirmMsg = f"\nDo you want to modify its details (price, warranty plans, mileage, or status)?"
            if ConfirmSelection(msg=confirmMsg): modifyCarMenu(carToView)
        elif action == '1': SearchCarMenu()
        elif action == '2': filterByMenu()
        elif action == '3': 
            carToOrder = GetObject(inventory)
            if not carToOrder: continue
            addOrderMenu(carToOrder, interface.getCustomerList())
        elif action == '4': modifyInventoryMenu()
            
        StallUntilUserInput()

def AddCar():
    """ Will get user input for a new car and add it to the inventory"""
    vin = input("Enter new car's VIN: ")
    make_model_year = None
    while True:
        make_model_year = SeparateInputToList(input("Enter make, model, year (Separated by commas): "))
        if len(make_model_year) != 3:
            PrintFormat("Invalid", "Make, Model, Year must be separated by a comma")
            continue
        if not make_model_year[2].isnumeric():
            PrintFormat("Invalid", "Year has to be a number")
            continue
        break
    mileage_color = None
    while True:
        mileage_color = SeparateInputToList(input("Enter mileage, color (Separated by commas): "))
        if len(mileage_color) != 2:
            PrintFormat("Invalid", "Mileage and Color must be separated by a comma")
            continue
        if not mileage_color[0].isnumeric():
            PrintFormat("Invalid", "Mileage has to be a number")
            continue
        if not mileage_color[1].isalpha():
            PrintFormat("Invalid", "Color has to be a string")
            continue
        break

    price = input("Enter price: ")

    # Ensure that the price is a numeric value
    while not price.isnumeric():
        price = input("HAS TO BE NUMERIC! Enter price: ")
    price = int(price)

    engine_transmission = None

    # Prompt the user to enter the engine and transmission of the car
    while True:
        engine_transmission = SeparateInputToList(input("Enter engine, transmission (Separated by commas): "))
        if len(engine_transmission) != 2:
            PrintFormat("Invalid", "Engine and Transmission must be separated by a comma")
            continue
        break
    interior_external_design =None
    while True:
        interior_external_design = SeparateInputToList(input("Enter interior, external design (Separated by commas): "))
        if len(interior_external_design) != 2:
            PrintFormat("Invalid", "Interior and External Design must be separated by a comma")
            continue
        break
    paint = ValidateUserInput("paint")
    handling = [input("Enter handling: ")]
    audio = [input("Enter audio: ")]
    comfort = [input("Enter comfort features: ")]
    package = input("Enter package: ")
    warranty_maintenance = None
    while True:
        warranty_maintenance = SeparateInputToList(input("Enter warranty, maintenance (Separated by commas): "))
        if len(warranty_maintenance) != 2:
            PrintFormat("Invalid", "Warranty and Maintenance must be separated by a comma")
            continue
        break

    # Create dictionaries for car information
    info = {"model": make_model_year[1],
            "make": make_model_year[0],
            "mileage": int(mileage_color[0]),
            "year": int(make_model_year[-1]),
            "color": mileage_color[-1],}
    
    performance = {"engine": engine_transmission[0],
                    "transmission": engine_transmission[-1]}
    
    design = {"interior": [interior_external_design[0]],
              "exterior": [{"paint": paint,"extra": [interior_external_design[-1]]}]}
    
    protection = {"maintenance": warranty_maintenance[1], "warranty": [warranty_maintenance[0]]}
    status = getAction(validSet={"ordered", "available", "backorder", "delivered"}, msg="Enter status: ")
    if not status: return
    add = interface.AddInventory(vin, info=info, performance=performance,comfort=comfort, design=design, protection=protection, price=price, handling=handling, package=package, entertainment=audio, status=status)    
    if add:
        PrintFormat("Success", "Car successfully added")
    else:
        PrintFormat("Invalid", "Car already exists")

def RemoveCar():
    """Function to remove a car from the inventory."""
    # Check if there are cars in inventory
    if not interface.GetInventory():
        PrintFormat("Invalid", "No cars in inventory")
        return
    
    # Get the car to delete from the user
    car_to_delete = GetObject(interface.GetInventory())

    # Add a confirmation message for the user
    confirm_msg = f"Are you sure you want to delete {car_to_delete}"
    if interface.isCarOrdered(car_to_delete):
        confirm_msg += f" {bcolors.BOLD}it has been ordered{bcolors.ENDC}"

    # Confirm if the user really wants to delete the car
    if not ConfirmSelection(msg=confirm_msg): return

    # Remove the car from the inventory
    rem = interface.RemoveInventory(car_to_delete)
    if rem:
        PrintFormat("Success", "Removed car successfully")
    else:
        PrintFormat("Invalid", "Car not found")

def addOrderMenu(carToOrder, customers):
    """ Allows the user to add a new order to the system by selecting a car and customer."""
    PrintFormat('Important', f"\nYou are about to order this car: {carToOrder}")
    if not ConfirmSelection(): return
    # check new customer
    customer = None
    confirmMessage = "Is this order for a new customer?"
    if ConfirmSelection(msg=confirmMessage):
        customer = AddCustomer()
    else: # get from old customers 
        if isEmpty(customers): return
        customer = GetObject(customers)

    if not customer: return
    order = interface.MakeOrder(customer, carToOrder, seller=user)
    if not order:
        PrintFormat("Invalid", "Failed to make order. This car has already been ordered by someone else.")
        
        # add to back order
        confirmMessage = "Would you like to add this car to back order instead?" 
        if ConfirmSelection(msg=confirmMessage):
            interface.changeCarStatus(carToOrder, "backorder")
        return
    
    PrintFormat("Success", order)

def OrderMenu():
    """Prints the order menu and provides options to add, remove, or view orders."""
    # Print the order menu and options
    PrintFormat('Purple','Order Menu')
    options = ["What would you like to do?",
               "1. Add order",
               "2. Remove order",
               "3. View order details"]
    formattedOptions ="\n".join(options)
    
    # Loop until user chooses to exit
    while True:
        orders = interface.viewOrders()
        inventory = interface.GetInventory()
        customers = interface.getCustomerList()
        displayData(orders)

        # Print options and get user input
        PrintFormat("Action", formattedOptions)
        action = getAction() # get user option choice

        # Exit loop if user doesn't choose an option
        if not action: break

        # Add an order
        if action == "1":
            if isEmpty(inventory): continue
            carToOrder = GetObject(inventory)
            if not carToOrder: break
            addOrderMenu(carToOrder, customers)
        else:
            # checker for empty orders
            if isEmpty(orders): continue

            # Remove an order
            if action == "2":
                orderToRemove = GetObject(orders)
                confirmMessage = f"Are you sure you want to remove this order: {orderToRemove}?"
                if not ConfirmSelection(msg=confirmMessage): break
                if not orderToRemove: break
                interface.UndoOrder(orderToRemove)
            
            # View order details
            else:
                orderToView = GetObject(orders)
                if not orderToView: break
                print(orderToView.orderDetails())
                # change status
                confirmMessage = "Would you like to change the order status?"
                if ConfirmSelection(msg=confirmMessage): updateCarStatus(orderToView.getCar())

        # Wait for user input
        StallUntilUserInput()

def ManageEmployeesMenu():
    """Displays employee management menu and provides options to view, add or remove employees."""
    PrintFormat("Purple","Employee Management Menu")
    # if not admin, return as they do not have permissions to view this menu
    if not isAdmin: return
    options = ["1. View Employee details", 
               "2. Add Employee", 
               "3. Remove Employee"]
    formattedOptions ="\n".join(options)
    while True:
        employees = interface.getEmployeeList()
        displayData(employees)
        PrintFormat("Action",f"{formattedOptions}")
        action = getAction()
        if not action: break

        if action == "2": AddEmployee()
        else:
            if isEmpty(employees):  continue
            if action == "1":
                employee = GetObject(employees)
                if not employee: break
                print(employee.getDetails()) # print info like when employee joined
            else:
                RemoveEmployeeMenu()

        StallUntilUserInput() # to get user time to read message before going back to next iteration of menu

def validateCreditCard():
    """Validates a credit card number."""
    creditCard = input('Credit Card #: ')
    while len(creditCard) != 16:
        PrintFormat("Invalid", "Credit card # needs 16 digits and needs to be digits only")
        creditCard = input('Credit Card #: ')
        if not creditCard.isdigit(): continue
    return creditCard

def modifyCustomerDetails(customer=None):
    """Modify details of a customer."""
    # If customer is not given as input, get it from the list of customers
    if not customer:
        customer = GetObject(interface.getCustomerList())
        if not customer: return
    # Display options to the user
    options = ["1. Update home address",
               "2. Update email address",
               "3. Update card details"]
    formattedOptions = "\n".join(options)
    PrintFormat("Action", f"{formattedOptions}")

    # Get user action
    action = getAction()
    if not action: return
    elif action == "1":
         # Get and validate new address from the user
        address = ValidateUserInput("new address")
        if not address: return
         # Call function to change customer address
        interface.changeCustomerAddress(customer, address)
    elif action == "2":
        email = ValidateUserInput("new email", isEmail=True)
        if interface.emailExists(email):
            PrintFormat("Invalid", "Email already exists")
            return
        interface.changeCustomerEmail(customer, email)
    else:
        cardNum = validateCreditCard()
        if not cardNum: return
        interface.changeCustomerCard(customer, cardNum)
        
def ManageCustomersMenu():
    """Displays a menu for managing customers and prompts for actions to perform."""
    options = ["1. View Customer details",
               "2. Add Customer", 
               "3. Remove Customer", 
               "4. Edit Customer details"]
    formattedOptions = "\n".join(options)
    while True:
        customers = interface.getCustomerList()
        PrintFormat("Purple","Customer list")
        displayData(customers)
        PrintFormat("Action",f"{formattedOptions}")
        # validate input
        validSet = {"1","2","3","4"}
        action = getAction(validSet=validSet)
        if not action: break
        if action == "2":
            AddCustomer()
        else:
            if isEmpty(customers): continue
            customer = GetObject(customers)
            if not customer: continue

            if action == "1": 
                print(customer.getDetails())
                # update details
                confirmMessage = "Would you like to update customer details?"
                if ConfirmSelection(msg=confirmMessage): modifyCustomerDetails(customer)
            elif action == "3":
                DeleteCustomerMenu(customer)
            else:
                modifyCustomerDetails(customer)

        StallUntilUserInput()

def CarSalesMenu():
    """Displays the car sales menu and allows the user to view the sale details of delivered cars."""
    PrintFormat('Purple','\nCar Sales Menu')
    options = ["1. View sale details"]
    formattedOptions = "\n" + "\n".join(options)

    while True:
        PrintFormat('Purple','\nDelivered Cars:')
        sales = interface.getDeliveredOrders()
        
        displayData(sales)
        PrintFormat('Action', '\nWhat would you like to do?')
        print(formattedOptions)

        validateSet = {"1"}
        action = getAction(validSet=validateSet)

        if not action:
            break

        if action == '1':
            saleToView = GetObject(sales)
            
            if not saleToView:
                break

            print(saleToView.orderDetails())
            print("Delivery date:", saleToView.getDeliveryDate())

        StallUntilUserInput()

def AccountSettingsMenu():
    """ This is the menu users interact with when they want to change their account details such as password or username """
    PrintFormat("Purple","Account settings")
    options = ["1. Change password",
               "2. Change username", 
               "3. View Account Details"]
    formattedOptions ="\n".join(options)
    while True:
        PrintFormat("Action",f"{formattedOptions}")
        action = getAction()
        if not action: break

        if action == "1":
            ChangePasswordMenu()
        elif action == "2":
            ChangeUsernameMenu()
        else:
            print(f"\nUser {user.getUsername()} details:\n{user}")

        StallUntilUserInput()

def menu():
    """ Main menu that the users will first interact with. Calls on otther menus """
    # made these global because almost all menus need it
    # the options are stored as list, so its easier to add/remove options
    options = ["1. Customer Orders",
               "2. Car Sales",
               "3. Car Inventory",
               "4. Manage Customers"]
    # creating the interface based on the user type
    # employees, get the regular interface, whereas admins get the admin interface which gives them more options
    if isAdmin:
        options.append("5. Manage Employees")

    options.append("A: Account settings") # to allow users to change their passwords/username
    formattedOptions = "\n".join(options) # this is what will be displayed to the users from the options list

    while True: # menu start
        PrintFormat("Success", f"\nHi {user.getFirstName()}, what would you like to do?")
        PrintFormat('Action',formattedOptions) # display options to user
        # validating user choice
        action = getAction({"1", "2", "3", "4", "5", "a"})
        if not action: break # if user presses q, break out of the loop and return to main menu
        # calls menu based on user choice
        {"1": OrderMenu,
         "2": CarSalesMenu,
         "3": InventoryMenu,
         "4": ManageCustomersMenu,
         "5": ManageEmployeesMenu,
         "a": AccountSettingsMenu}[action]()
    
def run():
    """ Runs the main program by logging in the user, setting up the interface, and displaying the main menu."""
    global user 
    global interface
    global isAdmin

    while True:
        user = Login()
        if not user:
            break

        isAdmin = (user.getCategory().lower() == "admin")
        if not isAdmin: 
            interface = Interface()
        else: 
            interface = AdminInterface()
        menu()
        
        interface.LogOut()
        if ConfirmSelection(msg="Would you like to log in again?"): continue
        break
        


if __name__ == "__main__":
    run()