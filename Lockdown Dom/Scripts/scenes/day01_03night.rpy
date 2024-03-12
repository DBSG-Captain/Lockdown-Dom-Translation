label day_0103_prepare_for_rest:
    scene bg stairs:
        background_art

    show main armup at fit(False, 5)        
    
    $ thought_bubble(
        None, _("You have to help your aunt more tomorrow, so you should get plenty of rest."),
        _("Damn. Is it already this late?")
        )

    if (bigsis.chosen or _in_replay):

        "Also, you should find some way to block out sound for the night."

        "Seeing how you'll be sleeping in the room beside [bigsis.name]'s."

        "Mom usually keeps the earplugs in the kitchen for when her and [sisbf.name] get really... rowdy."

    jump loc_stairs

label day_0103_get_the_earplugs:
    scene bg kitchen:
        background_art

    show main calm grab at fit(False, 5)

    "You find the earplugs. This will be useful for sleeping soundly tonight."

    show main down
    
    $ inventory.add_item(all_items_list["earplugs"])

    menu:

        "Put in the earplugs?"

        "Put Them In":

            $ inventory.get_item("Ear Plugs").turn_on()

            "You gently put them in. They feel like they're making a vacuum seal."

            $ thought_bubble(
                None, _("All sound is muted. Almost magically."),
                _("Good.")
                )

        "...":
            
            "..."

            $ thought_bubble(
                None, _("You kind of want to hear it..."),
                _("Fuck, I'm a weirdo.")
                )
    
    $ bigsis.stage = 11

    jump loc_kitchen

label day_0103_sleep_night_1:

    scene fembro sleep grind fembro

    "You enter [fembro.name]'s room. [fembro_nouns[0]]'s already lying in bed on the outside."

    "Well, you aren't going to sleep on the floor..."

    if _in_replay:
        if kink_cuck:
            jump day_0103_sleep_night_cuck_1
        else:
            jump day_0103_sleep_night_silent_1

    if (inventory.get_item("Ear Plugs") and inventory.get_item("Ear Plugs").active):
        jump day_0103_sleep_night_silent_1
    else:
        jump day_0103_sleep_night_cuck_1

label day_0103_sleep_night_silent_1:

    scene fembro sleep grind separate

    "You climb over [fembro_nouns[2]] sleeping frame to get into bed behind [fembro_nouns[1]]."

    "The room is quiet because of the earplugs."

    "It's almost uncomfortably quiet as you drift off to sleep."
    
    scene black
    with shift_eyes()

    "..."

    jump day_0103_sleep_night_silent_wake_up

label day_0103_sleep_night_cuck_1:

    if _in_replay:
        jump day_0103_sleep_night_cuck_2

    if  ((not bigsis.chosen) and (not _in_replay)):
        
        "You climb over [fembro_nouns[2]] sleeping frame to get into bed behind [fembro_nouns[1]]."

        scene black
        with shift_eyes()

        "..."

        "(You enabled NTR... But disabled [bigsis.name]...? Why are you here?)"

        jump day_0103_sleep_night_silent_wake_up

    else:

        if (bigsis.dom or (not kink_cuck)):

            "(You didn't use the earplugs?)"

            if bigsis.dom:

                "(This route will have you go from the cuck to the bull. But I'll let you change your mind this time. Just to be safe.)"

                menu:
                    "Did you want to go from cuck to bull? Or was there a misunderstanding?"

                    "No, No netorare for me at all":
                        jump day_0103_sleep_night_silent_wake_up

                    "Yes, give me the power shift story arch!":
                        $ kink_cuck = True
                        jump day_0103_sleep_night_cuck_2

            else:

                "(I'll let you skip it this time, but try and pay more attention please.)"

                "(Let's shorten the night to one sentence.)"

                "You fall asleep trying to block out the incredibly loud noises of [bigsis.name] and [sisbf.name] fucking."

                jump day_0103_sleep_night_silent_wake_up

label day_0103_sleep_night_cuck_2:
    
    scene fembro sleep grind fembro

    $ thought_bubble(
        bigsis.c, _("Aaah!"),
        _("... Well...")
        )

    "Even [fembro.name] wakes up at that."

    scene bg bed fembro:
        background_art

    show main underwear disgust red at fit(False, 3)

    show fembro sad at fit(True, 7)

    bigsis.c "Mmmm!"

    main.c "Do they do this every night?"

    "Her moans almost drown out what [fembro.name] says."

    fembro.c "Every night [sisbf.name] comes around."

    fembro.c "They're usually louder and... lewder, but she knows mom will get upset."
    
    $ thought_bubble(
        None, _("You can't imagine lewder moans than these."),
        _("If anyone can do it, it's [bigsis.name].")
        )

    fembro.c "We should get to bed."

    scene fembro sleep grind separate

    "You crawl beside [fembro.name], lying on the inside next to the wall."

    "Front row seat, whether you like it or not."

    scene bigsis imagine climax

    bigsis.c "Mmmaaah! Yes!"

    scene bigsis imagine heat

    $ thought_bubble(
        None, _("You're erect and drooling while breathing heavily."),
        _("This is fucking torture.")
        )

    "But you aren't about to jerk off to your older sister while lying next to your twin [fembro_nouns[4]]."

    scene bigsis imagine climax

    bigsis.c "Oh Go-hod Yes!"

    scene bigsis imagine heat

    "Your mind is entrapped by the moans."

    "They're like porn moans, but more authentic. Like comparing Splenda to pure cane sugar."

    "Both are sweet, but hers just felt, real."

    "You can't resist any longer and reach into your pants, rubbing yourself as quietly as you can."

    scene bigsis imagine climax

    bigsis.c "Deeper! get in there deeper!"

    scene bigsis imagine heat

    $ thought_bubble(
        None, _("You can just barely hear the sounds of wetness through her moans."),
        _("Which hole is it?")
        )

    scene bigsis imagine climax

    bigsis.c "Fucking Christ, I love you!"

    scene bigsis imagine heat

    "If only you were the one being told this. If only any woman would make these noises for you."

    $ thought_bubble(
        None, _("But instead, your {i}sister{/i} is making these noises for [sisbf.name]."),
        _("Not... Fair...")
        )

    if bigsis.dom:

        "It's at this moment you decide this has to change."

        $ thought_bubble(
            None, _("You're going to be the one to make her moan like that."),
            _("Somehow.")
            )

    else:

        "Your older sister, who this morning dented your nuts like it was a routine, is moaning herself into a mess."
        
        $ thought_bubble(
            None, _("And you're listening to it while rubbing yourself raw."),
            _("God... I'm pathetic")
            )

    "Her words 'Have fun jerking off tonight' ring through your memory as you do just that."

    "You can't get enough of her voice, her sounds, her lust..."

    "And then... She stops. Pants and kisses replace her moans."

    bigsis.c "I... love you, you... know... that."

    "She can barely breathe."
    
    $ thought_bubble(
        None, _("You missed your chance."),
        _("Blueballs tonight, I guess.")
        )
    
    $ persistent.replay_scenes.append('day_0103_sleep_night_1')
    $ renpy.end_replay()

    $ bigsis.stage = 12
    
    scene black
    with shift_eyes()

    jump day_0103_sleep_night_addison

label day_0103_sleep_night_silent_wake_up:
    
    scene fembro sleep grind separate
    with shift_eyes(False)
    
    ""
    scene fembro sleep grind separate main_open

        
    $ thought_bubble(
        None, _("You wake up as the door opens."),
        _("[sisbf.name] is back.")
        )

    "You don't know what time it is, but you don't need the earplugs now."

    "The silence was slightly unnerving, so you take them out."

    if ((not bigsis.chosen) and (not _in_replay)):

        jump day_0103_sleep_night_silent_2_2

    else:

        jump day_0103_sleep_night_silent_2_1

label day_0103_sleep_night_silent_2_1:

    if ((not bigsis.chosen) and (not _in_replay)):

        jump day_0103_sleep_night_silent_2_2

    else:

        bigsis.c "..."

    scene black
    with shift_eyes()

    "The night goes on, but you can't get any sleep."

    "You don't even know why, but you're stuck awake."

    bigsis.c "Mmmmm."

    scene bigsis imagine heat

    $ thought_bubble(
        None, _("Is she... masturbating?"),
        _("She's so loud.")
        )

    "You know that voice. It's [bigsis.name]."

    "[sisbf.name]'s in here, so she must be."

    $ thought_bubble(
        None, _("You look over passed [fembro.name]. [sisbf.name]'s sleeping soundly on the floor. So you know she's not doing it for him."),
        _("Is she really that horny?")
        )

    $ thought_bubble(
        None, _("You're worried about getting too horny."),
        _("I can't just jerk off. It's not your bed.")
    )
    

    $ thought_bubble(
        None, _("..."),
        _("Wait... Where am I going to jerk off from now on?")
        )
    

    scene bigsis imagine climax

    bigsis.c "Aah!"

    scene bigsis imagine heat

    $ thought_bubble(
        None, _("You can't stop yourself. You reach into your pants."),
        _("I'm sorry [fembro.name].")
        )

    scene bigsis imagine climax

    bigsis.c "Maah."

    scene bigsis imagine heat

    "[bigsis.name]'s moans are different from [lilsis.name]'s, but still don't seem forced. Maybe embellished?"

    scene bigsis imagine climax

    bigsis.c "A-hah."

    scene bigsis imagine heat

    "You quickly lose any focus on the logistics of her moans as your imagination fills in the blanks left by your eyes."

    "You try your best not to let out moans yourself as you see her breasts heaving and her legs trembling."

    "She's close, you can tell by her voice."

    "And you only just got started..."

    scene bigsis imagine climax

    bigsis.c "Sllls, Ah!"

    "And there it is. Her climax."

    "You can almost hear her gushing as she does."

    "She's left panting, audible even through the wall. You're left with a hard cock in your hand."

    "Her silence takes you out the mood long enough for tiredness to make you fall asleep despite your horniness."

    "But as you sleep, you dream. You replay her climaxing in your mind again and again."

    $ thought_bubble(
        None, _("..."),
        _("One day, I'm going to make her cum like that.")
        )
    
    $ persistent.replay_scenes.append('day_0103_sleep_night_1')
    $ renpy.end_replay()

    $ bigsis.stage = 12
    
    scene black
    with shift_eyes()

    jump day_0103_sleep_night_addison

label day_0103_sleep_night_silent_2_2:

    if ((not fembro.chosen) and (not _in_replay)):

        jump day_0103_cont

    else:
    
        scene fembro sleep grind fembro reach

        "You scoot as close to [fembro.name] as you can then reach over [fembro_nouns[1]] to put the earplugs on [fembro_nouns[2]] desk."

    "As you reach over, you're basically hugging [fembro_nouns[1]] from behind."

    "You realize just how small and dainty [fembro_nouns[0]] is. [fembro_nouns[0]]'s smaller than both [bigsis.name] and [lilsis.name], despite being older than the latter."

    scene fembro sleep grind together

    "Just as you pull away, [fembro_nouns[2]] hand grabs yours. [fembro_nouns[0]] must be clingy in [fembro_nouns[2]] sleep."
    
    "This makes you hesitate enough to realize that you're basically spooning [fembro_nouns[1]]."

    "Scratch that, you are literally spooning [fembro_nouns[1]]..."

    "Your face is in [fembro_nouns[2]] hair, your chest is against [fembro_nouns[2]] back,"

    "And your cock..."

    if kink_scent:

        "You get a whiff of [fembro_nouns[2]] hair."

        "A thick oily smell. [fembro_nouns[0]] must not wash it well in the shower."

        "..."

        "You smell it again, letting the aroma sink into your mind."

    "You hug [fembro_nouns[1]] fully now."

    if fembro.dom:

        jump day_0103_sleep_night_addison_1

    else:

        jump day_0103_sleep_night_addison_2

label day_0103_sleep_night_addison:

    if ((not fembro.chosen) and (not _in_replay)):

        jump day_0103_cont

    else:

        scene bg black

        "You fade awake."

    if kink_scent:

        "An oily haze fills your nose."

        "Unwashed hair."

        "You inhale again, deeply this time."

    "Something spongy presses against your crotch."
    
    scene fembro sleep grind together hard
    with shift_eyes(False)

    "You're hugging [fembro.name] from behind..."

    "..."

    if fembro.dom:

        jump day_0103_sleep_night_addison_2

    else:

        jump day_0103_sleep_night_addison_1

label day_0103_sleep_night_addison_1:

    $ thought_bubble(
        None, _("All the pent-up lust from before goes free."),
        _("I can't take it anymore!")
        )

    scene fembro sleep grind together hard fembro_open

    "You hug [fembro_nouns[1]] firmly, realizing too late it may wake [fembro_nouns[1]] up."

    "Subtly humping into [fembro_nouns[1]], you feel like you may break [fembro_nouns[1]] if you hug any harder."

    "[fembro_nouns[2]!c] butt is like a bouncy pillow, perfect give and pushback."

    "Your dick is rubbing the underside, you could only imagine what other orientations would be like."

    "[fembro_nouns[2]!c] ass..."

    if kink_scent:

        "[fembro_nouns[2]!c] scent..."

    "[fembro_nouns[2]!c] breath..."

    "[fembro_nouns[2]!c] tiny body between your arms..."

    "It's all too much!"

    $ thought_bubble(
        None, _("..."),
        _("!!!")
        )
    
    scene fembro sleep grind together hard

    $ thought_bubble(
        None, _("You lie there, wet and embarrassed."),
        _("...")
        )

    $ thought_bubble(
        None, _("At least [fembro.name]'s still asleep..."),
        _("This would be hard to explain.")
        )

    "As you succumb to tiredness, you hear panting..."

    $ thought_bubble(
        None, _("But the voice is far too soft to be yours..."),
        _("Wait...")
        )

    $ persistent.replay_scenes.append('day_0103_sleep_night_addison')
    $ persistent.replay_scenes.append('day_0103_sleep_night_silent_2_2')
    $ renpy.end_replay()

    $ fembro.stage = 11

    jump day_0103_cont

label day_0103_sleep_night_addison_2:

    "You worry that if you rest your arm on [fembro_nouns[1]], [fembro_nouns[0]]'ll break."

    "The only part of [fembro_nouns[1]] that seems sturdy... is [fembro_nouns[2]] fat ass."

    $ thought_bubble(
        None, _("[fembro_nouns[0]!c] pushes back into you."),
        _("!")
        )
    
    scene fembro sleep grind together hard

    "Now your dick is pressed firmly against [fembro_nouns[2]] soft cheeks. You can't help but get an erection."

    "You try not to grind into [fembro_nouns[1]], barely quelling the urge."

    "Your growing erection pushes deeper and deeper between [fembro_nouns[2]] butt cheeks. You feel every agonizing moment of it."

    $ thought_bubble(
        None, _("Agonizing because you refuse to hump your sleeping [fembro_nouns[4]]'s ass."),
        _("I really, really want to... but...")
        )
    
    $ thought_bubble(
        None, _("But you also refuse to pull away."),
        _("I don't want [fembro_nouns[1]] to wake up to this.")
        )
    
    "We all know why really."

    "Blue balls it is for you, and while your dick is wedged in the most heavenly booty too."

    "[fembro_nouns[2]!c] butt is at least a good pillow for your dick as you fade into sleep."
    
    $ persistent.replay_scenes.append('day_0103_sleep_night_addison')
    $ persistent.replay_scenes.append('day_0103_sleep_night_silent_2_2')
    $ renpy.end_replay()

    $ fembro.stage = 11

    jump day_0103_cont

label day_0103_cont:

    scene black
    with shift_eyes()

    pause 0.5

    scene bg bed fembro
    with shift_eyes(False)
    
    $ sleep_night("day_0201_showing_pains")