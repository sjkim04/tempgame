from time import sleep # the module that has the ability of The World
import sys # for killing the program when GAME OVERed

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # hiding that f**king annoying message

from pygame import mixer # playing BGMs and SEs
mixer.init()

reboot = 0

def typing(words, voice='default', offset=0.1): # typing effect
    for char in words:
        sleep(offset)
        sys.stdout.write(char)
        text_sound(voice)
        sys.stdout.flush()
    print()

def text_sound(voice='default'): # voices for type()
    if voice == 'default': # default voice from UNDERTALE (frisk)
        mixer.music.load('voices\\default.wav')
        mixer.music.play()
    elif voice == 'default2': # second default voice from UNDERTALE (chara)
        mixer.music.load('voices\\default2.wav')
        mixer.music.play()
    elif voice == 'sans': #SAAAAAAAAAAAAAAAAAAAAAAAAAAANS
        mixer.music.load('voices\\sans.wav')
        mixer.music.play()
    elif voice == 'select': # selecting commands
        mixer.music.load('voices\\select.wav')
        mixer.music.play()
    elif voice == 'papyrus': # I, THE GREAT PAPYRUS, VOICE ACTED IN THIS GAME!
        mixer.music.load('voices\\papyrus.wav')
        mixer.music.play()

def game_start():
    mixer.Channel(1).play(mixer.Sound('bgm\\wind.wav'), loops=-1)
    typing('Type \'y\'', 'default')
    shoken1 = input()
    if shoken1 == 'y':
        gameover('Yeah, this IS a troll game.')
    elif shoken1 == '':
        typing('or \'Start\' to start')
        gamestart = input('')
        if gamestart.lower() == 'start':
            text_sound('select')
            char_make()
        else:
            gameover('Yep. Don\'t enter anything else.')
    elif shoken1.lower() == 'n':
        gameover('Die then. Don\'t come back.')
    else:
        gameover('You\'ll just die when you type anything else.')

def char_make():
    mixer.Channel(1).play(mixer.Sound('bgm\\chara_make.wav'), loops=-1)
    typing('Then, let\'s make your character.')
    sleep(5)
    typing('What is your name?')
    charaname = input()
    if charaname.lower() == "gaster":
        gaster_reboot()
    typing('What is your gender? (M/F)')
    gender = input()
    if gender.upper() != 'M' or gender.upper() != 'Y':
      gameover('Uhhh, what are you then?')
    typing('Please confirm your changes.')
    sleep(1)
    typing('Name: '+charaname)
    sleep(1)
    typing('Gender: '+gender)
    sleep(3)
    typing('Nah/...')
    chara_fakeconf = input()
    if chara_fakeconf == '...' or chara_fakeconf == '..':
      typing('Oh, aren\'t you satisfied?')
      sleep(2.3)
      typing('Then we\'ll use the default settings!')
      mixer.Channel(1).fadeout(5000)
      sleep(3)
      typing('GAME START', 'sans', 0.3)
    else:
        gameover('Wait, are you serious? I\'ll kill you for now.')

def gameover(message):
    mixer.Channel(1).play(mixer.Sound('bgm\\gameover.wav'))
    typing('GAME OVER', voice='default2', offset=0.6)
    sleep(3)
    typing(message, 'default2', 0.07)
    mixer.Channel(1).fadeout(5000)
    sleep(5)
    sys.exit()

def gaster_reboot():
    global reboot
    reboot += 1
    if reboot >= 3:
        gameover('Nope, don\'t play with him! Just die then.')
    char_make()

