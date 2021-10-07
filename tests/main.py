from time import sleep # the module that has the ability of The World
import sys # for killing the program when GAME OVERed
import os

reboot = 0

def typing(words, voice='default', offset=0.1): # typing effect
    for char in words:
        sleep(offset)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()

def game_start():
    typing('始めたいなら「y」', 'default')
    shoken1 = input()
    if shoken1 == 'y':
        gameover('ちなみに外来語使うと死ぬよー')
    elif shoken1 == '':
        typing('または「始める」を入力')
        gamestart = input('')
        if gamestart == '始める' or gamestart == 'はじめる':
            text_sound('select')
            char_make()
        else:
            gameover('うん。変なの入力するな。')
    else:
        gameover('なんでも入力したところで死ぬよ')

def char_make():
    typing('あなたのキャラクターを作成します。')
    sleep(5)
    typing('キャラクターの名前は?')
    charaname = input()
    if charaname.lower() == "gaster" or charaname == "ガスター" or charaname == "がすたー":
        gaster_reboot()
    typing('男性、それとも女性?')
    gender = input()
    typing('以上でよろしいですか?')
    sleep(1)
    typing('名前: '+charaname)
    sleep(1)
    typing('性別: '+gender)
    sleep(3)
    typing('OK/...')
    chara_fakeconf = input()
    if chara_fakeconf == 'OK':
        gameover('OKって英語だよねー？')
    elif chara_fakeconf == '...' or chara_fakeconf == '..':
        typing('あれ、何か不満？')
        sleep(2.3)
        typing('だったらこっちで準備した設定でやるねー')
        sleep(3)
        typing('GAME START', 'sans', 0.3)
    elif chara_fakeconf == "":
        gameover('いやいや、真面目に聞いてる?　とりあえず殺したから！')
    else:
        gameover('なんでも入力した＝死だから…')

        
def gameover(message):
    typing('GAME OVER', voice='default2', offset=0.6)
    sleep(3)
    typing(message, 'default2', 0.07)
    sleep(5)
    sys.exit()

def gaster_reboot():
    global reboot
    reboot += 1
    if reboot >= 3:
        gameover('お前らさーガスヒカリで遊ぶなよ！ということで殺します。')
    char_make()

game_start()
