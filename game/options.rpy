# Options.rpy

# This is where you will name your mod!
# Change "DDLC Mod Template 2.0" to your mod name (e.g. "Yuri")
define config.name = "Switching Dokis"

# This controls whether you want your mod name to show in the main menu.
# If your mod name is big, it is suggested to turn this off
define gui.show_name = False

# This is where you will input the version of your mod.
# If you have multiple versions of your mod, this will be pretty useful to change.
# If you are starting out, set this to "1.0.0"
define config.version = "0.1"

# This adds information about your mod in the About section.
# DDLC does not have a about section so you can leave this blank.
define gui.about = _("")

# This is the name of your build that the Ren'Py SDK will read.
# The build name is ASCII only so no numbers, spaces, or semicolons.
# Example: Doki Doki Yuri Time to DokiDokiYuriTime
define build.name = "Switching"

# This configures whether your mod has sound effects (e.g. slap sound effects) or not.
# It is best to leave this set to True default.
define config.has_sound = True

# This configures whether your mod has music (e.g. Your Reality) or not.
# It is best to leave this set to True default.
define config.has_music = True


define config.has_voice = False


define config.main_menu_music = audio.t1

# These two settings control the transition effects of DDLC on the game menu.
# Dissolve(.2) sets the transition effect you see.
# config.enter_transition controls the effect seen when entering the game menu.
# config.exit_transition controls the effect when returning to the game.
define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)



define config.after_load_transition = None



define config.end_game_transition = Dissolve(.5)



define config.window = "auto"



define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)



default preferences.text_cps = 50

# This controls the auto-forward speed
# 15 is DDLC's default speed.
# You can change it from 0-30
default preferences.afm_time = 15


default preferences.music_volume = 1.00
default preferences.sfx_volume = 1.00

define config.save_directory = "SwitchingDoki"


define config.window_icon = "gui/window_icon.png"


define config.allow_skipping = True

# This controls whether your mod saves automatically.
define config.has_autosave = False

# This controls whether you mod saves when quitting the game.
define config.autosave_on_quit = False

# This controls the number of slots auto-saving can use
define config.autosave_slots = 0

# This controls the layers of screens, images, and more. 
# Best not to leave this alone.
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]

# Stuff to leave alone also.
define config.image_cache_size = 64
define config.predict_statements = 50
define config.rollback_enabled = config.developer
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"


init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)




# Building Your Mod

init python:

    # This is where your mod gets built by Ren'Py!
    # These are case-sensitive and matched against the actual filenames
    # in your 'game' folder, with or without '/'
    #
    # '/' this is a directory seperator
    # game/**.rpyc tells Ren'Py to grab all .rpyc's in the 'game' folder
    # **.psd matches all .psd's in the mod project.
    #
    # If you don't want a file to be added to your RPA, classify it as None
    # Example: build.classify("game/randomtext.txt", None)

    # Code to Package your mod to a ZIP in Ren'Py
    #build.package(build.directory_name + "Mod",'zip',build.name,description='DDLC Compatible Mod')

    #build.archive("scripts", build.name)
    #build.archive("mod_assets", build.name)

    #build.classify("game/mod_assets/**", "mod_assets")
    #build.classify("game/tl/**", "mod_assets")
    #build.classify("game/**.rpyc", "scripts")
    #build.classify('**.rpy', "scripts")
    #build.classify("game/README.txt", None)
    #build.classify("game/**.txt", "scripts")
    #build.classify("game/**.chr", "scripts")
    #build.classify("game/advanced_scripts/**","scripts")

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)
    build.classify('**.rpa', None)
    build.classify('README.html',build.name)

    # Set's README.html as documentation
    build.documentation('README.html')

    build.include_old_themes = True

    #Advanced Addons

    # Doki Doki Mod Manager metadata file
    build.classify('ddmm-mod.json',build.name)
