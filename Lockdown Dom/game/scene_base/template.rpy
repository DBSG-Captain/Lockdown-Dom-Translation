label template:

    #for adding scenes
    $ add_scene(
        #scene name
        "template",
        #times
        [0, 1, 2, 3],
        #location in scene_queue
        'stairs',
        #Moves Time forward?
        False,
        #character
        None
        )

    $ thought_bubble(
        None, _("Speech"), 
        _("Thought!")
        )

    #Checks if inventory has the item and if it's active
    if (inventory.get_item("Item") and inventory.get_item("Item").active):
        pass

    #add item
    $ inventory.add_item(all_items_list["item"])

    #replace char with character variable
    "[char.name]"

    #this is the player character's names
    "[player_name]"

    #increase stage
    ###$ character.stage += 1