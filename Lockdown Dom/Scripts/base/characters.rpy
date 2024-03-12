#Characters are defined here

init python:
    class ActorMain:
        def __init__(self, character, name, role):
            #The renpy character value
            self.c = character
            #name for inserting
            self.name = name
            #archetype
            self.role = role
            #How far along in the plot is the player?
            #every 10 is a new day with a stage
            self.stage = 10
            #Is this character enabled?
            self.chosen = True
            #Is the MC dominating this character?
            self.dom = False

        def advance(self):
            #if they didn't do any scenes for that character that day
            if (self.stage % 10 == 0):
                #sets the character to missed and disables the character
                self.stage = -10
                self.chosen = False
            else:
                #advances them to the next stage.
                self.stage = (self.stage - (self.stage % 10) + 10)

    def actor_creator(char_info, code):
        #Returns the actor with a renpy character that has the image name and callback name of the character's archetype.
        return ActorMain(
            Character(char_info, color=color[code], image=code,  callback=name_callback, cb_name=code),
            char_info,
            code
        )
    
    def name_character(info, code):
        #asks to name the character
        char_info = renpy.input(_("What's their name? (Default: ") + info + ")")
        #strips the ends of the string
        char_info = char_info.strip()
        #if nothing was entered, use default
        if char_info == "":
            char_info = info
        persistent.names[code] = char_info
        return actor_creator(char_info, code)

    def thought_bubble(sayer, speech, thought):
        renpy.say(sayer, speech, multiple=2)
        renpy.say(thoughts, thought, multiple=2)

#Ian's thoughts
define thoughts = Character(None, color='#FFFFFF', image="main",  kind=bubble)


define bubble.rows = 64
define bubble.cols = 64
define bubble.default_area = ([32, 40, 22, 7] if renpy.variant("small") else [32, 45, 22, 6])

#When who is talking is unknown
define mystery = Character("???", color="FFFFFF")

#all character colors
define color = {
    "main": "#698cff",
    "lilsis": "#fd7bb8",
    "bigsis": "#9351ff",
    "mom": "#fcf956",
    "fembro": "#4edcff",
    "aunt": "#f78b26",
    "sisbf": "#93dd51"
    }


define char_default_names = {
    "main": _("Ian"),
    "lilsis": _("Clarissa"),
    "bigsis": _("Jessie"),
    "fembro": _("Addison"),
    "mom": _("Linda"),
    "aunt": _("Ruby"),
    "sisbf": _("Darian")
}
default persistent.names = {
    "main": char_default_names["main"],
    "lilsis": char_default_names["lilsis"],
    "bigsis": char_default_names["bigsis"],
    "fembro": char_default_names["fembro"],
    "mom": char_default_names["mom"],
    "aunt": char_default_names["aunt"],
    "sisbf": char_default_names["sisbf"]
}

define main = actor_creator(persistent.names["main"], "main")
default lilsis = actor_creator(persistent.names["lilsis"], "lilsis")
default bigsis = actor_creator(persistent.names["bigsis"], "bigsis")
default mom = actor_creator(persistent.names["mom"], "mom")
default fembro = actor_creator(persistent.names["fembro"], "fembro")
default aunt = actor_creator(persistent.names["aunt"], "aunt")
default sisbf = actor_creator(persistent.names["sisbf"], "sisbf")

default love_interests = [lilsis, bigsis, mom, fembro, aunt]