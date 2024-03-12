
define loc_list = [
    "bed_bigsis", 
    "bed_fembro", 
    "bed_lilsis", 
    "bed_mom", 
    "bed_aunt", 
    "bath", 
    "kitchen", 
    "living", 
    "stairs", 
    "basement"
    ]
define loc_name_list = {
    "bed_bigsis": _("[bigsis.name]'s Den"),
    "bed_fembro": _("[fembro.name]'s Room"),
    "bed_lilsis": _("[lilsis.name]'s Room"),
    "bed_mom": _("Mom's Room"),
    "bed_aunt": _("Aunt [aunt.name]'s Room"),
    "bath": _("Bathroom"),
    "kitchen": _("Kitchen"),
    "living": _("Living Room"), 
    "stairs": _("Upstairs"),
    "basement": _("The Basement")
    }

init python:
    #checks for scene and moves time forward.
    def wait():
        local = globals()['room_in']
        #if there are any scenes
        if scene_queue[local] != []:
            check_scene("wait", local, "")
        #Moves time forward until night, then won't proceed
        else:
            #if it's not night
            if globals()['daytime'] < 3:
                set_time(globals()['daytime'] + 1)
            else:
                pass
    #entering a new location
    def location_new(local, nave):
        #If not going outside, than change the room the player is in to the location
        globals()['room_in'] = local
        scene_queue = globals()['scene_queue']
        #if local queue is empty calls the screen
        if scene_queue[local] == []:
            renpy.call_screen(nave)
        else:
            check_scene("loc", local, nave)
    #adding a scene to the queue
    def add_scene(scene, times, loc, skip=False, char=None):
        if scene in finished_scenes:
            return
        scene = QueuedScene(
            scene,
            times,
            skip,
            char
            )
        scene_queue[loc].append(scene)

    #playing a scene
    def run_scene(loc, scene):
        if scene.name in finished_scenes:
            return
        finished_scenes.append(scene.name)
        scene_queue[loc].remove(scene)
        if scene.skip:
            wait()
        renpy.jump(scene.name)
    
    #checks if the character is chosen for the scene
    def check_char(char):
        #separate flags for initiation check and glow check 
        check = False
        glow = False
        #if the scene has a character
        if char != None:
            #if the scene has multiple characters
            if type(char) == list:
                for person in char:
                    #if any of the characters are chosen, even just one
                    if person.chosen:
                        check = True
                        glow = True
            elif char.chosen:
                check = True
                glow = True
        else:
            glow = True
        return [check, glow]

    #checks if there are any scenes the player will miss
    def check_if_any_scenes(loc):
        check_popup = False
        #check every scene in every scene list
        for scene_list in scene_queue:
            for scene in scene_queue[scene_list]:
                #if the time is the present time of day flag a possibly missed scene, and exclude the present location to prevent false flagging
                if (daytime in scene.times) and (scene_list != loc):
                    check_popup = check_char(scene.char)[0]
        return check_popup

    def loc_glow_check(loc):
        glow = False
        #checks the local scene queue
        for scene in scene_queue[loc]:
            #if the time of the scene is the present time
            if (daytime in scene.times):
                glow = check_char(scene.char)[1]
        return glow

    #checks if scene should be ran
    def check_scene(check_type, local, nave):
        if scene_queue[local] != []:
            #checks all the scenes in the queue
            for i in scene_queue[local]:
                #if it has a wait
                num = 0
                #makes sure that you catch the scene that needs to be waited for
                if check_type == "wait":
                    num = 1
                if (daytime+num) in i.times:
                    if num > 0:
                        set_time(globals()['daytime'] + 1)
                    #if there are other scenes, checks first
                    if i.skip and check_if_any_scenes(local):
                        renpy.show_screen("confirm_menu", typ=[local, i])
                    else:
                        #if it skips time, skips then finally runs scene
                        run_scene(local, i)
                    break
                else:
                    if local not in loc_list:
                        renpy.jump(local + "_idle")
        else:
            renpy.jump(local + "_idle")
        #goes to the location after
        if check_type == "loc":
            renpy.call_screen(nave)
        #moves time forward
        elif check_type == "wait":
            set_time(globals()['daytime'] + 1)

    #checks if scene should be ran
    def check_scene_other(check_type, local, nave):
        if scene_queue[local] != []:
            #checks all the scenes in the queue
            for i in scene_queue[local]:
                if (daytime+1) in i.times:
                    if i.skip and check_if_any_scenes(local):
                        renpy.show_screen("confirm_menu", typ=[local, i])
                    else:
                        run_scene(local, i)
                    #if an item in the room, return to the room after scene
                    break
                else:
                    if local not in loc_list:
                        renpy.jump(local + "_idle")
        else:
            renpy.jump(local + "_idle")
        
transform background_art(even=False):
    blur 3
    (check_for_night if (not even) else normal_shade_interactive)
        

label loc_bath:
    scene bg bath:
        background_art
    $ location_new('bath', "bath_nav")

label loc_kitchen:
    scene bg bed kitchen:
        background_art
    $ location_new('kitchen', 'kitchen_nav')

label loc_living:
    scene bg living:
        background_art
    $ location_new('living', 'living_nav')

label loc_stairs:
    scene bg stairs:
        background_art
    $ location_new('stairs', 'stairs_nav')

label loc_basement:
    scene bg basement:
        background_art
    $ location_new('basement', 'basement_nav')

label loc_bed_bigsis:
    scene bg bed bigsis:
        background_art
    $ location_new('bed_bigsis', "bed_bigsis_nav")

label loc_bed_fembro:
    scene bg bed fembro:
        background_art
    $ location_new('bed_fembro', "bed_fembro_nav")

label loc_bed_lilsis:
    scene bg bed lilsis:
        background_art
    $ location_new('bed_lilsis', "bed_lilsis_nav")

label loc_bed_mom:
    scene bg bed mom:
        background_art
    $ location_new('bed_mom', "bed_mom_nav")

label loc_bed_aunt:
    scene bg bed aunt:
        background_art
    $ location_new('bed_aunt', "bed_aunt_nav")