init python:
    #for eye open and close animation
    def eyewarp(x):
        return x**1.33
    def shift_eyes(close=True, time=1):
        return ImageDissolve("eye.png", time, ramplen=128, reverse=close, time_warp=eyewarp)

###Sprite Positions

define sprite_height = (1.5)
define sprite_zoom = (0.43)

transform fit_sprite_gallery:
    zoom 0.30
    align (0.5, 1.0)

transform set_height(y=sprite_height):
    ypos y

transform set_place(x, y=sprite_height):
    xpos (x/10)
    ypos y

transform flip(z=-1):
    xzoom z
    
transform fit(flipper=False, x=(-10), y=sprite_height):
    zoom sprite_zoom
    yanchor 1.0
    xanchor 0.5
    (set_place(x, y) if (x != -10) else set_height(y))
    (flip(-1) if flipper else flip(1))

define config.mouse = { 
    'default' : [ ('ui/mouse_base.png', 0, 0)], 
    'item' : [ ('ui/mouse_item.png', 0, 0)], 
    'area' : [ ('ui/mouse_area.png', 0, 0)], 
    'char' : [ ('ui/mouse_character.png', 0, 0)], 
    'obje' : [ ('ui/mouse_object.png', 0, 0)]
    }

###Sprites


# For images
# Main

layeredimage main:
    at sprite_highlight('main')
    always:
        "main_1"

    group arm_b:
        attribute down default if_all ["casual"]:
            "main_a-b_down_o_casual"
        attribute down default if_all ["underwear"]:
            "main_a-b_down_o_underwear"
        attribute grab if_all ["casual"]:
            "main_a-b_reach_o_casual"
        attribute grab if_all ["underwear"]:
            "main_a-b_reach_o_underwear"
        attribute out if_all ["underwear"]:
            "main_a-b_out_o_underwear"

    group outfit:
        attribute casual default:
            "main_o_casual"
        attribute underwear:
            "main_o_underwear"

    group erection:
        attribute soft default:
            "main_empty"
        attribute erect if_all ["casual"]:
            "main_p_o_casual"
        attribute erect if_all ["underwear"]:
            "main_p_o_underwear"

    group arm_a:
        attribute a-down default if_all ["casual"]:
            "main_a-a_down_o_casual"
        attribute a-down default if_all ["underwear"]:
            "main_a-a_down_o_underwear"
        attribute a-out if_all ["casual"]:
            "main_a-a_out_o_casual"
        attribute a-out if_all ["underwear"]:
            "main_a-a_out_o_underwear"

    group exp:
        attribute calm default:
            "main_e_1"
        attribute anger:
            "main_e_anger"
        attribute annoy:
            "main_e_annoy"
        attribute blush:
            "main_e_blush"
        attribute disgust:
            "main_e_disgust"
        attribute fear:
            "main_e_fear"
        attribute happy:
            "main_e_happy"
        attribute sad:
            "main_e_sad"
        attribute smug:
            "main_e_smug"
        attribute surprise:
            "main_e_surprise"

    group blush:
        attribute no default:
            "main_empty"
        attribute red:
            "main_blush"

    group hair:
        attribute basic default:
            "main_h_basic"

# Clarissa

layeredimage lilsis:
    at sprite_highlight('lilsis')
    always:
        "lilsis_1"

    group hair_b:
        attribute ponytail default:
            "lilsis_h-b_ponytail"

    group arm_b:
        attribute hip default if_all ["casual"]:
            "lilsis_a-b_hip_o_casual"
        attribute hip default if_all ["pajama"]:
            "lilsis_a-b_hip_o_pajama"
        attribute lift if_all ["casual"]:
            "lilsis_a-b_lift_o_casual"
        attribute lift if_all ["pajama"]:
            "lilsis_a-b_lift_o_pajama"

    group outfit:
        attribute casual default:
            "lilsis_o_casual"
        attribute pajama:
            "lilsis_o_pajama"

    group arm_a:
        attribute ab-hip default if_all ["casual", "hip"]:
            "lilsis_a-ab_hip_o_casual"
        attribute a-hip default if_all ["casual"]:
            "lilsis_a-a_hip_o_casual"
        attribute ab-hip default if_all ["pajama", "hip"]:
            "lilsis_a-ab_hip_o_pajama"
        attribute a-hip default if_all ["pajama"]:
            "lilsis_a-a_hip_o_pajama"

    group exp:
        attribute calm default:
            "lilsis_e_1"
        attribute anger:
            "lilsis_e_anger"
        attribute annoy:
            "lilsis_e_annoy"
        attribute blush:
            "lilsis_e_blush"
        attribute disgust:
            "lilsis_e_disgust"
        attribute fear:
            "lilsis_e_fear"
        attribute happy:
            "lilsis_e_happy"
        attribute sad:
            "lilsis_e_sad"
        attribute smug:
            "lilsis_e_smug"
        attribute surprise:
            "lilsis_e_surprise"

    group blush:
        attribute no default:
            "lilsis_empty"
        attribute red:
            "lilsis_blush"

    group hair_a:
        attribute anime default:
            "lilsis_h-a_base"

# Jessie

layeredimage bigsis:
    at sprite_highlight('bigsis')
    always:
        "bigsis_1"

    group arm-b:
        attribute down default if_all ["casual"]:
            "bigsis_b_down_o_casual"
        attribute down default if_not ["casual"]:
            "bigsis_b_down_o_underwear"
        attribute cross:
            "bigsis_empty"
        attribute phone if_all ["casual"]:
            "bigsis_b_phone_o_casual"
        attribute phone if_not ["casual"]:
            "bigsis_b_phone_o_underwear"
        attribute point if_all ["casual"]:
            "bigsis_b_point_o_casual"
        attribute point if_not ["casual"]:
            "bigsis_b_point_o_underwear"
        attribute up if_all ["casual"]:
            "bigsis_b_up_o_casual"
        attribute up if_not ["casual"]:
            "bigsis_b_up_o_underwear"

    group outfit:
        attribute casual default:
            "bigsis_o_casual"
        attribute underwear:
            "bigsis_o_underwear"
        attribute towel:
            "bigsis_o_towel"
        
    group exp:
        attribute calm default:
            "bigsis_e_1"
        attribute anger:
            "bigsis_e_anger"
        attribute annoy:
            "bigsis_e_annoy"
        attribute blush:
            "bigsis_e_blush"
        attribute disgust:
            "bigsis_e_disgust"
        attribute fear:
            "bigsis_e_fear"
        attribute happy:
            "bigsis_e_happy"
        attribute sad:
            "bigsis_e_sad"
        attribute smug:
            "bigsis_e_smug"
        attribute surprise:
            "bigsis_e_surprise"

    group boobs:
        attribute flat default if_not ["a-down"]:
            "bigsis_empty"
        attribute booba default if_all ["casual", "a-down"]:
            "bigsis_b_o_casual"
        attribute booba default if_all ["underwear", "a-down"]:
            "bigsis_b_o_underwear"

    group arm-a:
        attribute a-cross default if_all ["casual"]:
            "bigsis_a_cross_o_casual"
        attribute a-cross default if_all ["underwear"]:
            "bigsis_a_cross_o_underwear"
        attribute a-down if_all ["casual"]:
            "bigsis_a_down_o_casual"
        attribute a-down if_all ["underwear"]:
            "bigsis_a_down_o_underwear"
        attribute ab-cross default if_all ["casual", "cross"]:
            "bigsis_a-b_cross_o_casual"
        attribute ab-cross default if_all ["underwear", "cross"]:
            "bigsis_a-b_cross_o_underwear"

    group blush:
        attribute no default:
            "bigsis_empty"
        attribute red:
            "bigsis_blush"

    group hair_a:
        attribute pixie default:
            "bigsis_h_base"
        attribute wet:
            "bigsis_h_wet"

# Addison(DO)

image fembro_new = "char/fembro/fembro-1.png"

layeredimage fembro:
    at sprite_highlight('fembro')
    always:
        "addison_0"

    group outfit:
        attribute tense default:
            "addison_2"
        attribute relax:
            "addison_3"
        attribute open:
            "addison_1"
        attribute pajama:
            "addison_4"

    group exp:
        attribute non default:
            "addison_default"
        attribute anger:
            "addison_anger"
        attribute disgust:
            "addison_disgust"
        attribute fear:
            "addison_fear"
        attribute happy:
            "addison_happy"
        attribute sad:
            "addison_sad"
        attribute surprise:
            "addison_surprise"

# Linda

layeredimage mom:
    at sprite_highlight('mom')
    always:
        "mom_1"

    group hair_b:
        attribute long default:
            "mom_h-b_long"
        attribute bun:
            "mom_h-b_bun"

    group arm_b_bare:
        attribute back default if_any ["casual", "pajama"]:
            "mom_a-b_back"
        attribute phone if_any ["casual", "pajama"]:
            "mom_a-b_phone"
        attribute point if_any ["casual", "pajama"]:
            "mom_a-b_point"
        attribute grab if_any ["casual", "pajama"]:
            "mom_a-b_grab"

    group outfit:
        attribute casual default:
            "mom_o_casual"
        attribute pajama:
            "mom_o_pajama"

    group exp:
        attribute calm default:
            "mom_e_1"
        attribute anger:
            "mom_e_anger"
        attribute annoy:
            "mom_e_annoy"
        attribute blush:
            "mom_e_blush"
        attribute disgust:
            "mom_e_disgust"
        attribute fear:
            "mom_e_fear"
        attribute happy:
            "mom_e_happy"
        attribute sad:
            "mom_e_sad"
        attribute smug:
            "mom_e_smug"
        attribute surprise:
            "mom_e_surprise"

    group blush:
        attribute no default:
            "mom_empty"
        attribute red:
            "mom_blush"

    group hair_a:
        attribute swoop default:
            "mom_h-a_base"

# Ruby(DO)

layeredimage aunt:
    at sprite_highlight('aunt')
    always:
        "ruby_1"

    group exp:
        attribute non default:
            "ruby_1"
        attribute anger:
            "ruby_anger"
        attribute disgust:
            "ruby_disgust"
        attribute fear:
            "ruby_fear"
        attribute happy:
            "ruby_happy"
        attribute sad:
            "ruby_sad"
        attribute surprise:
            "ruby_surprise"

# Darian

layeredimage sisbf:
    at sprite_highlight('sisbf')
    always:
        "sisbf_1"

    group arm_b:
        attribute down default if_all ["casual"]:
            "sisbf_a-b_down_o_casual"
        attribute down default if_all ["pajama"]:
            "sisbf_a-b_down_o_pajama"
        attribute grab if_all ["casual"]:
            "sisbf_a-b_grab_o_casual"
        attribute grab if_all ["pajama"]:
            "sisbf_a-b_grab_o_pajama"

    group outfit:
        attribute casual default:
            "sisbf_o_casual"
        attribute pajama:
            "sisbf_o_pajama"

    group arm_a:
        attribute a-down default if_all ["casual"]:
            "sisbf_a-a_down_o_casual"
        attribute a-down default if_all ["pajama"]:
            "sisbf_a-a_down_o_pajama"
        attribute a-wave if_all ["casual"]:
            "sisbf_a-a_wave_o_casual"
        attribute a-wave if_all ["pajama"]:
            "sisbf_a-a_wave_o_pajama"

    group exp:
        attribute calm default:
            "sisbf_e_1"
        attribute anger:
            "sisbf_e_anger"
        attribute annoy:
            "sisbf_e_annoy"
        attribute blush:
            "sisbf_e_blush"
        attribute disgust:
            "sisbf_e_disgust"
        attribute fear:
            "sisbf_e_fear"
        attribute happy:
            "sisbf_e_happy"
        attribute sad:
            "sisbf_e_sad"
        attribute smug:
            "sisbf_e_smug"
        attribute surprise:
            "sisbf_e_surprise"

    group blush:
        attribute no default:
            "sisbf_empty"
        attribute red:
            "sisbf_blush"

    group hair:
        attribute basic default:
            "sisbf_h_base"

###Backgrounds
image bg black:
    Solid("#000")

image bg white:
    Solid("#FFF")

image bg empty = "scenes/empty.png"

image bg living = "back/living.png"

image bg stairs = "back/stairs.png"

image bg bath = "back/bath.png"

image bg kitchen = "back/kitchen.png"

image bg basement = "back/basement.png"

image bg bed lilsis  = "back/bed_lilsis.png"

image bg bed fembro  = "back/bed_fembro.png"

image bg bed ian = "back/bed_ian.png"

image bg bed aunt = "back/bed_aunt.png"
image bg bed aunt done = "back/bed_aunt_done.png"

###Scenes

#day0101
layeredimage lilsis marker:
    always:
        "clarissa_marker_smirk"

    group face:
        attribute smirk default:
            "empty"
        attribute oops:
            "clarissa_marker_oops"

layeredimage bigsis shower:
    always:
        "jessie_shower"

    group pose:
        attribute p1 default:
            "jessie_shower_1"
        attribute p2:
            "jessie_shower_2"
        attribute p3:
            "jessie_shower_3"
        attribute p4:
            "jessie_shower_4"

layeredimage door bath:
    always:
        "door_bath"

    group exp:
        attribute clear default:
            "empty"
        attribute steam:
            "door_bath_steam"

image bigsis shower kick = "scenes/jessie_shower_kick.png"

image fembro stuck pull = "scenes/addison_stuck_pull.png"

image mom grab collar = "scenes/linda_grab_collar.png"

image mom grab balls = "scenes/linda_grab_balls.png"

image aunt intro stand = "scenes/ruby_intro_stand.png"

image ian box = "scenes/ian_box.png"

image news incest legal = "scenes/incest_legal.png"

#day0102
image lilsis cock shock = "scenes/clarissa_cock_shock.png"

image door lilsis = "scenes/door_clarissa.png"

layeredimage lilsis masturbation peak:
    always:
        "clarissa_masturbation_peak"

    group effect:
        attribute base default:
            "empty"
        attribute climax:
            "clarissa_masturbation_peak_climax"

layeredimage mom massage pov:
    always:
        "linda_massage_pov_wait"

    group face:
        attribute wait default:
            "empty"
        attribute back:
            "linda_massage_pov_back"
        attribute hot:
            "linda_massage_pov_hot"

layeredimage mom massage couch:
    always:
        "linda_massage_couch"

    group linda_pose:
        attribute lay default:
            "linda_massage_couch_linda_lay"
        attribute lean:
            "linda_massage_couch_linda_lean"
        attribute hump:
            "linda_massage_couch_hump"

    group linda_face:
        attribute rest default:
            "empty"
        attribute speak if_not "hump":
            "linda_massage_couch_linda_speak"
            
    group ian:
        attribute no_ian default:
            "empty"
        attribute feet:
            "linda_massage_couch_ian_feet"
        attribute calves:
            "linda_massage_couch_ian_calves"

    group linda_lay_ian_calves_fix:
        attribute no_fix default:
            "empty"
        attribute fix if_all ["lay", "calves"]:
            "linda_massage_couch_ian_calves_linda_lay"

    group fembro:
        attribute no_fembro default:
            "empty"
        attribute fembro:
            "linda_massage_couch_shadow"

layeredimage mom massage rub:
    always:
        "linda_massage_rub"

    group look:
        attribute forward default:
            "empty"
        attribute back:
            "linda_massage_rub_back"
        attribute back_grope:
            "linda_massage_rub_back_grope"

    group mouth:
        attribute closed default:
            "empty"
        attribute speak:
            "linda_massage_rub_speak"

    group butt-normal:
        attribute bare default if_not ["back_grope"]:
            "empty"
        attribute grope if_not ["back_grope"]:
            "linda_massage_rub_grope"

    group butt-back:
        attribute grope if_all ["back_grope"]:
            "linda_massage_rub_grope_back"

    group hands:
        attribute no_hands default:
            "empty"
        attribute calves:
            "linda_massage_rub_calves"

layeredimage mom massage hump:
    always:
        "linda_massage_hump"

    group hands:
        attribute nones default:
            "empty"
        attribute rub:
            "linda_massage_hump_rub"
        attribute punch:
            "linda_massage_hump_punch"

image aunt paint splash = "scenes/ruby_paint_splash.png"

image aunt paint wipe = "scenes/ruby_paint_wipe.png"

image aunt paint flirt = "scenes/ruby_paint_flirt.png"

#day0103
image bigsis imagine heat = "scenes/jessie_imagine_heat.png"

image bigsis imagine climax = "scenes/jessie_imagine_climax.png"

layeredimage fembro sleep grind:
    always:
        "addison_sleep_grind_bed_dark"

    group bed:
        attribute dark default:
            "empty"
        attribute light:
            "addison_sleep_grind_bed_light"

    group both:
        attribute empty default:
            "empty"
        attribute fembro:
            "addison_sleep_grind_addison"
        attribute separate:
            "addison_sleep_grind_both_separate"
        attribute together:
            "addison_sleep_grind_both_together"

    group ian:
        attribute empty default:
            "empty"
        attribute reach:
            "addison_sleep_grind_ian_pocket"

    group dick:
        attribute soft default:
            "empty"
        attribute hard:
            "addison_sleep_grind_both_together_boner"

    group eyes:
        attribute closed default:
            "empty"
        attribute main_open:
            "addison_sleep_grind_ian_eyes"
        attribute fembro_open:
            "addison_sleep_grind_both_together_eye"

#day0201

image aunt surprise punch = "scenes/ruby_surprise_punch.png"

image aunt surprise aftermath = "scenes/ruby_surprise_aftermath.png"

image aunt surprise kick = "scenes/ruby_surprise_kick.png"

image aunt surprise bonk = "scenes/ruby_surprise_bonk.png"

image aunt surprise kiss = "scenes/ruby_surprise_kiss.png"

layeredimage fembro reach:
    always:
        "addison_reach_counter"

    group body:
        attribute non default:
            "empty"
        attribute low:
            "addison_reach_low"

    group face:
        attribute non default:
            "empty"
        attribute forward:
            "addison_reach_look_forward"
        attribute back:
            "addison_reach_look_back"

layeredimage fembro cabinat:
    always:
        "addison_reach_cabinat"

    group body:
        attribute non default:
            "empty"
        attribute peak:
            "addison_reach_cabinat_peak"

layeredimage fembro fall:
    always:
        "addison_fall"

    group body:
        attribute non default:
            "empty"
        attribute balls:
            "addison_fall_balls"

    group eyes:
        attribute non default:
            "empty"
        attribute back:
            "addison_fall_eyes"

image aunt show_off = "scenes/ruby_show_off.png"

###day00