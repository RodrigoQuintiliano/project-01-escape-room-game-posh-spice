##############################################################################################
################## DATA LISTs  ###############################################################
##############################################################################################
# LIST : actions available to a player
actions = ['explore', 'examine', 'unlock door', 'navigate', 'restart', 'quit']

# LIST : items
items = ['couch', 'piano', 'queen bed', 'double bed', 'dresser', "dining table"]

# LIST : doors
doors = ['door A', 'door B', 'door C', 'door D']

# LIST : keys
keys = ['key door A', 'key door B', 'key door C', 'key door D']

##############################################################################################
################## DATA DICTs  ###############################################################
##############################################################################################

# Each key in this dictionary represents a room; each value is a list of objects, doors and keys
# Dictionary : GAME AREAS
game_areas = {
    "game room" : ['couch', 'piano', 'door A', 'key door A'],
    "bedroom 1": ['queen bed', 'door A', 'door B', 'door C', 'key door B'],
    "bedroom 2": ['double bed', 'door B', 'dresser', 'key door D', 'key door C'],
    "living room": ["dining table", 'door C', 'door D'],
    "outside": ["freedom"]
}

#############################################################################################

# Keep track of the player : current space; current item to examine; and inventory of keys
# Dict : GAME STATE
game_state = {
    'space_path' : [], # player current space to navigate and make a space path
    'item_path' : [], # to select an item to examine for key; and make an item path
    'inventory': [], # to store found keys
    'time': ["display_clock_countdown"] , #library time for live timer and countdown
}



##############################################################################################
################## FUNCTIONS = ACTIONS  ######################################################
##############################################################################################
#### the order of the main functions :

# 0) player_action
### // can still input another action or repeat same one ####

# 1) explore
# // update_item_path(item) 
# // return list of items in space

# 2) examine
# // return true  if key found
# // return false if key not found and not in inventory
# // return false if key in inventory
# // return 

# 3) unlock_door
# // quiz
# // update_door_path(door)

# 4) navigate
# // 
# // update_space_path(space)

################## PLAYER_ACTION(PLAYER_INPUT) MAIN FUNCTION ######################################################


# While Loop, if else, break, return : player_action function
def player_action(player_input: str):
    while player_input != 'quit' and player_input != 'restart': # While player_input is not 'quit' and 'restart'
        print("\Here is a list of actions :",actions) # Print the list of actions
        action = input("PLAYER! Enter your action:").lower() # Player inputs space of choice
        if action in actions:
            return action
        elif action == 'quit': # Exit the function to restart the game
            print("Quitting the game. Goodbye!")
            break
        elif action == 'restart': # Restart the game
            print("Game restarting!")
            player_action('play')
        else:
            print("Value Error, choose again!")
    return action



################## PLAYER_INPUT = EXPLORE  ######################################################

# define Function : explore(space)
def explore(space: str):
    space_items = []
    print(f"You are exploring {space}. You see these items:")
    for item in items:
        print("-", item)
        space_items.append(item)
    return space_items

################## PLAYER_INPUT = EXAMINE  ######################################################

# define Function : examine
def examine(space:str):
    print(f'Here is a list of items in {space}:', explore(space))
    select_item= input(f'Select an item to examine:') #select item
    print((f'You are examining :{select_item}'))
    
    print(f'Examining the {select_item} carefully...')
    #### ITEMS in SPACE ############################################
    for select_item in space:
        
        #### GAME ROOM ITEMS ################
        # ITEM = PIANO
        if select_item == 'couch':
            key= ''
            check(space, select_item, key)
        
        # ITEM = COUCH
        elif select_item == 'piano':
            key= 'key door A'
            check(space, select_item, key)

        #### BEDROOM 1 ITEM ################
        # ITEM = QUEEN BED
        elif select_item == 'queen bed':
            key= 'key door B'
            check(space, select_item, key)
        
        #### BEDROOM 2 ITEMS ################
        # ITEM = DOUBLE BED
        elif select_item == 'double bed':
            key= 'key door C'
            check(space, select_item, key)

        # ITEM = DRESSER
        elif select_item == 'dresser':
            key= 'key door D'
            check(space, select_item, key)

        #### LIVING ROOM ITEMS ########
        # ITEM = DINNING TABLE
        elif select_item == 'dinning table':
            key= ''
            check(space, select_item, key)

        # Re-INPUT
        else:
            print("Value ERROR !", examine(space))

        result=check(space, select_item, key)
        return result 
################## FUNCTION CHECK  ######################################################
#check for key in selected item in current space
# use this function inside examine()
def check(space, select_item, key):
    #if found key and not in inventory then update inventory
    if ( key!='' and key not in game_state['inventory'] ): 
        print(f'You found {key} in {select_item}')
        update_inventory(key)
        result = True
    #elif key=='' no key found
    elif key=='':
        print(f'No key found in {select_item}')
        result=False
    #else key in inventory
    else: 
        print(f'You already have the key in your inventory {game_state["inventory"]}')  
        result=False
    return result
#####################################################################################################
################## PLAYER_INPUT = UNLOCK DOOR  ######################################################
#####################################################################################################
    #player_input = 'unlock door'
    # action = player_input  
    # action = 'unlock door'
# define Function : unlock_door(action, door, inventory, current_space)
def unlock_door(action, space, door, inventory: list ):
for i in game_areas:
    
    if 'key door A' in game_state['inventory']:
        unlock()

    print(f'You chose to unlock in {current_space} ')
        if door in space:
        door = input("Enter the door you want to try unlock : ").lower() # Player inputs space of choice
        
        if door in doors:
            print(f'Player chose to try unlock: {door}')

            if key in inventory:
                print(f"This key is already in your inventory !")
                return True
    quiz(door)
    update_door_path(door)
    
    return game_state['door_path']

################## QUIZ FUNCTION  ######################################################
def quiz(current_door):
    # Quiz function to unlock doors
    if (game_state.inventory in current_door):
        print("This door is already unlocked ~ you can proceed!")
        return player_action('play')
    else:
        print("Answer the following question to unlock the door:")
        print("What is 7 + 6?")
        answer = int(input("Your answer: "))
        if answer == 13:
            print("Correct! The door is now unlocked...")
            game_state.inventory.append(current_door)
            return True
        else:
            print("Incorrect answer. Try again!")
            return quiz(current_door)
    return player_action('play')
# call function: quiz('door A')



################## DOOR QUIZZES FUNCTIONs  ######################################################
if door == 'door A':
    

def quiz('door A'):
    print("Question: What is the primary function of Door A, as suggested by its location in the floor plan?")
    print("A) To access the outdoors.")
    print("B) To provide entry or exit to a specific room.")
    print("C) To serve as a decorative element.")

    answer = input("Enter your choice (A, B, or C): ").upper()

    if answer == "B":
        print("Correct! Door A is most likely for entering or exiting a room.")
    else:
        print("Incorrect. Try again!")



def door_b_quiz():
    print("Question: Considering the layout, which room is Door B most likely connected to?")
    print("A) The Game Room")
    print("B) Bedroom 1")
    print("C) The Outdoors")

    answer = input("Enter your choice (A, B, or C): ").upper()

    if answer == "B":
        print("Correct! Based on the plan, Door B likely leads to Bedroom 1.")
    else:
        print("Incorrect. Try again!")


def door_c_quiz():
    print("Question: If you wake up on the couch, and the key to Door C is found nearby, what is the most logical room Door C leads to, considering the floor plan?")
    print("A) The Game Room")
    print("B) Bedroom 2")
    print("C) The Outdoors")

    answer = input("Enter your choice (A, B, or C): ").upper()

    if answer == "C":
        print("Correct! It makes sense that Door C might lead outside.")
    else:
        print("Incorrect. Consider the layout again!")



def door_d_quiz():
    print("Question: Considering the floor plan, and the fact you woke up on the couch, where is Door D most likely located?")
    print("A) In the Game Room")
    print("B) In Bedroom 1")
    print("C) Not visible on the plan")

    answer = input("Enter your choice (A, B, or C): ").upper()

    if answer == "C":
        print("Correct! Since Door D isn't shown, it's not visible on the plan.")
    else:
        print("Incorrect. Maybe Door D is a secret door?")


################## PLAYER_INPUT = NAVIGATE  ######################################################
print('Player is navigating to a new space!')

def navigate(space, door, inventory):
    print(f'Navigating through the {door}')
    if door in game_paths[door_path] and space in spaces:

        # space is new_space
        while (action == 'unlock door' and action != 'quit' and action != 'restart'): # While loop
            if ('door A' in space) and ('door B' not in space) and ('door C' not in space) and ('door D' not in space):
                update_space_path('game room')

            elif ('door A' in space) and ('door B' in space) and ('door C' in space) and ('door D' not in space):
                update_space_path('bedroom 1')
        
            elif ('door A' not in space) and ('door B' in space) and ('door C' not in space) and ('door D' not in space):
                update_space_path('bedroom 2')
        
            elif ('door A' not in space) and ('door B' not in space) and ('door C' in space) and ('door D' in space):
                update_space_path('living room')
        
            elif ('door A' not in space) and ('door B' not in space) and ('door C' not in space) and ('door D' in space):
                update_space_path('outside')
                print("FREEDOM | YOU WIN !")
                print(game_state)
                break
            else:
                ("UNKNOWN SPACE in the system?")
            print(f'You are now in{space}')
        update_space_path(space)



################## GAME PATHS ######################################################

# DICTIONARY : to track paths taken by player spaces, items, doors
game_paths = {
    'space_path': [],
    'item_path': [],
    'door_path': [],
}

# update space path [game room, bedroom 1, bedroom 2...]
def update_space_path(current_space:str):
    game_paths['space path'].append(current_space)
    return game_paths['space path']

# update item path [couch, piano, queen bed...]
def update_item_path(item:str):
    game_paths['item path'].append(item)
    return game_paths['item path']

# update door path [door A, door B, door C, ...]
def update_door_path(door:str):
    game_paths['door path'].append(door)
    return game_paths['door path']

# update inventory [key door A, key door B, key door C...]
def update_inventory(key:str):
    game_paths['inventory'].append(key)
    return game_paths['inventory']

# display_clock_countdown

################## UPDATE GAME STATE ######################################################
game_state = {
    'space_path': [],
    'item_path': [],
    'door_path': [],
    'inventory': [],
    'time':["display_clock_countdown"]
    }

def update_inventory(key: str, space: str):
    game_state["inventory"].append(key)
    return game_state["inventory"]

def update_game_state(door: str, key: str, item: str, space: str):
    update_space_path(space) #update space
    update_item_path(item) #update item
    update_door_path(door) #update door
    update_inventory(key) #update key
    display_clock_countdown() #run clock countdown

    
################## RESTART FUNCTION ######################################################

def restart(answer: bool):
    reset_game_state()
    
################## PLAYER_INPUT = RESTART ######################################################

def reset_game_state():
    answer = input("Do you want to restart the game? Enter: YES or NO")
    while answer !='YES' and answer!='NO':
        answer = input("To restart Enter only : YES or NO")
    
    if answer.low() == 'yes':
        print("Restarting the game...")
        game_state["space_path"].append('game room')
        game_state["item_path"].clear()
        game_state["inventory"].clear()
        game_state["door_path"].clear()
    elif answer.low() == 'no':
        print("Continue to play...")
        player_action('play')
    else:
        print("Value Error: Enter YES or NO")

    return game_state


################## PLAYER_INPUT = QUIT ######################################################

def quit():
    print("Quitting the game...")
    return game_state



##########################################################################################################
################## EXTRA FEATURES CAN BE ADDED HERE ######################################################
##########################################################################################################

# define Function to display live clock and countdown timer
import time
import sys
from datetime import datetime, timedelta

def display_clock_countdown(minutes):
    try:
        while True:  # Repeat indefinitely (change True to play=true)
            end_time = datetime.now() + timedelta(minutes=minutes)

            while True:
                # Current time
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")

                # Remaining time
                remaining_time = end_time - now
                if remaining_time.total_seconds() <= 0:
                    print(f"\rClock: {current_time} | Countdown: 00:00:00 ⌛", end="")
                    break

                hours, remainder = divmod(int(remaining_time.total_seconds()), 3600)
                mins, secs = divmod(remainder, 60)
                countdown_str = f"{hours:02}:{mins:02}:{secs:02}"

                # Print live clock and countdown on one line
                print(f"\r🕰️ Clock: {current_time} | ⏳ Countdown: {countdown_str}", end="")
                sys.stdout.flush()

                time.sleep(1)

            # Big "Time's Up" banner
            print("\n" + "*"*50)
            print("*****            TIME'S UP!            *****")
            print("*****      Restarting countdown...     *****")
            print("*"*50 + "\n")
            time.sleep(1)  # Optional pause before restarting

    except KeyboardInterrupt:
        print("\nCountdown stopped manually.")