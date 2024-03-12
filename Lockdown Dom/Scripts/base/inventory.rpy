init python:
    class Inventory():
        def __init__(self, items=[], no_of_items=0):
            self.items = items
            self.no_of_items = no_of_items

        def add_item(self, item):
            self.items.append(item)
            self.no_of_items += 1

        def remove_item(self, item):
            self.items.remove(item)
            self.no_of_items -= 1

        def get_item(self, item_name):
            for item in self.items:
                if item.name == item_name:
                    return item
            
    class InventoryItem():
        def __init__(self, name, desc, image):
            self.name = name
            self.desc = desc
            self.image = image
            self.active = False
        
        def turn_on(self):
            self.active = not self.active

define all_items_list = {
    "earplugs": InventoryItem(
        _("Ear Plugs"), 
        _("Silence is preferable to noises"), 
        "images/UI/items/earplugs.png"
        ),
    "multitool": InventoryItem(
        _("Multi-Tool"), 
        _("Whatever you need, it can do"), 
        "images/UI/items/multitool.png"
        ),
    "paint": InventoryItem(
        _("Orange Paint"), 
        _("Paint the town orange"), 
        "images/UI/items/paint.png"
        ),
    "flashlight": InventoryItem(
        _("Flashlight"), 
        _("Make sure to change the batteries~"), 
        "images/UI/items/flashlight.png"
        )
}