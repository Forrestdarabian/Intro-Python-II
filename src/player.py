# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.item_list = []

    # def __str__(self):
    #     return f"Player: {self.name}, Room: {self.room.name}...{self.room.description} Item Found: {self.room.item_list}"
