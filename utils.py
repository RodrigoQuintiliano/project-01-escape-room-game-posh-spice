

# LIST : actions available to a player
actions = ['explore', 'examine', 'unlock door', 'navigate', 'restart', 'quit']

# LIST : items
items = ['couch', 'piano', 'queen bed', 'double bed', 'dresser', "dining table"]

# LIST : doors
doors = ['door A', 'door B', 'door C', 'door D']

# LIST : keys
keys = ['key door A', 'key door B', 'key door C', 'key door D']

# Functions corresponding to actions


# define Function : explore(current_space)
def explore(current_space: str):
    print(f"You are exploring {current_space}. You see these items:")
    for item in items:
        print("-", item)
    return items

# define Function : examine(current_item)
def examine(current_item: str):
    print("Examining items carefully...")
    return True

# define Function : unlock(current_door, inventory)
def unlock_door(current_door: str, inventory: list):
    #player_input != 'play'
    while current_door != 'quit' and current_door != 'restart': # While Loop
        door = input("Type the door you want to try unlock : ").lower() # Player inputs space of choice
        if door in doors:
            print("Player chose to unlock :",door)
                if door == 'door A':
            break
        else:
            print("Value Error, choose again!")
    return door

        
    return door

def navigate():
    print("Navigating through the maze...")
    return "You moved forward"

def restart():
    print("Restarting the game...")
    return None

def quit():
    print("Quitting the game...")
    return None
