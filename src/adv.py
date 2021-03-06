from room import Room
from player import Player


# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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

#
# Main
#


# Message functionality


def alert(message):
    print(f"{message}")


# Notifying the player they're in a new room


def new_room():
    alert(f"You have entered the {player.room.name}, {player.name}")
    alert(f"{player.room.description}\n")


# Wrong Way Functionality


def direction_failure(direction):
    if direction == "w":
        alert("Sorry, this way is blocked, try another route!\n")
    elif direction == "s":
        alert("Sorry, this way is blocked, try another route!\n")
    elif direction == "e":
        alert("Sorry, this way is blocked, try another route!\n")
    elif direction == "w":
        alert("Sorry, this way is blocked, try another route!\n")


# Trying to enter a new room functionality


def move_player(direction, room):
    attribute = direction + "_to"
    if hasattr(room, attribute):
        return getattr(room, attribute)
    else:
        direction_failure(direction)
        return room


# Make a new player object that is currently in the 'outside' room.


player_name = input("Enter your name: ")
player = Player(player_name, room["outside"])
new_room()

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
        f"Choose a direction to get started! (N, S, E or W): ")

    if action in ["n", "s", "e", "w"]:
        player.room = move_player(action, player.room)
        new_room()
        continue

    elif action == "Q":
        print("You have been SACRIFICED! GAME OVER")
        break
