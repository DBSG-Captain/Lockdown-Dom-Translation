init python:
    #class for a scene queued for jumping
    class QueuedScene:
        def __init__(self, name, times, skip, char):
            self.name = name
            self.times = times
            self.skip = skip
            self.char = char

    #sets date
    def set_date(x):
        globals()['date'] = x

    #sets day
    def set_day(x):
        globals()['weekday'] = x

    #sets time
    def set_time(x):
        globals()['daytime'] = x

    def reset_timeline():
        #Moves week forward until Sunday, then restarts.
        set_date(1)
        set_day(4)
        set_time(0)
        globals()['finished_scenes'] = []

    def increase_date(x):
        #Moves week forward until Sunday, then restarts.
        days = (x % 7)
        if globals()['weekday'] < 6:
            set_day(globals()['weekday'] + days)
        else:
            globals()['weekday'] = 0
        set_date(globals()['date'] + x)
        set_time(0)
    
    #runs scenes at night, if not, goes to the next day
    def sleep_night(scene=""):
        if globals()['scene_queue']['night'] != []:
            run_scene('night', globals()['scene_queue']['night'][0])
        else:
            increase_date(1)
        clear_scenes()
        for char in love_interests:
            char.advance()
        if scene != "":
            renpy.jump(scene)
        else:
            renpy.jump("sleep_time")

    def clear_scenes():
        for scene_list in scene_queue:
            scene_queue[scene_list] = []

default extra_hint = False

#World
#0 - 6 is Monday to Sunday
default date = 1
default weekday = 4
define days = {
    0: _("Monday"),
    1: _("Tuesday"),
    2: _("Wednesday"),
    3: _("Thursday"),
    4: _("Friday"),
    5: _("Saturday"),
    6: _("Sunday")
}
#0 - 3 time
default daytime = 0
define times = {
    0: _("Morning"),
    1: _("Day"),
    2: _("Evening"),
    3: _("Night"),
    4: _("None")
}

default ending = "generic"
default room_in = "living"
#MC Stats
default dominant = True
default player_name = _("Ian")
#Billy Stats
default fembro_penis = True
default fembro_nouns_masc = ([_("he"), _("him"), _("his"), _("his"), _("brother"), _("bro")])
default fembro_nouns_fem = ([_("she"), _("her"), _("her"), _("hers"), _("sister"), _("sis")])
default fembro_nouns = fembro_nouns_masc
#kinks
default kink_ballbusting = False
default kink_scent = False
default kink_cuck = False

#Scenes that have yet to be played and are ready
default scene_queue = {
###Locations
    "bath": [],
    "bed_bigsis": [],
    "bed_fembro": [],
    "bed_lilsis": [],
    "bed_mom": [],
    "bed_aunt": [],
    "kitchen": [],
    "living": [],
    "stairs": [],
    "garage": [],
    "basement": [],
###Time
    "night": [],
###Items
#bed_bigsis
#bed_fembro
    "fembro_fembro": [],
    "fembro_sisbf": [],
#bed_lilsis
#bed_mom
#bed_aunt
    "aunt_aunt": [],
    "punchbag": [],
    "workbench": [],
#bathroom
    "bath_cabinat": [],
    "bath_sink": [],
    "toilet": [],
    "shower": [],
    "bath_fembro": [],
    "bath_lilsis": [],
    "bath_bigsis": [],
    "bath_aunt": [],
    "bath_mom": [],
#kitchen
    "kitchen_stove": [],
    "kitchen_fembro": [],
    "kitchen_lilsis": [],
    "kitchen_bigsis": [],
    "kitchen_aunt": [],
    "kitchen_mom": [],
    "kitchen_sisbf": [],
#living
    "tv": [],
    "living_fembro": [],
    "living_lilsis": [],
    "living_bigsis": [],
    "living_aunt": [],
    "living_mom": [],
#basement
    "breaker": [],
    "heater": [],
    "laundry": [],
    "basement_clutter": []
    }

#List of all finished scenes
default finished_scenes = []
default persistent.replay_scenes = []
#list of names, for replays

# file names:
# ro[route]-p[part]-[name]

# The game starts here.
label start:

    default inventory = Inventory([], 0)

    camera:
        perspective True

    $ choice_done_player = False


    jump age_check

label age_check:

    "WARNING: This is a smutty erotic porn game for 18+ audiences only!"
    
    "Unless the age is older in your country. Then go by that age!"

menu:

    "Now be honest. Are you 18 years old or older?"

    "Yes":
        jump make_mc
    
    "No":
        $ renpy.quit()

label start_2:

    $ intro = True

menu:
    
    "What would you like to do?"

    "Remake Character":
        jump make_mc
    
    "Start Game":
        jump day_0101_waking_from_a_dream

    "Skip Intro (New Intro, so don't)":
        jump day_0101_the_news_2

label sleep_time:

    scene black
    with shift_eyes(True, 0.8)

    pause 0.5

    scene bg bed fembro:
        background_art
    with shift_eyes(False, 0.8)

    jump loc_bed_fembro