##Location Screen##


style hand_written:
    font "ArchitectsDaughter.ttf"
style hand_written_neat:
    font "Funtype.ttf"

transform shader_auto(color):
    #turns a color into a shader
    linear (0.0) matrixcolor TintMatrix(color)

transform normal_shade:
    shader_auto("#ffffff")

transform check_shade:
    shader_auto("#ffc6ff")

transform night_shade:
    shader_auto("#1d1e66")

transform highlight_shade:
    shader_auto("#fdf9b8")

transform shade_interactive(shade):
    #turns a shader interactive
    #first shade is for the background
    shade
    on idle:
        shade
    on hover:
        highlight_shade

transform normal_shade_interactive:
    shade_interactive(normal_shade)

transform check_shade_interactive:
    shade_interactive(check_shade)

transform night_shade_interactive:
    shade_interactive(night_shade)

transform check_for_night(night=3):
    (normal_shade_interactive if daytime < night else night_shade_interactive)

transform rot:
    on hover:
        rotate -90
    on idle:
        rotate 0

default tt = Tooltip("")

###BASES###
#reusable room template
screen loc_room(backgr, nighttime=3):
    add backgr at check_for_night(nighttime)
    modal True

    transclude
    use vital_info

screen base_button(typ, im, thing, loc, click, skip, nighttime, char):
    imagebutton:
        idle im at check_for_night(nighttime)
        #for hint glow
        #if it's not the computer and if the hints are enabled
        if ((loc != "option_change") and extra_hint):
            #for a scene queue that have scenes
            if typ == "check":
                if loc_glow_check(loc):
                    at check_shade_interactive
            #for buttons that always lead the same place. Cuts out the "loc_" if its a location
            if typ == "jump":
                if loc[4:] in scene_queue.keys():
                    if loc_glow_check(loc[4:]):
                        at check_shade_interactive
                else:
                    at check_shade_interactive
        focus_mask True
        #says what it is if its hovered over
        hovered tt.Action(thing)
        unhovered tt.Action("")

        action ([
            tt.Action(""), 
            Function(renpy.restart_interaction), 
            #asks before continuing if the scene skips forward and if there are other scenes to find at the same time
            ((Show("confirm_menu", typ=loc) if (skip and check_if_any_scenes(loc)) else Jump(loc)) if (typ == "jump") else 
            #checks the scene
            (Function(check_scene, "item", loc, "") if (typ == "check") else 
            #asks before sleeping
            (Show("confirm_menu", typ="sleep") if check_if_any_scenes(loc) else sleep_night)))
            ]) mouse click

screen loc_button(typ, im, thing, loc, click, skip=False, nighttime=3, char=None):
    #if the button is a character AND if they are scheduled to be there and not busy it will show
    if (char == None):
        use base_button(typ, im, thing, loc, click, skip, nighttime, char)
    elif char:
        #if the character has multiple possible times, it goes over each
        for i in scheduled[char][loc]:
            if ((daytime in i[0] and weekday in i[1]) and ([daytime, date] not in busy[char])):
                use base_button(typ, im, thing, loc, click, skip, nighttime, char)
            else:
                pass
    else:
        pass

screen loc_decoration(imag, nighttime=3):
    add imag at check_for_night(nighttime)
    modal True 

screen back_to():
    zorder 15
    frame:
        xalign 0.5
        yalign 0.9
        textbutton _("Go Back") action Jump ("loc_stairs")

screen hint(char, def_name):
    text "[char.name]: " + (hint_var(def_name, char)) style "hand_written_neat"

screen hide_button:
    imagebutton:
        idle "bg empty"
        hover "bg empty"
        action ([Hide("hint_screen"), Hide("inventory_screen"), Hide("confirm_menu")])

screen confirm_menu(typ):
    modal True
    zorder 15
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            xalign 0.5
            text _("Are you sure you want to pass the time?"):
                xalign 0.5
            text _("You may miss scenes."):
                xalign 0.5
            hbox:
                xalign 0.5
                #checks what is being done to move time forward
                textbutton _("Yes") action ([Hide("confirm_menu"), (
                    #sleeps on keyword
                    sleep_night if typ == "sleep" else 
                    #waits on keyword
                    (wait if typ == "wait" else 
                    #jumps to scene if text
                    (Jump(typ) if type(typ) == str else
                    #runs scene if list
                    (Function(run_scene, typ[0], typ[1]
                    ))))), renpy.restart_interaction])
                textbutton _("No") action (
                    [Hide("confirm_menu"), (Jump("loc_" + room_in))] if type(typ) == str else 
                    Hide("confirm_menu"))

screen inventory_item_button(item):
    vbox:
        imagebutton:
            idle item.image hovered tt.Action(item.name + ": " + item.desc)
            action Function(item.turn_on)
        text (_("Active") if item.active else "") style "hand_written_neat"

screen name_tag:
    #for knowing what you're looking at
    frame:
        modal False
        #hides frame if no text
        if (tt.value) == "":
            background "bg empty"
        #puts the box on the mouse
        pos renpy.get_mouse_pos()
        text tt.value style "hand_written_neat"
        if main_menu:
            xsize 750

###UI###

screen hint_screen():
    modal False
    zorder 15
    use hide_button
    frame:
        xalign 1.0
        yalign 0.0
        vbox:
            spacing 30
            text _("Hints") style "hand_written_neat"
            use hint(lilsis, "Clarissa")
            use hint(bigsis, "Jessie")
            use hint(mom, "Linda")
            use hint(fembro, "Addison")
            use hint(aunt, "Ruby")

screen inventory_screen():
    modal True
    zorder 15
    use hide_button
    frame:
        xalign 0.5
        yalign 0.5
        if inventory.no_of_items > 0:
            vpgrid:
                cols 5
                for item in inventory.items:
                    use inventory_item_button(item)
        else:
            text _("Inventory Empty") style "hand_written_neat"
    use name_tag

screen vital_info():
    vbox:
        if intro == False:
            frame:
                modal False
                background "bg empty"
                xsize 250
                ysize 250
                imagebutton:
                    if daytime < 1:
                        idle "UI/time1morning.png"
                        hover "UI/time2day.png"
                    if daytime == 1:
                        idle "UI/time2day.png"
                        hover "UI/time3evening.png"
                    if daytime == 2:
                        idle "UI/time3evening.png"
                        hover "UI/time4night.png"
                    if daytime > 2:
                        idle "UI/time4night.png"
                        hover "UI/time4night.png"
                    #checks if waiting would skip the scene
                    action If(daytime < 3, [(Show("confirm_menu", typ="wait") if check_if_any_scenes("wait") else wait), renpy.restart_interaction])
                text (str(days[weekday][:3]) + " " + str(date) + 
                    ("st" if str(date)[-1] == "1" else 
                    ("nd" if str(date)[-1] == "2" else 
                    ("rd" if str(date)[-1] == "3" else 
                    ("th"))))) style "hand_written":
                    xalign 0.40
                    yalign 0.85
            imagebutton:
                idle "UI/hint_idle.png" at rot
                action Show("hint_screen")
            imagebutton:
                idle "UI/inventory_idle.png" at rot
                action Show("inventory_screen")
    use name_tag

###ROOMS###

screen living_nav():
    use loc_room("bg living"):

        ###Base
        use loc_button("jump", "living_stairs", loc_name_list["stairs"], "loc_stairs", "area")

        use loc_button("jump", "living_kitchen", loc_name_list["kitchen"], "loc_kitchen", "area")

        use loc_button("jump", "living_basement", loc_name_list["basement"], "loc_basement", "area")

        use loc_button("check", "living_tv", _("TV"), "tv", "obje")

        ###Plot
        ###Generic

        ###Linda
        use loc_button("check", "living_massage", _("[fembro.name] massaging Mom"), "living_fembro", "char", char='fembro')
        use loc_button("check", "living_mom_rest", mom.role.capitalize(), "living_mom", "char", char='mom')
        ###TV
        #use loc_button("check", "living_sharing", _("[lilsis.name] and [aunt.name] sharing the TV"), "living_aunt", "char", char='aunt')
        #use loc_button("check", "living_lilsis_chill", _("[lilsis.name] binging anime"), "living_lilsis", "char", char='lilsis')
        #use loc_button("check", "living_bigsis_chill", _("[bigsis.name] watching something"), "living_bigsis", "char", char='bigsis')

screen stairs_nav():
    use loc_room("bg stairs"):

        ###Base
        if intro:
            if go_down:
                use loc_button("jump", "stairs_living", _("Mom is calling"), "day_0101_mom_the_dom", "area")
            else:
                use loc_button("jump", "stairs_fembro", _("Shrimp's room"), "day_0101_help_from_addy_1", "area")
            
        else:
            use loc_button("jump", "stairs_living", loc_name_list["living"], "loc_living", "area")

            use loc_button("jump", "stairs_bathroom", loc_name_list["bath"], "loc_bath", "area")

            #use loc_button("jump", "stairs_bigsis", loc_name_list["bed_bigsis"], "loc_bed_bigsis", "area")

            use loc_button("jump", "stairs_lilsis", loc_name_list["bed_lilsis"], "loc_bed_lilsis", "area")

            #use loc_button("jump", "stairs_mom", loc_name_list["bed_mom"], "loc_bed_mom", "area")

            use loc_button("jump", "stairs_fembro", loc_name_list["bed_fembro"], "loc_bed_fembro", "area")

            if (aunt.stage == 10 and daytime != 2) or (aunt.stage == 11 and (not inventory.get_item("Orange Paint"))):
                pass
            else:
                use loc_button("jump", "stairs_aunt", loc_name_list["bed_aunt"], "loc_bed_aunt", "area")

        ###Plot
        ###Generic

screen bath_nav():
    use loc_room("bg bath"):

        ###Base
        use loc_button("jump", "bath_door", loc_name_list["stairs"], "loc_stairs", "area")
        use loc_button("check", "bath_cabinat", _("Cabinet"), "bath_cabinat", "obje")
        use loc_button("check", "bath_sink", _("Sink"), "bath_sink", "obje")
        use loc_button("check", "bath_toilet", _("Toilet"), "toilet", "obje")
        use loc_button("check", "bath_shower", _("Shower"), "shower", "obje")

        ###Plot

        ###Generic
        if (daytime in [0]):
            if (weekday in [0, 1, 2, 3]):
                pass
                #use loc_button("check", "bath_lilsis", _("[lilsis.name] Hogging the Shower"), "bath_lilsis", "char", char='lilsis')
            else:
                pass
                #use loc_button("check", "bath_bigsis", bigsis.name, "bath_bigsis", "char", char='bigsis')
        elif (daytime in [2]):
            if (weekday in [0, 1, 2, 3]):
                pass
                #use loc_button("check", "bath_mom", mom.role.capitalize(), "bath_mom", "char", char='mom')
            elif (weekday in [4]):
                pass
                #use loc_button("check", "bath_fembro", _("[fembro.name] Showering?"), "bath_fembro", "char", char='fembro')
            else:
                pass
                #use loc_button("check", "bath_aunt", aunt.name, "bath_aunt", "char", char='aunt')
            

screen kitchen_nav():
    use loc_room("bg kitchen"):

        ###Base
        use loc_button("jump", "kitchen_living", loc_name_list["living"], "loc_living", "area")

        if (daytime in [0, 1, 2]):
            use loc_button("check", "kitchen_pan", _("Stove"), "kitchen_stove", "obje")

        ###Plot

        if (bigsis.chosen and bigsis.stage == 10):
            use loc_button("jump", "kitchen_earplugs", _("Earplugs"), "day_0103_get_the_earplugs", "item")

        use loc_button("check", "kitchen_fembro_reach", _("[fembro.name] trying to cook"), "kitchen_fembro", "char", char='fembro')
        #use loc_button("check", "kitchen_lilsis", _("Clarissa Messing around"), "kitchen_lilsis", "char", char='sis')      
        use loc_button("check", "kitchen_mom", mom.role.capitalize(), "kitchen_mom", "char", char="mom")
        ###Generic
        use loc_button("check", "kitchen_aunt", _("Ruby cooking"), "kitchen_aunt", "char", char="aunt")
        #use loc_button("check", "kitchen_bigsis", bigsis.name, "kitchen_bigsis", "char")

screen basement_nav():
    use loc_room("bg basement"):

        ###Base
        use loc_button("jump", "basement_living", loc_name_list["living"], "loc_living", "area")
        use loc_button("check", "basement_breaker", _("Breaker"), "breaker", "obje")
        use loc_button("check", "basement_heater", _("Water Heater"), "heater", "obje")
        use loc_button("check", "basement_items", _("Various Misc"), "basement_clutter", "obje")
        use loc_button("check", "basement_washer", _("Laundry Machines"), "laundry", "obje")

        ###Plot
        ###Generic

        use loc_decoration("basement_front")

#screen bed_mom_nav():
    #use loc_room("bg bed mom"):

        ###Base
        ###Plot
        ###Generic

    #use back_to

screen bed_aunt_nav():
    use loc_room("bg bed aunt"):

        ###Base
        ###Plot
        ###Generic
        use loc_button("jump", "bed_aunt_door", loc_name_list["stairs"], "loc_stairs", "area")
        use loc_button("check", "bed_aunt_bench", _("Workout Equipment"), "workbench", "obje")
        use loc_button("check", "bed_aunt_punchbag", _("Punching Bag"), "punchbag", "obje")
        

        if (daytime in [1]):
            if (weekday in [5, 6]):
                use loc_button("check", "bed_aunt_ruby_stand", _("[aunt.name] chilling"), "aunt_aunt", "char")
        #elif (daytime in [2]):
            #if (weekday in [4, 5, 6]):
                #use loc_button("check", "bed_aunt_ruby_lifting", _("[aunt.name] working out"), "aunt_aunt", "char")
        elif (daytime in [3]):
            if (weekday in [0, 1, 2, 3, 4]):
                use loc_button("check", "bed_aunt_ruby_resting", _("[aunt.name] asleep"), "aunt_aunt", "char")

screen bed_fembro_nav():
    use loc_room("bg bed fembro"):

        ###Base

        use loc_button("jump", ("bed_fembro_comp_day" if daytime < 2 else "bed_fembro_comp_night"), _("Our Computer"), "option_change", "obje")

        ###Generic
        if (daytime in [3]):
            use loc_button("check", "bed_fembro_fembro_sleep", _("[fembro.name] asleep"), "fembro_fembro", "char")
            #use loc_button("check", "bed_fembro_sisbf_sleep", _("[sisbf.name] asleep"), "fembro_sisbf", "char")
        else:
            use loc_button("sleep", "bed_fembro_bed", _("Our Bed"), "", "obje")
            if (weekday in [0, 1, 2, 3]):
                if (daytime in [0]):
                    use loc_button("check", "bed_fembro_fembro_comp", _("Ass... I mean [fembro.name]"), "fembro_fembro", "char")
                elif (daytime in [1]):
                    use loc_button("check", "bed_fembro_fembro_phone", fembro.name, "fembro_fembro", "char")

        use back_to

screen bed_lilsis_nav():
    use loc_room("bg bed lilsis"):

        ###Base
        ###Plot
        ###Generic

        use back_to

#screen bed_bigsis_nav():
    #use loc_room("bg bed bigsis"):
        #modal True

        ###Base
        ###Plot
        ###Generic

        #use back_to

screen bed_main_nav():
    use loc_room("bg bed ian"):

        ###Base
        ###Plot
        ###Generic

        use loc_button("jump", "bed_aunt_door", _("Go After Her"), "day_0101_getting_got", "area")