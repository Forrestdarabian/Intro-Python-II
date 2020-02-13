# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.item_list = []

    def new_item(self, item):
        self.item_list.append(item)

    def inventory(self):
        output = ""
        if len(self.item_list) == 0:
            return None
        else:
            for item in self.item_list:
                output += f"{item.name}"
        return output
