from random import seed
from random import randint
import time
import random
import string
print('''
\033[34m ▐▄▄▄ ▐▄▄▄ ▄▄· ▄▄▄  ▄▄▄▄· ▄▄▄  ▄• ▄▌▄▄▄▄▄▄▄▄ .
\033[37m  ·██  ·██▐█ ▌▪▀▄ █·▐█ ▀█▪▀▄ █·█▪██▌•██  ▀▄.▀·
        ▪▄ ██▪▄ ████ ▄▄▐▀▀▄ ▐█▀▀█▄▐▀▀▄ █▌▐█▌ ▐█.▪▐▀▀▪▄
        ▐▌▐█▌▐▌▐█▌▐███▌▐█•█▌██▄▪▐█▐█•█▌▐█▄█▌ ▐█▌·▐█▄▄▌
        ▀▀▀• ▀▀▀•·▀▀▀ .▀  ▀·▀▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀  ▀▀▀ 
   
               tiktok jahsehrare
               insta: spookyle4n
''')

b = int(input("[?] How many passwords would you like to generate?: "))
a = input("[?] Start Attack? [y/n]: ")
if a == 'y':
    print("\033[31mStarting bruteforce on " + c + " passwords:\033[37m " + d)
    time.sleep(2)
    for i in range(b):
        randomnumber = chr(random.randint(ord('0'), ord('9')))
        randomnumber2 = chr(random.randint(ord('0'), ord('9')))
        randomnumber3 = chr(random.randint(ord('0'), ord('9')))
        randomnumber4 = chr(random.randint(ord('0'), ord('9')))
        randomnumber5 = chr(random.randint(ord('0'), ord('9')))
        randomnumber6 = chr(random.randint(ord('0'), ord('9')))
        randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
        randomLowerLetter = chr(random.randint(ord('a'), ord('z')))

        print("\033[31m attempting..." + randomnumber + randomnumber2 + randomnumber3 + randomnumber4 + randomnumber5 + randomnumber6 + randomUpperLetter + randomLowerLetter + " |", flush=True)
        time.sleep(0.00001)
