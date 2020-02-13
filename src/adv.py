from room import Room
from player import Player
from item import Item


# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together


room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Room Items

room["foyer"].item_list.append(
    Item("Sword: A mighty sword to aid you on your quest!", "sword"))
room["narrow"].item_list.append(
    Item("Shield: A durable shield for protection against anything that might stand in your way!", "shield"))
room["overlook"].item_list.append(
    Item("Dynamite: Explosive T.N.T. (Adult supervision is required)", "dynamite"))
room["treasure"].item_list.append(
    Item("Empty Chest: An empty treasure chest...Great souvenir!", "empty chest"))


#
# Main
#


# Message functionality


def alert(message):
    print(f"{message}")


# Notifying the player they're in a new room

def new_room():
    alert(f"You are in the {player.current_room.name}\n")
    alert(f"{player.current_room.description}\n")
    alert(f"You picked up an item -> {player.current_room.inventory()}\n")


# Wrong Way Functionality


def direction_failure(direction):
    if direction == "n":
        alert("Sorry, this way is blocked, try another route!\n")
    elif direction == "s":
        alert("Sorry, this way is blocked, try another route!\n")
    elif direction == "e":
        alert("Sorry, this way is blocked, try another route!\n")
    elif direction == "w":
        alert("Sorry, this way is blocked, try another route!\n")


# Trying to enter a new room functionality


def move_player(direction, current_room):
    attribute = direction + "_to"
    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)
    else:
        direction_failure(direction)
        return current_room


# Make a new player object that is currently in the 'outside' room.
player_name = input("Enter your name: ")
player = Player(player_name, room["outside"])

alert(f"Player: {player.name}, Room: {player.current_room.name}")
alert(f"{player.current_room.description}\n")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    action = input(
        f"Choose a Direction, {player.name}! (N, S, E, W or Q to quit): ").lower()

    if len(action) == 1:
        action = action[0]
        print("action", action)

    if action in ["n", "s", "e", "w"]:
        player.current_room = move_player(action, player.current_room)
        new_room()

    elif action == "q":
        print("You have been SACRIFICED! GAME OVER")
        break
