init -1 python:
    import math
init python:
    import math
    gallery = Gallery()


#Clarissa
    gallery.button("lilsis_marker")
    gallery.unlock_image("lilsis marker smirk")
    gallery.unlock_image("lilsis marker oops")
    gallery.button("lilsis_cock_shock")
    gallery.unlock_image("lilsis cock shock")
    gallery.button("lilsis_masturbation_peak")
    gallery.unlock_image("lilsis masturbation peak")
    gallery.unlock_image("lilsis masturbation peak climax")

#Jessie
    gallery.button("bigsis_shower")
    gallery.unlock_image("bigsis shower down")
    gallery.unlock_image("bigsis shower up")
    gallery.button("bigsis_shower_kick")
    gallery.unlock_image("bigsis shower kick")
    gallery.button("bigsis_imagine")
    gallery.unlock_image("bigsis imagine heat")
    gallery.unlock_image("bigsis imagine climax")

#Linda
    gallery.button("mom_collar")
    gallery.unlock_image("mom grab collar")
    gallery.button("mom_balls")
    gallery.unlock_image("mom grab balls")
    gallery.button("mom_pov")
    #gallery.unlock_image("mom massage pov wait")
    gallery.unlock_image("mom massage pov back")
    #gallery.unlock_image("mom massage pov hot")
    gallery.button("mom_couch")
    gallery.unlock_image("mom massage couch feet fembro")
    gallery.unlock_image("mom massage couch calves fix fembro")
    #gallery.unlock_image("mom massage couch hump fembro")
    gallery.button("mom_rub")
    gallery.unlock_image("mom massage rub")
    gallery.unlock_image("mom massage rub calves")
    gallery.unlock_image("mom massage rub grope")
    gallery.unlock_image("mom massage rub back_groping grope_backing")

#Addison
    gallery.button("fembro_stuck")
    gallery.unlock_image("fembro stuck pull")
    gallery.button("fembro_sleep")
    gallery.unlock_image("fembro sleep grind separate")
    gallery.button("fembro_sleep_together")
    gallery.unlock_image("fembro sleep grind together")
    gallery.unlock_image("fembro sleep grind together hard")
    gallery.unlock_image("fembro sleep grind together hard fembro_open")
    gallery.button("fembro_reach")
    gallery.unlock_image("fembro reach low forward")
    gallery.unlock_image("fembro reach low back")
    gallery.button("fembro_fall")
    gallery.unlock_image("fembro fall")
    gallery.button("fembro_fall_balls")
    gallery.unlock_image("fembro fall balls")

#Ruby
    gallery.button("aunt_stand")
    gallery.unlock_image("aunt intro stand")
    gallery.button("aunt_paint_splash")
    gallery.unlock_image("aunt paint splash")
    gallery.button("aunt_paint_wipe")
    gallery.unlock_image("aunt paint wipe")
    gallery.button("aunt_paint_flirt")
    gallery.unlock_image("aunt paint flirt")
    gallery.button("aunt_punch")
    gallery.unlock_image("aunt surprise punch")
    gallery.button("aunt_surprise_kick")
    gallery.unlock_image("aunt surprise kick")
    gallery.button("aunt_surprise_kiss")
    gallery.unlock_image("aunt surprise kiss")
    gallery.button("aunt_show_off")
    gallery.unlock_image("aunt show_off")


screen image_gallery_navigation:
    vbox:
        textbutton "[lilsis.name]" action ShowMenu("library_lilsis")
        textbutton "[bigsis.name]" action ShowMenu("library_bigsis")
        textbutton "[mom.name]" action ShowMenu("library_mom")
        textbutton "[fembro.name]" action ShowMenu("library_fembro")
        textbutton "[aunt.name]" action ShowMenu("library_aunt")

screen image_gallery_button_temp(nam, imag, typ, lock="locked.jpg"):
    add gallery.make_button(name=nam, unlocked=imag, locked=lock) size (360, 203)

screen image_gallery_temp(listed):
    tag menu

    use game_menu(_("Gallery")):
        hbox:
            use image_gallery_navigation
            xalign 0.5
            yalign 0.5
            spacing 20
            vpgrid:
                cols 3
                spacing 15
                draggable True
                mousewheel True

                scrollbars "vertical"
                for item in listed:
                    use image_gallery_button_temp(item["name"], item["image"], item["type"])

screen library_lilsis:
    tag menu
    use image_gallery_temp([
        {"name": "lilsis_marker", "image": "lilsis marker smirk", "type": "scene"},
        {"name": "lilsis_cock_shock", "image": "lilsis cock shock", "type": "scene"},
        {"name": "lilsis_masturbation_peak", "image": "lilsis masturbation peak", "type": "scene"}
    ])

screen library_bigsis:
    tag menu
    use image_gallery_temp([
        {"name": "bigsis_shower", "image": "bigsis shower down", "type": "scene"},
        {"name": "bigsis_shower_kick", "image": "bigsis shower kick", "type": "scene"},
        {"name": "bigsis_imagine", "image": "bigsis imagine heat", "type": "scene"},
        {"name": "bigsis_imagine", "image": "bigsis imagine climax", "type": "scene"}
    ])

screen library_mom:
    tag menu
    use image_gallery_temp([
        {"name": "mom_collar", "image": "mom grab collar", "type": "scene"},
        {"name": "mom_balls", "image": "mom grab balls", "type": "scene"},
        {"name": "mom_pov", "image": "mom massage pov back", "type": "scene"},
        {"name": "mom_couch", "image": "mom massage couch feet fembro", "type": "scene"},
        {"name": "mom_rub", "image": "mom massage rub", "type": "scene"}
        ])

screen library_fembro:
    tag menu
    use image_gallery_temp([
        {"name": "fembro_stuck", "image": "fembro stuck pull", "type": "scene"},
        {"name": "fembro_sleep", "image": "fembro sleep grind separate", "type": "scene"},
        {"name": "fembro_sleep_together", "image": "fembro sleep grind together", "type": "scene"},
        {"name": "fembro_reach", "image": "fembro reach low forward", "type": "scene"},
        {"name": "fembro_fall", "image": "fembro fall", "type": "scene"},
        {"name": "fembro_fall_balls", "image": "fembro fall balls", "type": "scene"}
    ])

screen library_aunt:
    tag menu
    use image_gallery_temp([
        {"name": "aunt_stand", "image": "aunt intro stand", "type": "scene"},
        {"name": "aunt_paint_splash", "image": "aunt paint splash", "type": "scene"},
        {"name": "aunt_paint_wipe", "image": "aunt paint wipe", "type": "scene"},
        {"name": "aunt_paint_flirt", "image": "aunt paint flirt", "type": "scene"},
        {"name": "aunt_punch", "image": "aunt surprise punch", "type": "scene"},
        {"name": "aunt_surprise_kick", "image": "aunt surprise kick", "type": "scene"},
        {"name": "aunt_surprise_kiss", "image": "aunt surprise kiss", "type": "scene"},
        {"name": "aunt_show_off", "image": "aunt show_off", "type": "scene"}
    ])

screen dom_toggler(thing, var, string_var):
    vbox:
        label _(thing)
        textbutton _(("Dom" if var else "Sub")) action ToggleVariable(string_var)

screen kink_question:
    vbox:
        hbox:
            spacing 50
            use dom_toggler("Narration", dominant, "dominant")
            vbox:
                label _("Kinks")
                hbox:
                    textbutton _("Ballbusting") action ToggleVariable("kink_ballbusting")
                    textbutton _("Scent") action ToggleVariable("kink_scent")
                    textbutton _("NTR") action ToggleVariable("kink_cuck")
        hbox:
            spacing 50
            use dom_toggler(lilsis.name, lilsis.dom, "lilsis.dom")
            use dom_toggler(bigsis.name, bigsis.dom, "bigsis.dom")
            use dom_toggler(fembro.name, fembro.dom, "fembro.dom")
            use dom_toggler(mom.name, mom.dom, "mom.dom")
            use dom_toggler(aunt.name, aunt.dom, "aunt.dom")

screen scene_gallery_navigation:
    vpgrid:
        label _("Days") xsize 150
        cols 1
        textbutton "Intro" action ShowMenu("library_intro")
        textbutton "Day 1" action ShowMenu("library_day_1")
        textbutton "Day 2" action ShowMenu("library_day_2")

screen scene_gallery_button_temp(nam, scen, desc):
    textbutton nam:
        if (scen in persistent.replay_scenes):
            hovered tt.Action(desc)
            unhovered tt.Action("")
            action (Replay(scen, scope={
                "dominant": dominant, 
                "kink_ballbusting": kink_ballbusting, 
                "kink_scent": kink_scent, 
                "kink_cuck": kink_cuck,
                "lilsis": lilsis,
                "bigsis": bigsis,
                "fembro": fembro,
                "mom": mom,
                "aunt": aunt
                }
                ))
        xsize 1000

screen scene_gallery_temp(listed):
    tag menu

    use game_menu(_("Gallery")):
        vbox:
            spacing 10
            use kink_question
            hbox:
                use scene_gallery_navigation
                xalign 0
                spacing 20
                vpgrid:
                    label _("Scenes") xsize 1000
                    cols 1
                    spacing 15
                    xfill True
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                    for item in listed:
                        use scene_gallery_button_temp(item["name"], item["scene"], item["desc"])
                    xsize 1000
    use name_tag

screen library_intro:
    tag menu
    use scene_gallery_temp([
        {
            "name": _("[lilsis.name] Intro"), 
            "scene": "day_0101_waking_from_a_dream", 
            "desc": _("[lilsis.name] pranks [main.name] first thing in the morning.")
            },
        {
            "name": _("[bigsis.name] Intro"), 
            "scene": "day_0101_getting_got", 
            "desc": _("[bigsis.name] teaches [main.name] to knock the hard way.")
            },
        {
            "name": _("[fembro.name] Intro"), 
            "scene": "day_0101_help_from_addy_1", 
            "desc": _("[main.name] forgets to knock and barges in on [fembro.name] changing.")
            },
        {
            "name": _("[mom.name] and [aunt.name] Intro"), 
            "scene": "day_0101_mom_the_dom", 
            "desc": _("[mom.name] lays down the law, and [aunt.name] greets [main.name].")
            },
        {
            "name": _("The News Drops"), 
            "scene": "day_0101_the_news_1", 
            "desc": _("During an argument, the family learns about the law.")
            }
        ])

screen library_day_1:
    tag menu
    use scene_gallery_temp([
        {
            "name": _("No Respect at All"), 
            "scene": "day_0102_no_respect_at_all", 
            "desc": _("During an argument, the family learns about the law.")
            },
        {
            "name": _("Rubbing and Prying 1"), 
            "scene": "day_0102_nothing_to_do_for_a_while", 
            "desc": _("[main.name] decides to give his mother a massage.")
            },
        {
            "name": _("Paint the Room Red (Orange)"), 
            "scene": "day_0102_help_auntie", 
            "desc": _("[main.name] helps [aunt.name] paint his old room.")
            },
        {
            "name": _("Silent Night, Horny Night?"), 
            "scene": "day_0103_sleep_night_1", 
            "desc": _("[main.name] Lists in to [bigsis.name] through the wall.")
            },
        {
            "name": _("Sleep Grinding"), 
            "scene": "day_0103_sleep_night_addison", 
            "desc": _("[main.name] helps [fembro.name] paint his old room.")
            },
        {
            "name": _("Sleep Grinding Alt Start (Jessie Disabled)"), 
            "scene": "day_0103_sleep_night_silent_2_2", 
            "desc": _("[main.name] helps [fembro.name] paint his old room.")
            }
        ])

screen library_day_2:
    tag menu
    use scene_gallery_temp([
        {
            "name": _("Bonk"), 
            "scene": "day_0201_get_hit", 
            "desc": _("[main.name] tries to make [aunt.name] feel welcome in the morning... Never sneak up on an Amazon.")
            },
        {
            "name": _("All Ass, No Height"), 
            "scene": "day_0201_reach_for_it", 
            "desc": _("[fembro.name] can't reach something on the high shelf. When they try and climb, they fall ontop of [main.name].")
            },
        {
            "name": _("Strike A Pose"), 
            "scene": "day_0201_strike_a_pose", 
            "desc": _("[main.name] and [fembro.name] watch [aunt.name] flex her 'guns'.")
            }
        ])