label day_0101_waking_from_a_dream:
        
    if not _in_replay:
        $ thought_bubble(
            None, _("(Narration and Dialogue)"), 
            _("([main.name]'s Thoughts)")
            )
    
    camera:
        perspective True

    if _in_replay:
        ""


    scene black

    camera:
        subpixel True
        pos (21, -180) zpos -800.0 blur 30
        easein2 1.5 pos (0, 0) zpos 0.0 blur 0

    scene lilsis marker smirk
    with shift_eyes(False, 1.5)

    camera:
        pos (0, 0) zpos 0.0 blur 0
    
    pause 0.5
        
    if not _in_replay:
        $ lilsis = name_character(char_default_names["lilsis"], "lilsis")

    lilsis.c "Hehehe."

    main.c "Whah... [lilsis.name]?"

    scene lilsis marker oops

    lilsis.c "Oh, uh... morning [main.name]."

    main.c "What are you-?"

    $ thought_bubble(
        None, _("Your sister quickly rolls off the bed."), 
        _("A marker?")
        )

    scene bg bed ian:
        background_art
        
    camera:
        subpixel True pos (-5, -86) zpos -700.0

    show main underwear surprise at fit(False, 4)
    #Shocked, just waking up, maybe groggy

    show lilsis pajama surprise lift at fit(True, 6)
    #Surprised that he woke up, but not shocked

    pause 0.5
    camera:
        subpixel True
        pos (-5, -86) zpos -700.0
        easein2 0.10 pos (0, 0) zpos 0.0
    show main fear at flip:
        subpixel True 
        set_place(4)
        easein2 0.10 set_place(1)
    with Pause(0.20)
    camera:
        subpixel True pos (0, 0) zpos 0 zoom 1.0
    show main fear:
    #Upset and trying to figure out what happened to his face
        set_place(1)

    $ thought_bubble(
        main.c, _("Argh, great! Really mature [lilsis.name]!"), 
        _("Again with the pranks?!")
        )

    $ thought_bubble(
        None, _("You move carefully to not expose your underwear."), 
        _("I hope she didn't see the wet spot.")
        )

    show lilsis smug hip:
    #Smug and arrogant grin
        subpixel True 
        set_place(6)
        easein2 0.10 set_place(7)
    with Pause(0.10)
    show lilsis smug:
        set_place(7)

    lilsis.c "Oh no, it's super childish. Still funny though. " 

    show main at fit
    #Frustrated and upset, but not raging.

    main.c "What did you draw? How bad is it?"

    lilsis.c "What's the fun if I tell you?"

    $ thought_bubble(
        None, _("You give up on covering."), 
        _("That's it!")
        )

    
    show lilsis:
        subpixel True 
        set_place(7)
        easein2 0.10 set_place(9)
    show main anger:
    #Rage
        subpixel True 
        set_place(1)
        easein2 0.30 set_place(5)
    with Pause(0.30)
    show lilsis:
        set_place(9)
    show main anger:
        set_place(5)

    show lilsis happy at fit(False)
    #Big, self-satisfied, smug smile.

    "You lunge at her, but She's already heading out the door."

    lilsis.c "Catch me if you can!"

    show main fear erect
    #blushing in surprise at his own horniness.

    $ thought_bubble(
        None, _("She says, slapping her ass to mock you."), 
        _("That shouldn't be turning me on.")
        ) 

    show main anger soft
    #Angry again

    hide lilsis
    with easeoutright

    main.c "Get back here!"

    hide main
    with easeoutright

    hide lilsis

    $ persistent.replay_scenes.append('day_0101_waking_from_a_dream')
    $ renpy.end_replay()

    call screen bed_main_nav

label day_0101_getting_got:

    camera:
        perspective True

    scene bg stairs:
        background_art

    "You stumble into the hall, pulling on your clothes."

    $ thought_bubble(
        None, _("You rush to the restroom."), 
        _("Let's see the damage...")
        )

    scene door bath steam

    "You don't notice that the restroom is steamy."

    "You look in, and..."

    scene bigsis shower p1

    pause(0.7)

    scene bigsis shower p2
        
    if not _in_replay:
        $ bigsis = name_character(char_default_names["bigsis"], "bigsis")

    scene bigsis shower p3

    bigsis.c "Stupid, tiny towels."

    scene bigsis shower p4

    $ thought_bubble(
        None, _("You can't rip your eyes away from those massi-"), 
        _("...")
        )

    if dominant:

        scene bg stairs:
            background_art

        show main underwear surprise at fit(False, 4)
        #snapping out of the horny trance

        show bigsis towel anger at fit(True, 7)
        #Indignant and annoyed, angry

        $ thought_bubble(
            bigsis.c, _("The Fuck!?"), 
            _("Oh Shit!")
            )

        window auto hide
        show main fear:
            subpixel True 
            set_place(4)
            easeout2 0.4 set_place(2)
            easeout2 0.6 set_place(4)
        show bigsis up:
            subpixel True 
            set_place(7)
            easeout2 0.4 set_place(5)
            easein2 0.6 set_place(7)
        with Pause(1.0)
        show main red:
            set_place(4)
        show bigsis point:
            set_place(7)
        window auto show

        $ thought_bubble(
            None, _("You just manage to dodge."), 
            _("She's getting faster.")
            )

        bigsis.c "Don't sneak up on me, bitch!"

        hide bigsis
        with easeoutright

        $ thought_bubble(
            None, _("[bigsis.name] finishes getting dressed right in front of you."), 
            _("Why does she never care that I'm right here?")
            )

        show bigsis calm cross at fit(True, 8)
        #Completely unconcerned with him.
        with easeinright

        main.c "Hey, I'm sorry! I didn't know you were in there."

        bigsis.c "Tsh"

    else:
        
        scene bigsis shower kick
        with vpunch

        main.c "Agh!"

        if kink_ballbusting:

            "Before you can react, there's a foot firmly planted in your crotch."

            "Your legs give out underneath you, unable to stand after such a devastating strike."
        
            "Seems like [bigsis.name]'s getting rusty..."

            "Thankfully."

        scene bg stairs:
            background_art

        show main underwear disgust at fit(False, 4)
        #pain

        show bigsis towel calm at fit(True, 7)
        #annoyed at worst

        bigsis.c "That's what you get for barging in."

        $ thought_bubble(
            bigsis.c, _("And this!"), 
            _("Wha-")
            )

        window auto hide
        show main surprise:
        #pain
            subpixel True 
            set_height(1.5)
            easeout2 0.4 set_height(1.5)
            easeout2 0.6 set_height(1.65)
        show bigsis anger:
            subpixel True 
            set_place(7)
            easeout2 0.4 set_place(5)
            easein2 0.6 set_place(7)
        with Pause(1.2)
        show main fear:
        #pain
            set_height(1.65)
        show bigsis annoy:
            set_place(7)
        window auto show

        if kink_ballbusting:

            "Even now, you're not safe. She hooks her foot passed your hand, hitting the underside of your balls."

        main.c "Fu-huck"

        hide main
        with easeoutbottom

        if kink_ballbusting:

            "Alright. Not rusty. She's Stainless steel."

        bigsis.c "That's for sneaking up on me."

        hide bigsis
        with easeoutbottom

        show bigsis annoy cross at fit(True, 7)
        #Completely disinterested
        with easeinbottom

        "She finishes drying herself as you writhe in pain."

        show main underwear sad at fit(False, 4)
        #woozy
        with easeinbottom

        "By the time you get up, [bigsis.name]'s already dressed."
    
    show main sad no at fit
    #Upset at the situation

    main.c "Where did [lilsis.name] go?"
    
    show bigsis calm
    #Doesn't care

    bigsis.c "Hoe ran off to the shrimp's room."

    main.c "Thank. Also, what did she draw on my face!?"
    
    show bigsis annoy at fit(False)
    #Rolling eyes

    bigsis.c "Are you a fucking idiot?"
    
    hide bigsis
    with easeoutright

    "Before you have time to respond, she goes back into the restroom, leaving the door cracked."
    
    show main anger at fit(True)

    $ thought_bubble(
        main.c, _("{i}Sigh{/i}"), 
        _("Classic [bigsis.name].")
        )

    hide main
    with easeoutleft

    $ go_down = False

    $ persistent.replay_scenes.append('day_0101_getting_got')
    $ renpy.end_replay()

    jump loc_stairs

label day_0101_help_from_addy_1:

    camera:
        perspective True

    scene bg bed fembro:
        background_art

    with None

    show main underwear anger at fit, flip, set_place(7)
    with easeinright

    "You don't even bother knocking, nobody does for-"

    scene fembro stuck pull

    "!!!"

    if not _in_replay:
        $ fembro = name_character(char_default_names["fembro"], "fembro")

    $ choice_done_fembro = False

    if _in_replay:
        jump day_0101_help_from_addy_2
    else:
        jump change_fembro

label day_0101_help_from_addy_2:

    scene fembro stuck pull

    $ choice_done_fembro = True
    
    fembro.c "[main.name]?!"

    $ thought_bubble(
        None, _("..."), 
        _("{i}ASS{/i}")
        )

    fembro.c "I am so sorry."

    "..."

    main.c "Why are you apologizing?"

    $ thought_bubble(
        fembro.c, _("I'm... mooning you..."), 
        _("... I'll take the pass.")
        )
    
    fembro.c "I was getting dressed, b-but these shorts won't fit anymore."

    "As [fembro_nouns[0]] pull on the shorts, [fembro_nouns[2]] booty jiggles."
    
    "You barely manage to turn your head to be polite, but you don't manage to look away."

    scene bg bed fembro:
        background_art

    show main underwear sad erect red at fit, flip, set_place(7)
    #blushing

    show fembro sad at fit, set_place(3)
    #pout

    $ thought_bubble(
        None, _("[fembro.name] finally manages to put them on."), 
        _("Like squeezing a cantaloupe into a sock.")
        )

    show main soft no at fit, flip(1)
    #blushing

    main.c "Hey [fembro.name], tell me."

    main.c "What did [lilsis.name] draw on my face?"

    show fembro happy at fit
    #show fembro blush

    $ thought_bubble(
        fembro.c, _("I don't see anything except how handsome you are.."), 
        _("Classic [lilsis.name].")
        )

    main.c "Where is she now."

    show fembro fear at fit
    #timid looking to the side.

    fembro.c "I... don't know"

    main.c "[fembro.name], I know she's here. And you suck at lying."
    #sigh

    fembro.c "I told her that when she came in here."

    show fembro surprise at fit
    #panic
    
    $ thought_bubble(
        bigsis.c, (_("Hey [main.name] and pin dick, mom wants you both.") if fembro_penis else _("Hey [main.name] and zit tits, mom wants you both.")), 
        _("Well shit, [lilsis.name] will have to wait.")
        )

    show main disgust at fit, flip

    lilsis.c "Don't talk to [fembro_nouns[1]] like that, hoe."

    bigsis.c "I will rend your soul from your body, bitch!"

    hide main
    hide fembro
    with easeoutright

    $ go_down = True

    $ persistent.replay_scenes.append('day_0101_help_from_addy_1')
    $ renpy.end_replay()

    jump loc_stairs

label day_0101_mom_the_dom:

    camera:
        perspective True

    scene bg living:
        background_art

    "You rush down the stairs, but your mom isn't anywhere in sight."

    show fembro fear at fit, flip, set_place(7)
    #worried

    show main sad at fit, flip, set_place(5)
    #Tired
    with easeinright

    main.c "Ugh, where is she?"

    show main annoy at fit, flip
    #annoyed

    fembro.c "Don't let her hear-"

    show mom annoy at fit, set_place(3) behind main
    #raised eyebrow
    with easeinleft

    show fembro surprise at fit, flip(1)
    #cringing at mom about to moshinderu Ian

    main.c "[fembro.name], I'm so pissed right now, I don't care if she hears me."

    scene mom grab collar

    if not _in_replay:
        $ mom = name_character(char_default_names["mom"], "mom")

    $ thought_bubble(
        mom.c, _("Excuse me?"), 
        _("Well... shit.")
        )

    "Her cold voice shocks your ego back to reality."

    if dominant:

        main.c "... I was talking about... [bigsis.name]?"

    else:

        main.c "... I'm sorry?"

    "..."

    mom.c "Go help your aunt with her bags."

    if dominant:

        main.c "... Sure..."

    else:

        main.c "Yes ma'am"
    
    $ thought_bubble(
        mom.c, _("And move them to your room, you'll be staying with [fembro.name]"), 
        _("What?!")
        )

    mom.c "We already cleared out your room this morning. You're welcome."

    main.c "But-"

    if (not dominant and kink_ballbusting):

        scene mom grab balls
        with CropMove(0.2, "wipeup")

        "She already has her hand cupped around your balls."

        "She squeezes down, and you almost faint."

        main.c "Ugh! Okay, I get it."

        "She crushes one between her thumb and index finger, and the other between her fingers and palms."

        mom.c "Try again."

        "Her stern, cold delivery tells you she won't have mercy again."

        "Your balls already hurt from [bigsis.name]'s kick. Now you're about to cry."

        main.c "Thank you for cleaning out my room Mommy, I'll do whatever you say!"

        mom.c "Good boy. Though, the 'mommy' part was a bit much..."

        "She cringes as she wipes her hand on your shirt."

    else:

        mom.c "Listen, [main.name]. If I say your aunt gets your room, your aunt gets your room."

        mom.c "Now suck it up and get her bags."

    scene bg living:
        background_art

    show mom calm at fit, set_place(1)
    #annoyed

    show fembro sad at fit, flip, set_place(5)
    #Cowering

    show main fear at fit, flip, set_place(7)
    #pain

    "You stumble back as she lets go."

    mom.c "Where are your sisters?"

    main.c "They're upstairs."

    mom.c "[fembro.name], go get them."

    fembro.c "I'd rather not. They're fighting, pretty heated too..."

    pause 1.0

    show mom annoy at fit:
    #raised eyebrow
        subpixel True 
        set_place(1)
        easein2 1.00 set_place(2) 
    camera:
        subpixel True 
        zpos 0.0 
        easein2 1.0 zpos -300.0 
    with Pause(2.0)
    show mom annoy at fit:
    #raised eyebrow
        set_place(2)
    camera:
        zpos -300.0 

    mom.c "... And you're so scared of them that won't do what {i}I{/i} say?"

    "It was at that moment, [fembro.name] knew,"

    show fembro surprise at fit, flip(1)
    #Panic

    show mom calm
    #resting bitch

    "[fembro_nouns[0]!c] fucked up."

    fembro.c "Oh gosh, of course, ma'am. I'll go take care of that!"

    hide fembro
    with easeoutright

    camera:
        subpixel True pos (0, 0) zpos 0

    $ thought_bubble(
        None, _("[fembro_nouns[0]!c] scurries away like a rabbit from a fox."), 
        _("Classic [fembro.name].")
        )

    show mom disgust
    #roll eyes

    mom.c "God, [fembro_nouns[0]]'s pathetic."

    show mom annoy
    #resting bitch

    "Your mom looks at you and scoffs."

    mom.c "And you... Go make yourself useful and get your aunt's bags!"

    hide main
    with easeoutleft

    scene black

    $ thought_bubble(
        None, _("You stumble back."), 
        _("OW")
        )

    mystery "Don't pile drive me yet, I just got here."

    scene aunt intro stand

    if not _in_replay:
        $ aunt = name_character(char_default_names["aunt"], "aunt")

    $ thought_bubble(
        aunt.c, _("Heya."), 
        _("Thank the lord above.")
        )

    main.c "Hey auntie. What's up."

    aunt.c "Just getting myself moved in."

    "She stretches her back."

    scene bg living:
        background_art
    
    show main sad at fit, flip, set_place(7)

    show aunt happy at fit, set_place(2)

    main.c "I better hurry with the boxes, otherwise mom will-"

    show aunt surprise at fit
    #sympathy

    aunt.c "Yeah, [mom.name]'s a beast. Been like that since I was born."

    $ thought_bubble(
        aunt.c, _("She's the only person that can scare me, to be honest."), 
        _("Classic Mom.")
        )

    show main calm
    #annoyed

    "You sigh"
    
    main.c "I'll go get your bags."

    show aunt happy at fit
    #Charming smile

    "She puts on an old southern lady voice and pulls on the ends of her eyes to give herself crows-feet."

    show main happy
    #laughing

    aunt.c "Well thank you kindly, youngster, for helping your old, helpless auntie with her bags."
    
    main.c "'Tis a pleasure."
    
    "You head to the car with a laugh."

    hide main
    with easeoutleft

    jump day_0101_getting_the_bags

label day_0101_getting_the_bags:

    scene ian box

    $ thought_bubble(
        None, _("You come back from the car hefting boxes... Like your mom told you to..."), 
        _("Damn, I feel like a wuss.")
        )

    ""

    if dominant:

        $ thought_bubble(
            None, _("No!"), 
            _("I hate this.")
            )
        
        "You aren't going to let your mom or anyone else push you around!"

        "Things have got to change around here..."

        "And you're going to change them."

    else:

        "Welp, Better make the best of it."

        "It's not like you'll ever like it but..."
        
        "... You don't like it... Do you?"
    
    "..."

    pause 1

    $ persistent.replay_scenes.append('day_0101_mom_the_dom')
    $ renpy.end_replay()

    jump day_0101_the_news_1

label day_0101_the_news_1:

    camera:
        perspective True

    scene ian box

    $ thought_bubble(
        None, _("What's in these boxes, weights?"), 
        _("Actually, that would make sense.")
        )

    "You carry the box to the living room, but you find yourself in the middle of a sibling spat."

    scene bg living:
        background_art

    show main sad at fit, set_place(4)
    #tired
    
    show fembro anger at fit, flip, set_place(6)
    #trying to be assurtive

    show lilsis annoy at fit, set_place(1)
    #irritated with the arguing

    show bigsis at fit, flip, set_place(9)
    #gives 0 shits

    $ thought_bubble(
        fembro.c, _("Guys, let's quiet down a bit. [main.name]'s upset cause mom's making him bunk with me."), 
        _("Like that would work.")
        )

    show lilsis smug
    #rubbing it in

    lilsis.c "RIP Nii-chan."

    show bigsis anger at fit, flip:
    #annoyed
        subpixel True 
        set_place(9)
        easein2 0.30 set_place(8)
    show fembro sad at fit, flip(1):
    #cowering
        subpixel True 
        set_place(6, 1.5)
        easein2 0.30 set_place(5, 1.55)
    camera:
        subpixel True 
        zpos 0.0 
        easein2 0.30 zpos -100.0 
    with Pause(0.30)
    show bigsis at fit, flip:
        set_place(8)
    show fembro at fit, flip(1):
        set_place(5, 1.55)
    camera:
        zpos -100.0

    $ thought_bubble(
        bigsis.c, _("No one asked your opinion, shrimp."), 
        _("Here we go again")
        )

    show lilsis anger at fit:
    #angry
        subpixel True 
        set_place(1)
        easein2 0.30 set_place(3)
    show fembro at fit, flip:
        subpixel True 
        set_place(5, 1.55)
        easein2 0.30 set_place(5, 1.6)
    camera:
        subpixel True 
        zpos -100.0 
        easein2 0.30 zpos -200.0 
    with Pause(0.30)
    show lilsis at fit:
        set_place(3)
    show fembro at fit, flip:
        set_place(5, 1.6)
    camera:
        zpos -200.0 

    lilsis.c "Actually, I did. Is that a problem!?"

    show bigsis at fit, flip:
    #anger
        subpixel True 
        set_place(8) 
        easein2 0.30 set_place(7)
    show fembro at fit, flip(1):
        subpixel True 
        set_place(5, 1.6)
        easein2 0.30 set_place(5, 1.65)
    camera:
        subpixel True 
        zpos -200.0 
        easein2 0.30 zpos -300.0 
    with Pause(0.30)
    show bigsis at fit, flip:
        set_place(7)
    show fembro at fit, flip(1):
        set_place(5, 1.65)
    camera:
        zpos -300.0 

    bigsis.c "[lilsis.name], You are a fucking-!"

    "'INCEST LEGALIZED NATIONWIDE'"

    show main surprise at fit, flip

    show fembro surprise at fit, flip
    #Shocked

    camera:
        pos (0, 0) zpos -400

    "What..."

    show lilsis surprise at fit, flip

    camera:
        pos (0, 0) zpos -500

    "The..."

    show bigsis surprise at fit, flip(1)

    camera:
        pos (0, 0) zpos -600

    "Fuck?!?!?!"

    scene news incest legal

    camera:
        pos (0, 0) zpos 0

    "[aunt.name]'s watching TV behind you. Even she can't hide her shock."

    "Everyone gathers in the living room. The news anchor goes on about the court case."

    "'Any non-vaginal sex act between consenting adults is legal, regardless of familial relation.'"

    scene bg living:
        background_art

    show main fear red at fit, set_place(3)

    show lilsis surprise red at fit, flip, set_place(7)

    "Then, your eyes meet [lilsis.name]'s."

    "There's an awkward energy between you."

    show lilsis fear at fit, flip(1)

    "She looks down and rushes out of the room, blushing."

    hide lilsis
    with easeoutright

    show main blush erect at flip, set_place(5)
    with easeinleft
    #Horny

    "For the first time, your mind wanders to thoughts you always pushed away."

    "You were aware that your sisters, and even your mom, were attractive..."
        
    "But it was always in an abstract sense."
        
    "But now-"

    show main calm soft

    show fembro sad at fit, set_place(3)
    with easeinleft
    #Blush Shock

    fembro.c "WHAT?! How can... what does... Huh?!"

    show bigsis annoy at fit, flip, set_place(7)
    #annoyed
    with easeinright

    bigsis.c "And the whole of Alabama rejoiced."

    mom.c "I don't have time for this."

    "Your mother, seemingly unfazed, goes to your room to prepare it for your aunt."

    bigsis.c "I already have a boyfriend. Not that any of you had a chance."

    show bigsis smug at fit, flip(1)
    #smug

    bigsis.c "But if you beg, I'll let you watch."

    show fembro surprise red at fit

    fembro.c "What?"

    show bigsis blush at fit, flip(1)
    #blush

    bigsis.c "I know your bed is up against my wall, [fembro.name]. I bet you lean in and listen. Might as well get a show too."

    fembro.c "[bigsis.name]! I-I would never-"

    show bigsis anger at fit, flip(1)
    #frustrated

    $ thought_bubble(
        bigsis.c, _("Ugh. You fucking idiot. I swear, satire is dead."), 
        _("That's not how satire works.")
        )

    show fembro sad no at fit
    
    $ thought_bubble(
        fembro.c, _("That's not how satire works."), 
        _("Wait... will I have to listen to... that while I'm sleeping.")
        )

    show bigsis annoy at fit, flip(1)
    #Dissmissive

    $ thought_bubble(
        bigsis.c, _("I'll say when I want your opinion, midget."), 
        _("Wait... will me and [fembro.name] have to share a bed?")
        )

    "Just then, there's a knock on the door."

    show bigsis happy at flip, flip(1)
    #happy

    bigsis.c "Speaking of my beau."

    if not _in_replay:
        $ sisbf = name_character(char_default_names["sisbf"], "sisbf")

    if dominant:

        $ thought_bubble(
            None, _("You go to the door to let him in."), 
            _("Hey, it's [sisbf.name]. Who doesn't like [sisbf.name]?")
            )

    else:
    
        bigsis.c "[main.name], go get the door."

        main.c "I'm no-"

        mom.c "[main.name], go get the door."

        "You go get the door."

    hide fembro
    with easeoutright
    
    show main calm at fit:
        subpixel True 
        set_place(5)
        easein2 0.70 set_place(0)
    with Pause(0.70)
    show main calm at fit:
        set_place(0)

    show sisbf at fit, set_place(2)
    with easeinleft
    #Smile
    
    show main calm at fit:
        subpixel True 
        set_place(0)
        easein2 0.70 set_place(6)
    with Pause(0.70)
    show main happy at fit:
    #Smile
        set_place(6)

    sisbf.c "Howdy, brother."

    main.c "Sup [sisbf.name]?"

    "[sisbf.name] has a way of raising everyone's mood when he's around."

    show sisbf blush at fit

    show bigsis blush at fit, flip(1)

    bigsis.c "Hey, you handsome devil."

    sisbf.c "Hey, you beautiful angel."

    $ thought_bubble(
        None, _("He blows her a kiss, and she flashes her tongue."), 
        _("Odd, I'd think he was the angel and her the devil.")
        )

    show bigsis happy at fit, flip(1)

    show lilsis happy at fit, flip, set_place(4)
    #Super excited
    with easeinright

    show sisbf happy at fit

    lilsis.c "[sisbf.name]! OMG!"

    "[lilsis.name] bounds over and hugs him. Of course, he returns the embrace."

    show mom happy at fit, set_place(9), flip
    #calm and happy
    with easeinright

    mom.c "Oh, [sisbf.name]. Always good to see you. You're looking well."

    "That's the first time in a long time your mom has complimented someone."

    "That someone was also [sisbf.name]."

    mom.c "What brings you here?"

    show sisbf surprise at fit behind bigsis
    #Surprised

    sisbf.c "[bigsis.name] didn't tell you, Ma'am?"

    show bigsis at fit:
    #Attitude
        subpixel True 
        set_place(7)
        easein2 0.50 set_place(1) 
    with Pause(0.60)
    show bigsis calm at flip(1):
        set_place(1)

    bigsis.c "[sisbf.name]'s staying here for a while. His place has a hole in the roof."

    show mom surprise at fit
    #raises eyebrow

    show sisbf fear at fit

    mom.c "That's news to me."

    "[bigsis.name] hugs [sisbf.name] passionately."

    bigsis.c "He would do the same for us."

    show lilsis annoy at fit, flip

    lilsis.c "Please? We can't just leave him homeless!"

    show mom disgust at fit
    #dismissive

    "[mom.name] rubs her temples."

    show lilsis smile at fit, flip

    show main annoy at fit
    #annoyed

    show sisbf happy at fit

    mom.c "Ugh, alright. But he stays in [fembro.name]'s room, not yours [bigsis.name]."

    fembro.c "Yay!"

    show sisbf calm at fit

    show main anger at fit
    #annoyed

    main.c "Aw, come on! Three of us in one room?"

    aunt.c "Better get comfy. They've issued another lockdown. We'll be stuck together for a while."

    show main anger at flip(1)

    main.c "You inhale, holding back your frustration as best you can."

    "You storm off upstairs."

    hide main
    with easeoutright

    #show mom eye roll

    if dominant:

        "You don't want to say something you'll regret."

    else:

        "You know better than to talk back, at least."
        
        mom.c "Ugh, drama queen."

    $ persistent.replay_scenes.append('day_0101_the_news_1')
    $ renpy.end_replay()

    jump day_0101_the_news_2

label day_0101_the_news_2:

    $ choice_done_family = False

    $ choice_done_fembro = True

    jump disable_question

label day_0101_what_now:

    $ intro = False
    
    $ choice_done_family = True

    scene bg stairs:
        background_art

    "You can't take this."
    
    "You remove yourself to calm down"

    "You should just take a shower. Those help you calm down."

    $ add_scene(
        "day_0102_no_respect_at_all",
        [0],
        'shower',
        True,
        lilsis
        )

    $ add_scene(
        "day_0102_how_to_deal_with_mom",
        [1],
        'living',
        False,
        mom
        )

    $ add_scene(
        "day_0102_help_auntie",
        [2],
        'bed_aunt',
        False,
        aunt
        )

    $ add_scene(
        "day_0103_prepare_for_rest",
        [3],
        'stairs',
        False,
        None
        )

    $ add_scene(
        "day_0103_sleep_night_1",
        [3],
        'fembro_fembro',
        True,
        [fembro, bigsis]
        )

    jump loc_stairs