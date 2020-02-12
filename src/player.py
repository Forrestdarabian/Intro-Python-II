# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room


class Explorer(Player):
    def __init__(self, name, room):
        super().__init__("John", "Outside", name, room)
