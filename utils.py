# utils.py

# List of items
items = ['couch', 'piano', 'queen bed', 'double bed', 'dresser', 'dining table']


# Functions corresponding to actions
def explore():
    print("Exploring the area...")
    return items

def examine():
    print("Examining items carefully...")
    return True

def unlock_door():
    print("Trying to unlock the door...")
    return True

def navigate():
    print("Navigating through the maze...")
    return "You moved forward"

def restart():
    print("Restarting the game...")
    return None

def quit():
    print("Quitting the game...")
    return None
