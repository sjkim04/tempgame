from time import sleep # the module that has the ability of The World
import sys # for killing the program when GAME OVERed

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # hiding that f**king annoying message

from pygame import mixer # playing BGMs and SEs
mixer.init()

reboot = 0

def type(words, voice='default', offset=0.1): # typing effect
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
    type('始めたいなら「y」', 'default')
    shoken1 = input()
    if shoken1 == 'y':
        gameover('ちなみに外来語使うと死ぬよー')
    elif shoken1 == '':
        type('または「始める」を入力')
        gamestart = input('')
        if gamestart == '始める' or gamestart == 'はじめる':
            text_sound('select')
            char_make()
        else:
            gameover('うん。変なの入力するな。')
    else:
        gameover('なんでも入力したところで死ぬよ')

def char_make():
    mixer.Channel(1).play(mixer.Sound('bgm\\chara_make.wav'), loops=-1)
    type('あなたのキャラクターを作成します。')
    sleep(5)
    type('キャラクターの名前は?')
    charaname = input()
    if charaname == "Gaster" or charaname == "gaster" or charaname == "ガスター" or charaname == "がすたー":
        gaster_reboot()
    type('男性、それとも女性?')
    gender = input()
    type('以上でよろしいですか?')
    sleep(1)
    type('名前: '+charaname)
    sleep(1)
    type('性別: '+gender)
    sleep(3)
    type('OK/...')
    chara_fakeconf = input()
    if chara_fakeconf == 'OK':
        gameover('OKって英語だよねー？')
    elif chara_fakeconf == '...' or chara_fakeconf == '..':
        type('あれ、何か不満？')
        sleep(2.3)
        type('だったらこっちで準備した設定でやるねー')
        mixer.Channel(1).fadeout(5000)
        sleep(3)
        type('GAME START', 'sans', 0.3)
    elif chara_fakeconf == "":
        gameover('いやいや、真面目に聞いてる?　とりあえず殺したから！')
    else:
        gameover('なんでも入力した＝死だから…')

        
def gameover(message):
    mixer.Channel(1).play(mixer.Sound('bgm\\gameover.wav'))
    type('GAME OVER', voice='default2', offset=0.6)
    sleep(3)
    type(message, 'default2', 0.07)
    mixer.Channel(1).fadeout(5000)
    sleep(5)
    sys.exit()

def gaster_reboot():
    global reboot
    reboot += 1
    if reboot >= 3:
        gameover('お前らさーガスヒカリで遊ぶなよ！ということで殺します。')
    char_make()

game_start()
