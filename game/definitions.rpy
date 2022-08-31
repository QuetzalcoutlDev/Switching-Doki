

transform gout_appear:
    alpha 0.0 yoffset -10 
    ease 1.12 yoffset 0 alpha 1.0

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass
    def restore_all_characters():
        import os
        try: os.remove(config.basedir + "/characters/monika - respaldo,chr")
        except: pass
        try: renpy.file("../characters/monika.chr")
        except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
        try: renpy.file("../characters/geraldine.chr")
        except: open(config.basedir + "/characters/geraldine.chr", "wb").write(renpy.file("geraldine.chr").read())
        try: renpy.file("../characters/fredgio.chr")
        except: open(config.basedir + "/characters/fredgio.chr", "wb").write(renpy.file("fredgio.chr").read())
        try: renpy.file("../characters/natsuki.chr")
        except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
        try: renpy.file("../characters/yuri.chr")
        except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
        try: renpy.file("../characters/sayori.chr")
        except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())
    def pause(time=None):
        if not time:
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            return
        if time <= 0: return
        renpy.pause(time)

    """Esta función define las partes del cuerpo de X personaje, no es capaz de definir las expresiones."""
    def make_sprites(char="", char_dir="",char_short="", head_num=1, eyebrows_num=1, eye_num=1, eyeexp_num=1, mouth_num=1, tears_num=1, blush_num=1, glasses=False, gout=True, body_num=True):
        # El nombre del personaje en minuscula.
        if char == "":
            renpy.error(_("Es necesario colocar el nombre del personaje."))
        if char_dir == "" or char_dir == None:
            sprite = "/sprites/" + char + "/"
        else:
            sprite = "/sprites/" + char + "/" + char_dir + "/"

        if head_num == 1:
            if renpy.exists("images" + sprite + "Head.png"):
                renpy.image(char_short + "head", sprite + "Head.png") #jnhead
            else:
                renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'head.png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))
        elif head_num > 1:
            for heads in range(1, head_num + 1):
                if renpy.exists("images" + sprite + "Head" + str(heads) + ".png"):
                    renpy.image(char_short + "head" + str(heads), sprite + "Head" + str(heads) + ".png") #jnhead1
                else:
                    renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'head_") + str(heads) + _(".png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))
       
        elif head_num == None:
            pass
        
        for eyebrowss in range(1, eyebrows_num + 1):
            if renpy.exists("images" + sprite + "eyebrows_" + str(eyebrowss) + ".png"):
                renpy.image(char_short + "eyebrows" + str(eyebrowss), sprite + "eyebrows_" + str(eyebrowss) + ".png") #jneyebrows1
            else:
                renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'eyebrows_") + str(eyebrowss) + _(".png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))
            
        for eyes in range(1, eye_num + 1):
            if renpy.exists("images" + sprite + "eye_" + str(eyes) + ".png"):
                renpy.image(char_short + "eye" + str(eyes), sprite + "eye_" + str(eyes) + ".png") #jneye1
            else:
                renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'eye_") + str(eyes) + _(".png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))
            
        if eyeexp_num >= 1:
            for eyeexps in range(1, eyeexp_num + 1):
                if renpy.exists("images" + sprite + "eye_exp" + str(eyeexps) + ".png"):
                    renpy.image(char_short + "eyeexp" + str(eyeexps), sprite + "eye_exp" + str(eyeexps) + ".png") #jneyeexp1
                else:
                    renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'eye_exp") + str(eyeexps) + _(".png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))
        
        elif eyeexp_num == None:
            pass

        for mouths in range(1, mouth_num + 1):
            if renpy.exists("images" + sprite + "mouth_" + str(mouths) + ".png"):
                renpy.image(char_short + "mouth" + str(mouths), sprite + "mouth_" + str(mouths) + ".png") #jnmouth1
            else:
                renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'mouth_") + str(mouths) + _(".png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))

        if tears_num == 1:
            if renpy.exists("images" + sprite + "tears.png"):
                renpy.image(char_short + "tears", sprite + "tears.png") #jntears
            else:
                renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'tears.png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))

        elif tears_num > 1:
            for tearss in range(1, tears_num + 1):
                if renpy.exists("images" + sprite + "tears" + str(tearss) + ".png"):
                    renpy.image(char_short + "tears" + str(tearss), sprite + "tears" + str(tearss) + ".png") #jntears1
                else:
                    renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'tears" + str(tearss) + ".png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))

        elif tears_num == None:
            pass
            
        if blush_num == 1:
            if renpy.exists("/images" + sprite + "blush.png"):
                renpy.image(char_short + "blush", sprite + "blush.png") #jnblush
            else:
                renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'blush.png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))
        elif blush_num == None:
            pass
        elif blush_num > 1:
            for blushs in range(1, blush_num + 1):
                if renpy.exists("/images" + sprite + "blush" + str(blushs) + ".png"):
                    renpy.image(char_short + "blush" + str(blushs), sprite + "blush" + str(blushs) + ".png") #jnblush1
                else:
                    renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'blush") + str(blushs) + _("png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))
        if glasses == True:
            if renpy.exists("/images" + sprite + "glasses.png"):
                renpy.image(char_short + "glasses", sprite + "glasses.png") #koglasses
            else:
                renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'glasses.png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))
        
        if gout == True:
            if renpy.exists("/images" + sprite + "gout.png"):
                renpy.image(char_short + "gout", At(sprite + "gout.png", gout_appear)) #kogout
            else:
                renpy.error(_("El personaje ") + "'" + char + "'" + _(" no contiene la imagen 'gout.png' en su directorio, verifica el nombre\n o puede ser que tal imagen no exista."))
        
        body_keys = ["a", "b", "c", "d"]
        if body_num == True:
            for bodys in range(10):
                if renpy.exists("/images" + sprite + str(bodys) + ".png"):
                    renpy.image(char_short + str(bodys), sprite + str(bodys) + ".png") #ko1
                else:
                    pass

        elif body_num >= 1:
            for key in range(len(body_keys)):
                for bodys in range(1,body_num + 1):
                    renpy.image(char_short + str(bodys) + body_keys[key] + "l", sprite + str(bodys) + "_" + body_keys[key] + "_l.png")
                    renpy.image(char_short + str(bodys) + body_keys[key] + "r", sprite + str(bodys) + "_" + body_keys[key] + "_r.png")
                    renpy.image(char_short + str(bodys) + body_keys[key], sprite + str(bodys) + "_" + body_keys[key] + ".png")


define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m2 = DynamicCharacter('m_name', image='monika2', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define al = Character('Todas', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define nm = Character('Nat & Moni', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define gen = Character('Nat & Geral', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ge = DynamicCharacter("g_name", image='geraldine', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define f = DynamicCharacter("f_name", image='fredgio', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define _dismiss_pause = config.developer
define persistent.geraldine_exclusives_first = True

default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.anticheat = 0
default persistent.first_load = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"
default g_name = "Geraldine"
default f_name = "Fredgio"

define persistent.steam = False
define config.developer = "auto"
default -1 persistent.time_notify = 3.25

python early:
    import singleton
    me = singleton.SingleInstance()