init python:
    import random #

    def get_char_for_rand(scene):
        if list_of_char_for_scenes[scene]:
            char = random.choice(list_of_char_for_scenes[scene])
        else:
            char = "default"
        return char

default list_of_char_for_scenes = {
    "good_cook": []
    }

label day00_good_cook:
    scene bg bed kitchen:
        background_art
    
    "Yeah, I could use something to eat."

    $ char = "default"

    #$ char = get_char_for_rand("good_cook")
    
    #"[char]"

    if char == "lilsis":
        if lilsis.chosen:
            if lilsis.dom:
                ""
            else:
                ""
        else:
            ""

    elif char == "bigsis":
        if bigsis.chosen:
            if bigsis.dom:
                ""
            else:
                ""
        else:
            "You tried your best to make fried rice, but you made the eggs too spongy..."

            "Maybe you should ask [sisbf.name] for help, [bigsis.name] says he can cook."

            "Wait... would he think I'm racist?"

            "..."

            "Nah, [sisbf.name] would never take it that way. He's super chill."

    elif char == "fembro":
        if fembro.chosen:
            if fembro.dom:
                ""
            else:
                ""
        else:
            ""

    elif char == "mom":
        if mom.chosen:
            if mom.dom:
                ""
            else:
                ""
        else:
            ""

    elif char == "aunt":
        if aunt.chosen:
            if aunt.dom:
                ""
            else:
                ""
        else:
            ""

    else:
        "You make yourself food. Finally not pestered by anyone else."

        "You decided to make a refreshing salad."

    $ wait()

    jump loc_kitchen