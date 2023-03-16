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
e = input("[?] Your schoology email?: ")
d = input("[?] Your schoology password? (bruteforce attack wont work without it): ")
print("attempting to log into schoology with...\033[1;3m " + e)
time.sleep(4)
print("\033[32msuccessfully logged in as " + e + " [\u2713]")

c = input("[?] Victims schoology email?: ")
b = int(input("[?] How many passwords would you like to try?: "))
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

        print("\033[31m| attempting..." + randomnumber + randomnumber2 + randomnumber3 + randomnumber4 + randomnumber5 + randomnumber6 + randomUpperLetter + randomLowerLetter + " |", flush=True)
        time.sleep(0.00001)
