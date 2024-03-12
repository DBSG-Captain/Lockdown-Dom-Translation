init python:
    def hint_var(def_name, char):
        #if the character exists
        if char:
            #If you didn't miss any stages
            if char.stage != -10:
                #if they're selected
                if char.chosen:
                    if char.stage in hints_list[(def_name)]:
                        #if hints is on
                        if extra_hint:
                            return (times[hints_list[(def_name)][char.stage][0]] + "; " + hints_list[(def_name)][char.stage][1])
                        else:
                            return hints_list[(def_name)][char.stage][1]
                    else:
                        return end_of
                else:
                    return hints_list["disabled"]
            else:
                return hints_list["ignored"]

#every 10 is a new day with a stage
define nothing_more = [4, _("Nothing today...")]
define end_of = [4, _("End of Content")]
define hints_list = {
    "disabled": _("Not focused on them."),
    "ignored": _("I feel like I missed something yesterday."),
    "Clarissa": {
        0: [4, _("You missed a scene, go back a day.")],
        10: [0, _("You should go to the restroom")],
        11: [1, _("What's she doing anyway, probably in her room")],
        12: nothing_more,
        20: end_of
        },
    "Jessie": {
        0: [4, _("You missed a scene, go back a day.")],
        10: [3, _("Sleep. Use earplugs downstairs to avoid hearing anything")],
        11: [3, _("Sleep.")],
        12: nothing_more,
        20: end_of
        },
    "Linda": {
        0: [4, _("You missed a scene, go back a day.")],
        10: [1, _("She's in the living room, I should try and learn more about her")],
        11: nothing_more,
        20: end_of
        },
    "Addison": {
        0: [4, _("You missed a scene, go back a day.")],
        10: [3, _("Sleep.")],
        11: nothing_more,
        20: [0, _("They may be in the kitchen, you should apologize for last night")],
        21: end_of
        },
    "Ruby": {
        0: [4, _("You missed a scene, go back a day.")],
        10: [2, _("I should help her get moved in.")],
        11: [2, _("I gotta get the orange paint.")],
        12: nothing_more,
        20: [0, _("I should greet her to make her feel welcome")],
        21: end_of
        }
    }