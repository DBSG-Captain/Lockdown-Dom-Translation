define busy = {
    "lilsis": [],
    "bigsis": [],
    "fembro": [],
    "mom": [],
    "aunt": []
}

define scheduled = {
    "lilsis": {
    },
    "bigsis": {
    },
    "fembro": {
        "living_fembro": [[[1], [4, 5, 6]]],
        "kitchen_fembro": [[[2], [0, 1, 2, 3]], [[0], [4, 5, 6]]]
    },
    "mom": {
        "living_mom": [[[2], [4, 5, 6]]],
        "kitchen_mom": [[[3], [4, 5, 6]]]
    },
    "aunt": {
        "living_aunt": [[[2], [0, 1, 2, 3, 4]]],
        "kitchen_aunt": [[[0], [5, 6]], [[3], [5, 6]]]
    }
}

label bath_cabinat_idle:
    scene bg bath:
        background_art

    $ thought_bubble(
        None, _("Each person has a towel for every part of the body."),
        _("I only need one.")
        )

    jump loc_bath

label bath_sink_idle:
    scene bg bath:
        background_art

    $ thought_bubble(
        None, _("Migraine pills."),
        _("The family's greatest weapon.")
        )

    jump loc_bath

label toilet_idle:
    scene bg bath:
        background_art

    $ thought_bubble(
        None, _("Rather clean for a toilet."),
        _("I don't need to go.")
        )

    jump loc_bath

label shower_idle:
    scene bg bath:
        background_art

    $ thought_bubble(
        None, "There's no need.",
        "I have a dirty mind, but my body's clean."
        )

    jump loc_bath

label bath_fembro_idle:
    scene bg bath:
        background_art
    
    ""

    jump loc_bath

label bath_lilsis_idle:
    scene bg bath:
        background_art
    
    ""

    jump loc_bath

label bath_bigsis_idle:
    scene bg bath:
        background_art
    
    ""

    jump loc_bath

label bath_aunt_idle:
    scene bg bath:
        background_art
    
    ""

    jump loc_bath

label bath_mom_idle:
    scene bg bath:
        background_art
    
    ""

    jump loc_bath

label fembro_fembro_idle:
    scene bg bed fembro:
        background_art

    if (daytime == 0):
        
        show fembro disgust at fit, set_place(8)
        #Focused

        pause 0.5
        
        show main casual aware at fit, flip, set_place(3)
        with easeinleft

        "Wow..."

        $ thought_bubble(
            main.c, "How do you play like that?", 
            "That is not good gaming posture."
            )

        show fembro non at fit, flip

        fembro.c "Huh?"

        $ thought_bubble(
            main.c, "You're bent over. Your butt is almost higher than your head.", 
            "I'm not complaining, but..."
            )

        main.c "And you're still demolishing everyone else?"

        "[fembro_nouns[0]!c] has trouble looking you in the eyes."

        fembro.c "I just like standing like that."
        
        show fembro sad at fit
        
        fembro.c "I got used to it, I guess."

    elif (daytime == 1):
        
        show fembro happy at fit, flip(1)(), set_place(7)
        #Joyful

        pause 0.5
        
        show main casual calm at fit, flip, set_place(3)
        with easeinleft

        "It's nice to see [fembro.name] relaxing every once in a while."

        "Mom works [fembro_nouns[1]] pretty hard around the house."

    elif (daytime == 3):

        "You squeeze into bed beside [fembro.name]."

        if check_if_any_scenes("night"):
            call screen confirm_menu('sleep')
        else:
            $ sleep_night()

    jump loc_bed_fembro

label fembro_sisbf_idle:
    scene bg bed fembro:
        background_art

    ""

    jump loc_bed_fembro

label aunt_aunt_idle:
    scene bg bed aunt:
        background_art

    if (daytime == 0):
        
        show aunt non at fit, set_place(8)
        #Focused
        
        show main casual aware at fit, flip, set_place(3)
        with easeinleft

        "Wow..."

        $ thought_bubble(
            main.c, "How do you play like that?", 
            "That is not good gaming posture."
            )

        show fembro non at fit, flip

        fembro.c "Huh?"

        $ thought_bubble(
            main.c, "You're bent over. Your butt is almost higher than your head.", 
            "I'm not complaining, but..."
            )

        main.c "And you're still demolishing everyone else?"

        "[fembro_nouns[0]!c] has trouble looking you in the eyes."

        fembro.c "I just like standing like that."
        
        show fembro sad at fit
        
        fembro.c "I got used to it, I guess."

    elif (daytime == 1):
        
        show fembro happy at fit, flip(1)(), set_place(7)
        #Joyful

        pause 0.5
        
        show main casual calm at fit, flip, set_place(3)
        with easeinleft

        "It's nice to see [fembro.name] relaxing every once in a while."

        "Mom works [fembro_nouns[1]] pretty hard around the house."

    elif (daytime == 3):

        "You squeeze into bed beside [fembro.name]."

        call screen confirm_menu('sleep')

    jump loc_bed_fembro

label punchbag_idle:
    scene bg bed aunt:
        background_art

    "Now you know why [aunt.name] can knock people out."

    jump loc_bed_aunt

label workbench_idle:
    scene bg bed aunt:
        background_art

    "You bet [aunt.name] could bench press you easily."

    jump loc_bed_aunt

label kitchen_stove_idle:
    scene bg kitchen:
        background_art

    "You feel like cooking food."

    call screen confirm_menu("day00_good_cook")

label kitchen_fembro_idle:
    scene bg kitchen:
        background_art
        
    show fembro happy at fit, set_place(8)
    #Focused

    pause 0.5
    
    show main calm at fit, set_place(3)
    with easeinleft

    $ thought_bubble(
        fembro.c, _("Oh, hey [main.name], do you want me to cook something for you?"), 
        _("Huh... I didn't know [fembro.name] could cook.")
        )

    show fembro sad at fit
    #pout

    main.c "Nah, I'm good. Thanks anyway though."

    jump loc_kitchen

label kitchen_lilsis_idle:
    scene bg kitchen:
        background_art
    
    ""

    jump loc_kitchen

label kitchen_bigsis_idle:
    scene bg kitchen:
        background_art
    
    ""

    jump loc_kitchen

label kitchen_aunt_idle:
    scene bg kitchen:
        background_art
    
    if (daytime < 2):

        show aunt happy at fit, set_place(7)

        show main calm at fit, set_place(3)

        main.c "What's that white stuff you're putting in the eggs?"

        #show aunt big smile

        aunt.c "The shells."

        "You pause for a good while."

        #show aunt eyebrow raised

        aunt.c "Would you rather I eat it all raw."

        show main fear at fit

        "Your look of horror says it all."

        "You're pretty sure she's joking, but you don't want to test it."
        
    elif (daytime > 2):

        show aunt happy at fit, set_place(7), flip

        show main calm at fit, set_place(3)

        aunt.c "You're up pretty late."

        show main surprise at fit

        main.c "Oh, well..."

        #show aunt big smile

        aunt.c "Relax, you're a 'grown-up' now."

        show main calm at fit

        aunt.c "I'm not going to spank you or anything."

        aunt.c "Unless you want me to."

        if dominant:

            show aunt surprise at fit, set_place(7), flip

            main.c "I prefer to be the one doing the spanking."

            "She clears her throat and gets back to organizing the spices."

        else:

            "..."

            main.c "Good to know."

            "Your voice cracked."
 
    jump loc_kitchen

label kitchen_mom_idle:
    scene bg kitchen:
        background_art

    show mom phone annoy at fit(True, 7)

    show main calm at fit(False, 3)

    main.c "..."

    mom.c "..."

    "..."

    main.c "Hey mo-"

    $ thought_bubble(
        mom.c, "Do me a favor and go to bed, [main.name].", 
        "Oof"
        )
    
    jump loc_kitchen

label kitchen_sisbf_idle:
    scene bg kitchen:
        background_art
    
    ""

    jump loc_kitchen

label tv_idle:
    scene bg living:
        background_art
    
    "There's never anything good on TV, even now."

    jump loc_living

label living_fembro_idle:
    scene bg living:
        background_art

    show main calm at fit, right

    show fembro disgust at fit(True, 5)

    show mom disgust at fit, flip, set_place(3)

    "There's [fembro.name], still failing miserably to massage your mother."

    "You think [fembro_nouns[0]]'s making the stress worse..."

    show fembro surprise at fit, flip

    "When you step over, [fembro.name] pleads silently for you not to let Mom see you."

    show fembro sad at fit, flip(1)()

    "[fembro_nouns[0]!c] really wants to do a good job on [fembro_nouns[2]] own."

    "You're rooting for [fembro_nouns[1]]."

    show mom sad at fit, flip(1)()

    "And hoping Mom can survive."

    jump loc_living

label living_lilsis_idle:
    scene bg living:
        background_art
    
    ""

    jump loc_living

label living_bigsis_idle:
    scene bg living:
        background_art
    
    ""

    jump loc_living

label living_aunt_idle:
    scene bg living:
        background_art
    
    ""

    jump loc_living

label living_mom_idle:

    scene bg living:
        background_art
    
    show mom phone disgust at fit(False, 7)

    show main calm at fit(False, 3)

    mom.c "What is this ad."

    "Your mom's savvy enough to know that the internet is full of scams, but not aware enough to know they're fake."

    "She really believes that Nigerian princes are begging for money."

    "But she doesn't trust them to pay her back."

    show mom point annoy at fit(True)

    mom.c "[main.name], how do these people know where we live?"

    "!!!"

    main.c "What?!"

    show mom back calm

    mom.c "This ad a while back said there are desperate milfs in our area."

    mom.c "I asked [bigsis.name] what a milf was, and she said I was one."

    mom.c "Now the same ad is showing our town."

    show main annoy

    main.c "..."

    main.c "[bigsis.name], you suck!"

    bigsis.c "And swallow!"

    show mom phone fear at fit

    $ thought_bubble(
        mom.c, "How did they get our information?", 
        "I don't even know how to unpack this one."
        )

    show main at fit(True)
    with None

    hide main
    with easeoutleft

    jump loc_living

label breaker_idle:
    scene bg basement:
        background_art

    $ thought_bubble(
        None, _("This controls the power."),
        _("Now we're playing with power.")
        )

    jump loc_basement

label heater_idle:
    scene bg basement:
        background_art
    
    "What would you even need with this?"

    jump loc_basement

label laundry_idle:
    scene bg basement:
        background_art

    $ thought_bubble(
        None, _("Man, I'm a pervert."),
        _("We all know what you're thinking")
        )

    jump loc_basement

label basement_clutter_idle:
    scene bg basement:
        background_art
    
    $ thought_bubble(
        None, _("Too much stuff to sort through."),
        _("Is that a frog?")
        )

    jump loc_basement