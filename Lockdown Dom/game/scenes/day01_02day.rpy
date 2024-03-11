label day_0102_no_respect_at_all:

    scene bg bath:
        background_art

    show main underwear at fit(True, 6)

    "As you strip down for your shower, contemplate your situation."

    "You start with your sister [lilsis.name]."

    "She's annoying, but not malicious, not cruel, and not really even mean."

    "She never moved past her 'bother others for the fun of it' phase, but has only become more entitled."

    "She plays you like a fiddle. Or better yet, plays with you like a toy."

    if lilsis.dom:

        "If only there were a way to get her to respect you more."

        "Maybe even get her to be your plaything for once."

    else:

        "You wouldn't mind being her plaything if it weren't so annoying."

    $ thought_bubble(
        None, _("..."), 
        _("Did I just think that?")
        )

    "*SLAM*"

    show lilsis smug at fit(False, 3)
    with easeinleft

    lilsis.c "Alright, Out. I've got t-"

    show lilsis surprise red

    $ thought_bubble(
        None, _(""), 
        _("She's just standing there, staring...")
        )

    "You thought she barged in here to pester you in some way, but..."

    "You follow her eyes to see where she's looking."

    scene lilsis cock shock
    with dissolve

    $ thought_bubble(
        None, _(""), 
        _("Is she staring at my crotch!?")
        )

    if dominant:

        "Well, that's new."

    else:

        "You resist the urge to cover yourself."

    "There's a different energy now. The tension has turned sexual."

    lilsis. c "I... uh"

    $ thought_bubble(
        None, _("She's your sister, she's seen you in your underwear before."), 
        _("What's Changed?")
        )

    "Could it be that... seeing the news has her looking at you differently. And so much differently?"

    "Whatever it is, you've both stood in silence long enough to make it awkward."

    if lilsis.dom:

        main.c "You know, some say it's rude to stare."

        lilsis.c "Huh?"

        main.c "You're gawking at my cock."

        lilsis.c "No, I-"

        main.c "It's all good. I don't mind giving you a show."

        lilsis.c ""
    
    else:

        main.c "[lilsis.name], are you..."

        lilsis.c "Huh? No! I'm not staring at anything!"

        "You were going to ask if she was alright, but never mind."

        main.c "I mean, it's alright if you wanna look. It doesn't bother me."

    lilsis.c "..."

    "She considers what you said carefully..."

    "Looks back at your crotch for a solid 5 seconds..."

    "Then slowly turns and walks to her room. The look of shock still plastered on her face."

    "Perhaps you went too far."

    scene bg bath:
        background_art

    show main underwear at fit(True, 6)

    "..."

    if _in_replay:
        jump day_0102_the_touch

    $ set_time(1)

    $ add_scene(
        "day_0102_the_touch",
        [1],
        'bed_lilsis',
        False,
        lilsis
        )

    $ lilsis.stage = 11

    jump loc_stairs

label day_0102_the_touch:

    if ((not lilsis.chosen) and (not _in_replay)):

        jump loc_bed_lilsis

    else:

        scene bg stairs:
            background_art

        $ thought_bubble(
            None, _("As you head out of the restroom, a moan comes from [lilsis.name]'s room."), 
            _("No way...")
            )

    scene lilsis masturbation peak
    with dissolve

    $ thought_bubble(
        None, _("Her eyes are glued to her phone, her hand to her crotch"), 
        _("Holy fuck.")
        )

    "Her movements are smooth and slow, rhythmic."

    "You'd think she was brushing her hair if it weren't for her moans."

    "Soft, sweet moans flow out of the room."

    "They're nothing like porn moans. Those seem fake in comparison."

    "But there is a forced element to hers as well."
    
    "She's holding them back. Most likely so no one can hear her."

    "Guess she didn't think about anyone seeing her."

    scene lilsis masturbation peak climax

    mystery "'Nii-chan!'"

    "She almost dropped the phone trying to turn it down."

    scene lilsis masturbation peak

    $ thought_bubble(
        None, _("So, she's watching incest porn?"), 
        _("She's such a weeb.")
        )

    lilsis.c "Stupid... [main.name]..."

    $ thought_bubble(
        None, _("..."), 
        _("!!!")
        )

    "This was already an overstimulating experience."

    "But the knowledge that you're the reason she's doing this..."

    "It took a lot for you not to start jerking off then and there."

    lilsis.c "With his... stupid fat cock..."

    "She slowly loses the frustrated edge, which gives way to a lustful rasp."

    "Your breath almost matches hers as you try to hold back gasps."

    lilsis.c "And his stupid... kissable lips... And..."

    scene lilsis masturbation peak climax

    "She inhales sharply. She's climaxing."

    "You swallow hard and make yourself scarce before she turns around and sees your massive erection."

    if _in_replay:
        jump day_0102_caught_in_the_act

    $ lilsis.stage = 12

    $ add_scene(
        "day_0102_caught_in_the_act",
        [1],
        'stairs',
        False,
        None
        )
    
    jump loc_stairs

label day_0102_caught_in_the_act:

    scene bg stairs:
        background_art

    show main fear at fit(False, 3)

    show bigsis disgust cross at fit(True, 7)
    #disgust

    $ thought_bubble(
        None, _("You turn around, [bigsis.name]'s standing there judging you."), 
        _("Shit!")
        )

    show bigsis annoy
    #bored and disinterested

    bigsis.c "Relax, I'm not gonna rat. I'll just remind her to close her door."

    show main calm
    #relief

    main.c "... Thanks..."

    if (bigsis.chosen or _in_replay):

        show main fear red
        #blush

        show bigsis blush
        #teasing

        bigsis.c "You know the invite I gave [fembro.name] is open to you too. Right?"

        if (kink_cuck and not bigsis.dom):

            show main sad
            #blush

            "You blush, and she reads you like a book."

            bigsis.c "I mean, not tonight. You'd just have to listen through the walls tonight. But perhaps another..."

            "You fidget a little."

            show bigsis smug
            #smug

            bigsis.c "Have fun jerking off tonight."

            show bigsis at fit(False)

            "She leaves with a sway in her hips."

        else:

            show main annoy
            #passive

            main.c "I prefer the real thing to watching."

            show bigsis annoy
            #annoyed

            "She scoffs."

            bigsis.c "Like hell you'll ever get this."

            show main smug
            #smug
            
            show bigsis surprise red
            #blushing

            main.c "I never said with you. You made that connection by yourself."

            "She blushes slightly then scoffs again."

            show bigsis anger
            #rage

            bigsis.c "Whatever. Have fun jerking off tonight creep."

            show bigsis at fit(False)

            $ thought_bubble(
                None, _("She leaves with a huff."), 
                _("Wow, I actually flustered her. Is that a win?")
                )
    

    hide bigsis
    with easeoutright

    pause 0.3

    "You sigh and head to the stairs."
    
    $ persistent.replay_scenes.append('day_0102_no_respect_at_all')
    $ renpy.end_replay()

    jump day_0102_nothing_to_do_for_a_while

label day_0102_nothing_to_do_for_a_while:

    scene bg stairs:
        background_art

    "As you head away from the door, you get an email on your phone."

    $ thought_bubble(
        None, _("It's from work."), 
        _("Shit.")
        )

    "Until this wave of the pandemic is under better control, the restaurant you work at is closing again."

    $ thought_bubble(
        None, _("There goes your income."), 
        _("Great.")
        )

    if _in_replay:
        jump day_0102_how_to_deal_with_mom

    jump loc_stairs

label day_0102_how_to_deal_with_mom:

    if ((not mom.chosen) and (not _in_replay)):

        jump loc_living

    else:

        scene bg living:
            background_art

        show main sad at fit(True, 5)

        "You sigh."

    if mom.dom:

        "If you're going to finally stop being your mom's throw rug, you have to think this through."

        "She's, by far, the least likely to ever give you respect."

        "Maybe if you learn more about her personally, you can find something, anything, to work with."

        "But she's so tense all the time. If you just go asking her, she'll get annoyed."

        "... Isn't [fembro.name] giving her a massage right now?"

    else:

        "Well, now that you lost your job, you're going to be broke for a while."
        
        "You should probably ingratiate yourself to your mom."

        "At least that way she won't give you hell for it."

        "Heck, she might even be nicer to you."

        "... [fembro.name] usually gives her a massage around this time."
        
    $ thought_bubble(
        None, _("Perfect opportunity to get some dirt!" if mom.dom else "Great chance to show how useful you can be!"), 
        _("Won't be too bad to feel her legs either.")
        )

    if _in_replay:
        jump day_0102_rubbing_and_prying

    $ add_scene(
        "day_0102_rubbing_and_prying",
        [1],
        'living_fembro',
        True,
        mom
        )

    jump loc_living

label day_0102_rubbing_and_prying:

    camera:
        perspective True

    scene bg living:
        background_art

    show main disgust at fit, flip, set_place(7)
    #wincing

    show fembro disgust at fit, flip, set_place(5)
    #wincing

    show mom disgust at fit, flip, set_place(3)
    #In actual pain

    mom.c "Ugh. You've been doing this for years, [fembro.name]. How are you still so bad at this?"

    "[fembro.name] tries [fembro_nouns[2]] best to massage your mother's thighs. But they seem to function like quicksand to [fembro_nouns[2]] hands."

    show main happy at fit, flip(1)
    #Nice

    main.c "Maybe you need stronger hands."

    show mom annoy at fit, flip, set_place(3)
    #Annoyed

    show fembro sad at fit
    #discouraged

    mom.c "Ugh. Sure, let's see if you're good at something useful."

    scene mom massage couch lean speak feet fembro

    mom.c "Just start from the lower calf and go up until I tell you to stop."

    if mom.dom:

        "Why are you doing this again?"

        "Oh yeah, the dirt."

        "Also, why not?"
    
    "Maybe the massage will help her to relax a little."

    scene mom massage couch feet fembro

    mom.c "And don't be a wuss like your [fembro_nouns[4]]. Put your muscle into it. I can take it."

    main.c "I'll do my best."

    mom.c "I don't want 'your best'. I want you to get rid of the cramp in my legs."

    scene mom massage rub
        
    $ thought_bubble(
        None, _("..."), 
        _("Damn... the view...")
        )

    scene mom massage rub calves

    "This isn't so bad after all."

    scene mom massage rub back speak calves

    mom.c "What are you doing?"

    "..."

    main.c "Massaging your calves?"

    scene mom massage rub back calves

    mom.c "Of course, you'd mess up this quickly."

    main.c "What did I-"

    scene mom massage rub calves

    mom.c "I said lower calf, that's clearly the upper."

    pause 1
        
    $ thought_bubble(
        None, _("..."), 
        _("Wow")
        )
    
    if mom.dom:

        "You inhale deeply."
        
        $ thought_bubble(
            None, _("You've got to get that info, any info you can use."),
            _("The wrath of 1000 suns.")
            )

    else:

        "You really wish she was nicer to you."

        "But something about her stern voice..."

    scene mom massage couch calves fix fembro
        
    $ thought_bubble(
        main.c, _("You seem really tense."),
        _("Why is [fembro.name] watching?")
        )

    scene mom massage pov

    mom.c "Hmph. My job, I'm surrounded by idiots every day."

    "You slowly go up the shins until you get to the knees."

    main.c "You're a secretary, right?"

    scene mom massage pov back

    mom.c "Yeah."

    main.c "So a lot of arrogant dicks telling you what to do?"

    mom.c "And a lot of catty bitches acting like I have it good."

    scene mom massage rub calves
        
    $ thought_bubble(
        None, _("You just got to her thighs, and..."),
        _("... Holy fuck!")
        )
    
    "It went from tense to pillowy soft instantly."

    "It's like you're kneading dough at this point."

    "No, keep focused."

    if mom.dom:

        "You need to ask more questions."

    else:

        "You can't start perving over her, or you're toast."

    main.c "I guess it's worth it for the money, huh?"

    mom.c "Oh I wish. I couldn't get another job if I tried."

    main.c "Well, at least it pays for the house."

    mom.c "Oh no, you're father bought the house a long time ago."

    main.c "No kidding?"

    mom.c "He also helped me get the job, before..."

    "..."

    mom.c "We're done talking."

    main.c "Whatever you say."

    if mom.dom:

        "Well, now you know what to do."

        "You need to have a talk with dear old dad."

        "If only you knew how to get in contact with him."

        "[lilsis.name] is your half-sister by your mother."

        "But [bigsis.name] is your full sister, and [fembro.name] is your half-[fembro_nouns[4]] by your father."

        "So either of them may know how to-"

    else:

        "Huh, that's the first time your mother has sounded that way."

        "She was actually sad. That's new."

        "It makes you wonder, is there anythin-"

    scene mom massage rub grope
        
    $ thought_bubble(
        None, _("..."),
        _("!")
        ) 

    scene mom massage rub back_grope grope

    mom.c "You stopped."

    main.c "Well, I-"

    mom.c "Keep going until I say otherwise."

    scene mom massage rub grope
        
    $ thought_bubble(
        None, _("Even [fembro.name] is blushing now."),
        _("Well...")
        )

    "Oh yeah. [fembro.name] is still here, watching this whole thing."

    "I wonder what [fembro_nouns[0]]'s thinking about?"

    "Maybe the same thing you are..."

    scene mom massage rub speak back_grope grope

    mom.c "Hey. Didn't I tell you to keep going?"

    main.c "Oh. Of course."

    scene mom massage rub grope

    "How the fuck did you get distracted when THIS is in front of you?"

    "You don't need to be asked twice to get your hands back on that ass."

    "You get your hands deep in her glutes, staying on the underside so as not to push your luck."

    "Her butt is soft. Like, softer than anything you've ever felt."

    "Softer than you thought people could be."

    "And jiggly."

    "With your caressing, her cheeks wobble, lightly tapping against each other."

    "Your cock swells, clearly visible through your pants."

    "Your hands move up passed the shelf of her cheeks, up to-"

    mom.c "Alright. That's enough."

    main.c "... Whah?"

    scene bg living:
        background_art

    show main happy at fit, set_place(5), flip
    #Satisfied

    show fembro sad at fit, flip, set_place(9)
    #Pouts

    show mom happy at fit, set_place(3)
    #relaxed

    "Your mom gets up, leaving the sensation of her ass engraved into your palms."

    "She looks over with a soft expression."

    mom.c "Good job."

    show main surprise at fit
    #In shock
        
    $ thought_bubble(
        None, _("..."),
        _("Did she actually Praise me?!")
        )

    hide mom
    with easeoutright

    "She heads to her room as you process what just happened."

    "[fembro.name] steeps in jealousy."

    if mom.dom:

        show main calm at fit
        #measured

        "Still, one moment of kindness doesn't make up for the years of abuse."
        
        $ thought_bubble(
            None, _("You've made up your mind. You're going to take her down a peg."),
            _("All the pegs.")
            )

    else:

        show main happy red at fit
        #measured

        "She actually praised you! You can't believe it."

        "This is great, she's actually showing you an emotion besides disgust and disappointment."

    "But hell, There's not much you wouldn't do to feel that butt on your hands again."

    "Maybe more places too."
    
    $ persistent.replay_scenes.append('day_0102_nothing_to_do_for_a_while')
    $ renpy.end_replay()

    $ mom.stage = 11

    jump loc_living

label day_0102_help_auntie:

    camera:
        perspective True

    if ((not aunt.chosen) and (not _in_replay)):

        jump loc_bed_aunt

    else:

        scene bg bed ian:
            background_art

        show main calm at fit, set_place(7), flip

        "You enter your room, they've already set up painting equipment."

    show aunt non at fit, set_place(2)
    #happy and welcoming
    with easeinleft

    aunt.c "Good, you're here!"

    show aunt happy at fit
    #Friendly

    aunt.c "[mom.name]'s having me refresh the paint."

    aunt.c "Wanna help me?"

    show main annoy at fit
    #annoyed

    $ thought_bubble(
        main.c, _("{i}Sigh{/i} yep."), 
        _("Mom didn't tell me any of this.")
        )

    show aunt sad at fit
    #sympathetic

    aunt.c "Hey, I'm sorry you're mom's forcing you to give up the room."

    show main calm at fit
    #relaxed

    main.c "Don't worry about it, you need a place to sleep, after all."

    show aunt non at fit
    #happy

    main.c "You can even pick the new color and put up some decor if you want."

    aunt.c "Really? Thanks, [main.name]."

    aunt.c "You're welcome to keep any of it when I leave."

    show main fear at fit
    #panicing

    $ thought_bubble(
        aunt.c, _("I noticed your room is pretty bare when I came."), 
        _("Wait...")
        )

    show aunt surprise at fit
    #surprised

    main.c "Aw shit, where's spike!"
    
    show main fear at flip:
        subpixel True 
        set_place(7)
        easeout2 0.6 set_place(9)
    with Pause(1.2)
    show main fear:
        set_place(9)

    "You start frantically searching the room. There's barely anything to search though."

    aunt.c "Who's spike?"

    show main sad at fit
    #really sad

    main.c "My cactus."

    show aunt non at fit
    #comforting

    aunt.c "Oh, don't worry, your mom took it to the basement."
    
    show aunt surprise at fit
    #thinking
    
    aunt.c "Though I don't think that's a good place to keep a plant."

    main.c "He's plastic... She probably threw him away."
    
    show aunt non at fit
    #trying to comfort him

    $ thought_bubble(
        aunt.c, _("Come on, have some faith in your mom, would you? She can be really caring in her own way."), 
        _("... Are we talking about the same person?")
        )

    main.c "Not much to have faith in."
    
    show aunt sad at fit
    #disheartened

    "[aunt.name] sighs, then lights up."
    
    show aunt non at fit
    #smile

    aunt.c "I already know what to paint in here."
    
    show main happy at fit
    #calm

    main.c "Cool, I'll go get the orange one from the basement."

    $ aunt.stage = 11

    $ add_scene(
        "day_0102_got_paint",
        [2],
        'basement_clutter',
        False,
        None
        )

    if _in_replay:
        jump day_0102_got_paint

    jump loc_stairs

label day_0102_got_paint:

    camera:
        perspective True

    scene bg basement:
        background_art

    show main annoy grab at fit(False, 5)

    $ thought_bubble(
        aunt.c, _("You find it relatively easily."), 
        _("That was easy.")
        )

    $ thought_bubble(
        aunt.c, _("Of course, you don't see spike anywhere."), 
        _("Of course. Nice one Mom.")
        )

    if _in_replay:
        jump day_0102_help_auntie_2

    $ inventory.add_item(all_items_list["paint"])

    $ add_scene(
        "day_0102_help_auntie_2",
        [2],
        'bed_aunt',
        True,
        aunt
        )

    jump loc_basement

label day_0102_help_auntie_2:

    camera:
        perspective True

    scene bg bed aunt:
        background_art(True)

    show aunt disgust at fit, set_place(2)
    
    show main sad at fit, set_place(9), flip

    pause 1

    "The two of you spend hours painting. By the end, you're both drained."

    main.c "Only one wall left."
    
    show aunt non at fit

    aunt.c "Yeah, then we can watch it dry."

    "As you go to fill the tray-"
    
    show main calm at fit:
        subpixel True 
        set_place(9)
        easeout2 0.8 set_place(8)
    with Pause(0.8)
    show main calm at fit:
        set_place(8)

    show aunt fear at fit
    
    show main fear at fit:
        subpixel True 
        set_place(8)
        easeout2 0.2 set_place(6)
    with Pause(0.2)
    show main fear at fit:
        set_place(6)

    "{i}SPLASH{/i}"

    "The paint hits the wall but splashes off of it. A large glob hits [aunt.name]."

    scene aunt paint splash

    aunt.c "Agh, I like this top."

    main.c "Fuck, I'm sorry."

    aunt.c "Don't worry, barely any got on me."

    aunt.c "You got any towels?"

    main.c "Yeah, here."

    "You grab a wet rag and rush to clean her off."

    scene aunt paint wipe

    "You reach to wipe her down, but stop when you realize it's on her boobs."

    "You go down to her belly instead, but freeze up when you feel how firm her abs are."

    "She's wiping her breasts, so she doesn't notice you stalling."

    "As you clean off the muscles along the side of her stomach, you gravitate toward the center, towards her abs."

    "Her abdomen feels amazing."

    "You can feel the hump of each muscle."

    "Are you cleaning her abs with the rag or washing the rag on her abs?"

    $ thought_bubble(
        None, _("Then, you get to her Apollo's belt, which guides the paint down to her..."), 
        _("They're like gutters...")
        )

    "Somewhere you dare not reach."

    "So instead, you stop where her shorts' waist band starts."

    if dominant:
        "In spite of the situation, your movements are sure and smooth."

    else:
        "Your hands quiver with each stroke."

    aunt.c "[main.name]?"

    $ thought_bubble(
        None, _("Huh?"), 
        _("Damn, she probably thinks I'm a creep.")
        )

    scene aunt paint flirt

    aunt.c "I said thanks for being so thorough."

    "You sign in relief as she chuckles."

    aunt.c "You missed a spot though, a little lower."

    "You go down until your hand is up against her waistband."

    aunt.c "Lower."

    "You pull on the waistband, revealing skin untouched by paint."

    aunt.c "Low-"

    scene bg bed aunt:
        background_art
    
    show aunt fear at fit, set_place(2)
    
    show main fear at fit, set_place(9), flip

    mom.c "[main.name]! Get your ass to bed! You'll be busy tomorrow!"
    
    show aunt sad at fit

    show main annoy at fit

    $ thought_bubble(
        aunt.c , _("Boo."), 
        _("Damn it, mom.")
        )
    
    show aunt surprise at fit

    aunt.c "Well, it looks like the painting is... done?"

    aunt.c "You can head out, I'll smooth it over."

    show main calm red

    "She winks at you."

    show aunt non at flip
    
    "When she looks away, you adjust your pants and take your leave."

    show main calm
    pause 0.1

    hide main
    with easeoutright

    $ aunt.stage = 12
    
    $ persistent.replay_scenes.append('day_0102_help_auntie')
    $ renpy.end_replay()

    jump loc_stairs