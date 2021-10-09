from time import sleep # the module that has the ability of The World
import sys # for killing the program when GAME OVERed

reboot = 0

def typing(words, voice='default', offset=0.1): # typing effect
    for char in words:
        sleep(offset)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()

def game_start():
    typing('Type \'y\'', 'default')
    shoken1 = input()
    if shoken1 == 'y':
        gameover('Yeah, this IS a troll game.')
    elif shoken1 == '':
        typing('or \'Start\' to start')
        gamestart = input('')
        if gamestart.lower() == 'start':
            char_make()
        else:
            gameover('Yep. Don\'t enter anything else.')
    else:
        gameover('You\'ll just die when you type anything else.')

def char_make():
    typing('Then, let\'s make your character.')
    sleep(5)
    typing('What is your name?')
    charaname = input()
    if charaname.lower() == "gaster":
        gaster_reboot()
    typing('What is your sexuality? (M/F)')
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
      sleep(3)
      typing('GAME START', 'sans', 0.3)
    else:
        gameover('Wait, are you serious? I\'ll kill you for now.')

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
        gameover('Nope, don\'t play with him! Just die then.')
    char_make()
