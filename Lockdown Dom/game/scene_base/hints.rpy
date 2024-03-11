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
                            return hints_list[(def_name)][char.stage]
                        else:
                            return (hints_list[(def_name)][char.stage][6:])
                    else:
                        return end_of
                else:
                    return hints_list["disabled"]
            else:
                return hints_list["ignored"]

#every 10 is a new day with a stage
define nothing_more = _("None; Nothing today...")
define end_of = _("None; End of Content")
define hints_list = {
    "disabled": _("Not focused on them."),
    "ignored": _("I feel like I missed something yesterday."),
    "Clarissa": {
        0: _("None; You missed a scene, go back a day."),
        10: _("Morn; You should go to the restroom"),
        11: _("Day ; What's she doing anyway, probably in her room"),
        12: nothing_more,
        20: end_of
        },
    "Jessie": {
        0: _("None; You missed a scene, go back a day."),
        10: _("Nigh; Sleep. Use earplugs downstairs to avoid hearing anything"),
        11: _("Nigh; Sleep."),
        12: nothing_more,
        20: end_of
        },
    "Linda": {
        0: _("None; You missed a scene, go back a day."),
        10: _("Day ; She's in the living room, I should try and learn more about her"),
        11: nothing_more,
        20: end_of
        },
    "Addison": {
        0: _("None; You missed a scene, go back a day."),
        10: _("Nigh; Sleep."),
        11: nothing_more,
        20: _("Morn; [fembro_nouns[0]!c] may be in the kitchen, you should apologize for last night"),
        21: end_of
        },
    "Ruby": {
        0: _("None; You missed a scene, go back a day."),
        10: _("Even; I should help her get moved in."),
        11: _("Even; I gotta get the orange paint."),
        12: nothing_more,
        20: _("Morn; I should greet her to make her feel welcome"),
        21: end_of
        }
    }