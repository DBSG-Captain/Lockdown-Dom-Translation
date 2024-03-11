label day_0201_showing_pains:

    scene bg bed fembro:
        blur 3

    "You wake up, surprisingly refreshed given what happened the night before."

    "[fembro.name] has already left the room... "

    $ add_scene(
        "day_0201_get_hit",
        [0],
        'kitchen_aunt',
        True,
        aunt
        )

    $ add_scene(
        "day_0201_reach_for_it",
        [0],
        'kitchen_fembro',
        False,
        fembro
        )

    $ add_scene(
        "day_0201_strike_a_pose",
        [1],
        'aunt_aunt',
        False,
        aunt
        )
    

    jump loc_bed_fembro

label day_0201_get_hit:

    if ((not aunt.chosen) and (not _in_replay)):

        jump kitchen_aunt_idle

    else:

        scene bg kitchen:
            background_art
        
        show aunt disgust at fit, set_place(9)
        #tired

        show main calm at fit, set_place(4)

        $ thought_bubble(
            None, _("You didn't know Aunt [aunt.name] woke up this early,"),
            _("Isn't it her day off?")
            )

    $ thought_bubble(
        None, _("Then again, she may not be used to it."),
        _("She looks like she's dying.")
        )

    main.c "Hey."

    show aunt fear at fit
    #frightened

    "You place a hand on her shoulder."

    scene aunt surprise punch

    "{i}POW{/i}"

    if aunt.dom:
        
        "You're thrown back almost a yard. Barely able to keep yourself from collapsing."

        scene bg kitchen:
            background_art

        show aunt fear at fit, set_place(9), flip
        #tired

        show main disgust a-out at fit, set_place(4):
        # in Paint
            subpixel True 
            set_place(4) 
            easein2 0.2 set_place(1)
        with Pause(0.3)
        show main fear at fit:
            set_place(1)

        main.c "FUCK!"

        aunt.c "What! [main.name]?!"

        show main anger a-down
        #Upset

        main.c "What was that for?"

        show aunt sad
        #Apologetic

        aunt.c "I'm so sorry, I'm not used to hearing a man's voice in the morning."

        show main sad
        #bothered

        show aunt surprise
        #In shock

        aunt.c "More importantly, how are you still standing? Everyone I hit ends up on the floor."

        main.c "Well, I'm sturdy as hell."

        show aunt happy
        #amazed and impressed

        show main calm
        #relaxed

        $ thought_bubble(
            aunt.c, _("Damn. It must be the 'Cason' family genes."),
            _("I have an idea.")
            )

        show main sad red
        #faking pain

        main.c "It still hurts a lot though."

        show aunt sad
        #concerned

        aunt.c "Aw shit. Should I take you to the hospital?"

        main.c "No, it's not that bad. A kiss should be enough."

        show aunt surprise
        #blushing

        $ thought_bubble(
            aunt.c, _("..."),
            _("That's the first time I've seen her blush.")
            )

        show aunt happy
        #laughing

        aunt.c "You sly tod."

        show aunt non
        #smiling
        
        aunt.c "Sure. why not?"

        "You want to take the chance to kiss her, but she's too quick. By the time you realize she said yes, her lips are already on you."

    else:

        if kink_ballbusting:

            scene aunt surprise kick

            "{i}WHACK{/i}"

            "Your breath is stolen as you are lifted off your feet."

            "Then, you feel the sharp pain of the impact."

            main.c "FUCK!"

            "Of course, the universe is merciful, and you don't have time to focus on that pain."
            
            scene aunt surprise bonk

            "{i}THUMP{/i}"
        
        "With your head ringing and your legs wobbling, gravity does its thing."
        
        scene aunt surprise aftermath

        aunt.c "Holy Shit! [main.name]?!"

        "You barely understand her as all sound fades. You can't keep your eyes open."

        "The pain starts to set in... You let the darkness take you."

        scene bg black
        with shift_eyes()

        pause 2

        "[main.name[0]]-[main.name]?"

        scene bg kitchen:
            background_art
        
        show aunt fear at fit, set_place(7), flip
        #Panic

        show main disgust at fit, set_place(4)
        #pain

        with shift_eyes(False)

        "God, your head hurts."

        if kink_ballbusting:

            "Your balls feel like they were hit by a hammer."

            $ thought_bubble(
                None, _("And not a rubber mallet."),
                _("Please... Still work...")
                )

        "You're dizzy and slightly nauseous."

        aunt.c "I'm soooo sorry."

        aunt.c "Can you hear me?"

        main.c "Yeah?"

        aunt.c "I'm not used to hearing a man's voice in the morning, you scared the hell out of me."

        aunt.c "But I'm so sorry, I-"
        
        show aunt sad at fit

        show main sad at fit

        main.c "I'm alright, Auntie. Take a minute to breathe."

        "She inhales, then exhales, blowing your hair back."
        
        main.c "I'm not injured, and that's all that matters."

        if kink_ballbusting:

            "Your crotch disagrees, but oh well."

        show aunt non

        aunt.c "Yeah, you're right."

        aunt.c "Come here, you."

        "She brings you close and kisses your head."

    scene aunt surprise kiss

    "She wraps her arms around you, hugging you tenderly."

    "Her boobs press against your face as she pulls you in tightly."

    "You're surprised someone so muscular can also be so soft."

    "Her flexed muscles overpower that softness though, and her firm grip pushes you further into her bust."
    
    "You feel like, if she wanted to, she could squeeze you to death."

    "The softness of her lips, however, is unadulterated."

    "Eventually, you have a little trouble breathing."

    "Despite that, you feel incredibly safe in her arms, between her breasts."
    
    scene bg kitchen:
        background_art
    
    show aunt non at fit, set_place(7), flip
    show main happy red at fit, set_place(4)

    "She pulls away, and it feels too soon."

    $ thought_bubble(
        None, _("Why are you getting so worked up over a kiss on the head from your aunt?"),
        _("There were also boobs.")
        )
    
    show aunt non at fit, flip

    aunt.c "If you need anything just say."

    hide aunt
    with easeoutleft

    if (not aunt.dom and kink_ballbusting):

        show main fear at fit

        "When you move, you're almost brought to your knees by the pain in your balls."

        $ thought_bubble(
            None, _("Your butt hurts a lot, so it must have taken most of the force."),
            _("Thank God, not a direct hit.")
            )

        $ thought_bubble(
            None, _("You try your best not to make a scene as you waddle out of the kitchen."),
            _("Please... Still work.")
            )

    $ persistent.replay_scenes.append('day_0201_get_hit')
    $ renpy.end_replay()
        
    $ set_time(1)
 
    $ aunt.stage = 21

    jump loc_kitchen

label day_0201_reach_for_it:

    if ((not fembro.chosen) and (not _in_replay)):

        jump kitchen_fembro_idle

    else:
        
        scene bg kitchen:
            background_art
        
        show fembro sad at fit, set_place(8)
        #tired

        show main sad at fit, set_place(4)
        #nervous

        fembro.c "Ngh"

    "[fembro.name]'s trying to reach spices at the top shelf."

    show fembro anger at fit
    #Frustrated

    fembro.c "[bigsis.name] put those up there on purpose!"

    "[fembro_nouns[0]!c]'s probably right. [bigsis.name] loves fucking with [fembro_nouns[1]]."

    $ thought_bubble(
        main.c, _("Hey [fembro.name], I wanna-"),
        _("Focus.")
        )
    
    scene fembro reach low forward

    $ thought_bubble(
        main.c, _("What are you doing?"),
        _("Woah")
        )

    scene fembro reach low back

    fembro.c "We're not all tall like you, [main.name]."

    "[fembro_nouns[0]!c] smiles back at you."

    main.c "But you can't climb to save your life. Let me get it."

    $ thought_bubble(
        fembro.c, _("No! No. I can do it myself."),
        _("[fembro_nouns[0]!c] has something to prove. But to who?")
        )

    $ thought_bubble(
        None, _("[fembro_nouns[0]!c]'s surprisingly weak at climbing."),
        _("With all that booty too...")
        )

    scene fembro cabinat

    main.c "At least get a ladder or something."

    scene fembro cabinat peak

    fembro.c "No thanks, I need my oregano."

    "[fembro_nouns[0]!c]'s barely holding [fembro_nouns[1]]self up."

    "Until [fembro_nouns[0]] isn't."
    
    scene fembro cabinat
    
    fembro.c "AAH!"

    main.c "[fembro.name]!"

    scene black

    "..."

    "A familiar sponginess hugs your crotch."

    fembro.c "[main.name]"

    if fembro_penis:
        scene fembro fall balls
    else:
        scene fembro fall
    with shift_eyes(False)

    $ thought_bubble(
        None, _("As you come to, it takes everything in you not to grind into [fembro_nouns[1]]."),
        _("At least I caught [fembro_nouns[1]].")
        )

    if fembro_penis:
        scene fembro fall balls back
    else:
        scene fembro fall back

    fembro.c "Are you alright?"

    $ thought_bubble(
        None, _("Your sigh warbles."),
        _("Pull it together! You're in the kitchen.")
        )

    "You came to apologize, and now look at you. Your cock is in the same place as last night."

    "The same, soft, warm, boun-"

    $ thought_bubble(
        None, _("You take a deep breath, and help [fembro.name] to [fembro_nouns[2]] feet."),
        _("No! focus.")
        )

    
    scene bg kitchen:
        background_art
    
    show fembro sad at fit, flip, set_place(6)
    #tired

    show main sad at fit, set_place(3)
    #nervous

    $ thought_bubble(
        fembro.c, _("I'm So Sorry!"),
        _("Alright, time to apolo-")
        )

    main.c "Wha- What for?"

    fembro.c "You hit your head, but you're so worried about me that you don't even care!"

    $ thought_bubble(
        None, _("Your hand brushes the back of your head. There is indeed a bruise."),
        _("Huh... Horny trumps pain it seems.")
        )

    main.c "Don't worry about it. I'm sturdy."

    fembro.c "It's not about that. You got hurt because of me."

    #show fembro sad

    $ thought_bubble(
        fembro.c, _("I keep messing things up..."),
        _("... That explains things.")
        )

    if fembro.dom:

        show main anger at fit

        show fembro sad at fit:
            subpixel True 
            set_place(6)
            easein2 0.10 set_place(5)
        with Pause(0.10)
        show fembro surprise at fit, set_place(5)

        "Frustrated, you pull [fembro_nouns[1]] over to you."
    
        main.c "[fembro.name], you're my [fembro_nouns[4]]."

        main.c "Stop feeling guilty, I want you to be safe."

        "You loosen your grip. [fembro_nouns[0]!c] feels so easy to break."

        show fembro non at fit, flip(1)

    else:

        main.c "[fembro.name], I'd rather get injured than let you get hurt."

        show fembro non at fit, flip(1)

        fembro.c "..."

        "At first worry that [fembro_nouns[0]]'ll panic at that. But... [fembro_nouns[0]] just stare at you."

        "Is [fembro_nouns[0]] intrigued? Amazed? Content? You can't tell."

        "Then, [fembro_nouns[0]] snaps out of it."
    
    fembro.c "O-okay."

    show main calm at fit

    hide fembro
    with easeoutleft

    "[fembro_nouns[0]!c] nods and smiles a little. Then [fembro_nouns[0]] rushes off, blushing."

    $ thought_bubble(
        None, _("You don't quite know what to make of this situation."),
        _("This is a win... Right?")
        )
    
    "But you're glad [fembro.name] isn't upset or hurt."

    $ persistent.replay_scenes.append('day_0201_reach_for_it')
    $ renpy.end_replay()

    $ fembro.stage = 21

    jump loc_kitchen

label day_0201_strike_a_pose:

    if ((not aunt.chosen) and (not _in_replay)):

        jump aunt_aunt_idle

    else:

        
        scene bg bed aunt:
            background_art
        
        show aunt anger at fit, flip, set_place(1.5)
        #Focused

        show main calm red at fit, flip, set_place(6)
        #impressed

        aunt.c "Hah!"

    $ thought_bubble(
        aunt.c, _("Yah"),
        _("Damn, she's thrashing that punching bag.")
        )

    "She stops the last punch before she hits the bag. The sweat from her arm splashes into it instead."

    main.c "Wow"
        
    show aunt surprise at fit
    #happy but surprised
        
    show main happy at fit, flip(1)
    #smiling

    aunt.c "Oh, howdy."

    main.c "Hey."
        
    show main calm no at fit, flip(1)

    if aunt.stage == 21:

        show aunt sad at fit
        #apologetic

        aunt.c "I really am sorry for earlier."

        if dominant:

            #show
            
            main.c "Hey, as long as you don't go as hard as you are on that punching bag, I should be fine."

            show aunt happy at fit
            #laugh

            aunt.c "Haha"
        
        else:

            main.c "It's fine, really."

            show aunt non at fit
            #blushing

            main.c "The kiss really did help..."

            "She blushes again."

    main.c "So are you training for anything?"

    show aunt surprise at fit
    #confused
    
    aunt.c "Huh?"

    main.c "Like a tournament or something?"

    show aunt happy at fit
    #smiling

    aunt.c "Nah, I just like exercising. Can't stand still for too long. You know?"

    $ thought_bubble(
        None, _("You understand the standing part. Usually because you like sitting after a while."),
        _("Lying down is nice too.")
        )

    show fembro sad at fit, flip, set_place(9)
    #nervous
    with easeinright

    pause 0.5

    show fembro surprise at fit, flip(1)
    #spooked

    aunt.c "Howdy, [fembro.name]"

    show fembro non at fit, flip(1)
    #calm

    show aunt non at fit
    #calm

    fembro.c "Ho-Howdy."

    "The lion meets the mouse."

    show fembro happy at fit, flip(1)
    #nervous smile, blush

    fembro.c "Auntie? Can you... Do the thing?"

    main.c "What thing?"

    show aunt happy at fit
    #proud

    aunt.c "Oh yeah, [main.name] hasn't seen my guns. Has he?"

    main.c "Oh, I never took you for a gun nut."

    aunt.c "Well then, let me show you."

    scene aunt show_off

    "[fembro.name] squees as [aunt.name]'s arms rise."
    
    $ thought_bubble(
        None, _("And although you're silent, you're very starstruck as well."),
        _("I've never seen muscles like that in person.")
        )

    "It's not just the size, but the definition that's impressive."

    if aunt.stage == 21:
    
        $ thought_bubble(
            None, _("To think those were the same arms that held you so tenderly."),
            _("The same arms that punched me...")
            )

    aunt.c "Enjoying the show, I see."

    "She makes her arm muscles bounce, and flexes her chest, making her breasts shift ever so slightly."

    "It's mesmerizing how she makes them move."
    
    $ thought_bubble(
        None, _("[fembro.name] whimpers with excitement."),
        _("Did [fembro_nouns[0]] cream [fembro_nouns[2]] shorts?")
        )
    
    "You don't blame them."
    
    "Her sweat glistening off her body entices you as well."

    scene bg bed aunt:
        blur 3
    
    show aunt non at fit, set_place(1.5)

    show main calm at fit, flip, set_place(6)

    show fembro sad at fit, flip, set_place(9)

    aunt.c "Alright you two. Eyes back in your skulls."

    "You blush, but [fembro.name] for once, is utterly shameless."
    
    $ thought_bubble(
        fembro.c, _("Aw... Can you do it again later?"),
        _("Wow... [fembro_nouns[0]]'s addicted.")
        )

    aunt.c "Maybe tomorrow. But I'll let you watch me work out."
    
    show aunt anger at fit, flip

    show fembro happy at fit, flip(1)

    show main calm at fit

    pause 0.1

    hide main
    with easeoutright

    "You realize you have important stuff to get to, but [fembro.name] accepts the invitation happily."

    $ persistent.replay_scenes.append('day_0201_strike_a_pose')
    $ renpy.end_replay()

    jump loc_bed_aunt

