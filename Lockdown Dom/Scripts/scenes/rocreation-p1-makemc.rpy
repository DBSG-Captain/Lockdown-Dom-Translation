init python:
    def set_day_stages(stage):
        reset_timeline()
        clear_scenes()
        increase_date(int((stage/10) - 1))
        lilsis.stage = stage
        bigsis.stage = stage
        mom.stage = stage
        aunt.stage = stage
        fembro.stage = stage


label make_mc:
    python:
        player_name = renpy.input("What's your name? (Default: " + char_default_names["main"] + ")")
        player_name = player_name.strip()
        if not player_name:
            player_name = char_default_names["main"]
        main = actor_creator(player_name, "main")

menu:

    "Do you want to be a sub or dom in general narration? You can choose to be a switch for specific characters later."

    "I want to dominate":
        $ dominant = True
        jump kink_question

    "I want to be dominated":
        $ dominant = False
        jump kink_question

label kink_question:

menu:
    "NTR on: ([kink_cuck]) Effects Jessie Path,
    Can have Netori without Netorare":
        $ kink_cuck = not kink_cuck
        jump kink_question

    "Ballbusting on: ([kink_ballbusting]) Catered for Subs":
        $ kink_ballbusting = not kink_ballbusting
        jump kink_question

    "Scent on: ([kink_scent])":
        $ kink_scent = not kink_scent
        jump kink_question

    "Done":
        jump start_2

label option_change:

menu:
    
    "What would you like to do?"

    "Rename Character":
        jump rename_character
    
    "Change Active and Dominant Characters":
        jump disable_question
    
    "Change [fembro.name]'s Sex/Gender":
        jump change_fembro
    
    "Set Day":
        jump set_day_stages

    "Get Item":
        jump get_item
    
    "Exit":
        jump loc_bed_fembro

label disable_question:
menu:
    "Who do you want to have lewd scenes for?"

    "[lilsis.name]: [lilsis.chosen]":
        $ lilsis.chosen = not lilsis.chosen
        jump disable_question

    "[bigsis.name]: [bigsis.chosen]":
        $ bigsis.chosen = not bigsis.chosen
        jump disable_question

    "[mom.name]: [mom.chosen]":
        $ mom.chosen = not mom.chosen
        jump disable_question

    "[fembro.name]: [fembro.chosen]":
        $ fembro.chosen = not fembro.chosen
        jump disable_question

    "[aunt.name]: [aunt.chosen]":
        $ aunt.chosen = not aunt.chosen
        jump disable_question

    "Ready":
        jump dom_question

label dom_question:
menu:
    "Who will you Dominate, and to whom will you Submit?"

    "General Dominant: [dominant]" if choice_done_family:
        jump dom_question

    "Dominate [lilsis.name]: [lilsis.dom]":
        $ lilsis.dom = not lilsis.dom
        jump dom_question

    "Dominate [bigsis.name]: [bigsis.dom]":
        $ bigsis.dom = not bigsis.dom
        jump dom_question

    "Dominate [mom.name]: [mom.dom]":
        $ mom.dom = not mom.dom
        jump dom_question

    "Dominate [aunt.name]: [aunt.dom]":
        $ aunt.dom = not aunt.dom
        jump dom_question

    "Dominate [fembro.name]: [fembro.dom]":
        $ fembro.dom = not fembro.dom
        jump dom_question

    "Ready":
        if choice_done_family:
            jump option_change
        else:
            jump day_0101_what_now

label change_fembro:
    menu:

        "What is [fembro.name]?"

        "He's My Brother":
            $ fembro_penis = True
            $ fembro_nouns = fembro_nouns_masc


        "She's My Sister":
            $ fembro_penis = False
            $ fembro_nouns = fembro_nouns_fem


        "She's My Sister with a Dick":
            $ fembro_penis = True
            $ fembro_nouns = fembro_nouns_fem
    
    if choice_done_fembro:
        jump option_change
    else:
        jump day_0101_help_from_addy_2

label rename_character:

menu:
    
    "Who do you want to rename?"

    "[main.name], You":
        $ main = name_character(main.name, "main")
        jump rename_character

    "[lilsis.name], The Younger Sister":
        $ lilsis = name_character(lilsis.name, "lilsis")
        jump rename_character

    "[bigsis.name], The Older Sister":
        $ bigsis = name_character(bigsis.name, "bigsis")
        jump rename_character
    
    "[fembro.name], The Twin":
        $ fembro = name_character(fembro.name, "fembro")
        jump rename_character
    
    "[mom.name], The Mother":
        $ mom = name_character(mom.name, "mom")
        jump rename_character
    
    "[aunt.name], The Aunt":
        $ aunt = name_character(aunt.name, "aunt")
        jump rename_character
    
    "[sisbf.name], [bigsis.name]'s Boyfriend":
        $ sisbf = name_character(sisbf.name, "sisgf")
        jump rename_character
    
    "Go Back":
        jump option_change

label set_day_stages:
    
menu:
    
    "What day do you want to skip to"

    "Day 1":
        $ set_day_stages(10)
        jump day_0101_what_now

    "Day 2":
        $ set_day_stages(20)
        jump day_0201_showing_pains
    
label get_item:
    python:
        item = renpy.input("Item do you want?")
        if item in all_items_list.keys():
            inventory.add_item(all_items_list[item])
            renpy.jump("loc_bed_fembro")
        else:
            renpy.say(None, "No such Item")
            renpy.jump("option_change")