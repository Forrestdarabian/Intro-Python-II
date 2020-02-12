# Write a class to hold player information, e.g. what room they are in
# currently.


class Avatar:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def forward(self):
        print("?")

    def backward(self):
        print("?")

    def left(self):
        print("?")

    def right(self):
        print("?")


class Explorer(Avatar):
    def __init__(self, name, room):
        super().__init__("John", "Outside", name, room)

    def walk(self):
        print(f"{self.name} is going to a new room!")
