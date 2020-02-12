# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Outside(Room):
    def __init__(self, name, description):
        super().__init__("outside",
                         "Outside Cave Entrance, North of you, the cave mount beckons", name, description)


class Foyer(Room):
    def __init__(self, name, description):
        super().__init__("foyer",
                         "Dim light filters in from the south. Dusty passages run north and east.", name, description)


class Overlook(Room):
    def __init__(self, name, description):
        super().__init__("overlook",
                         "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", name, description)


class Narrow(Room):
    def __init__(self, name, description):
        super().__init__("narrow",
                         "The narrow passage bends here from west to north. The smell of gold permeates the air.", name, description)


class Treasure(Room):
    def __init__(self, name, description):
        super().__init__("treausre",
                         "You've found the long-lost treasurechamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.", name, description)
