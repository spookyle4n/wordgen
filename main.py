from random import seed
from random import randint
import time
import random
import string
print('''
\033[34m 
  _____     _____
 /____/|   /____/|_______________________________
|    | |  |    |/________/___________/_________\\ \\
|    | |  |    |   ___   |     __    |    ___   \\_\\
|    | /\ |    |  |   |  |    | |\\___|   |   |  | |
|    |/  \|    |  |___|  |    | |    |   |___|  |_|
 \             /         |    | |    |          / /
\033[37m   \___________/__________|____|_|    |_________/_/
   
               tiktok jahsehrare
               insta: spookyle4n
''')
b = int(input("[?] How many passwords would you like to generate?: "))
a = input("[?] Generate wordlist? [y/n]: ")
if a == 'y':
    for i in range(b):
        randomnumber = chr(random.randint(ord('0'), ord('9')))
        randomnumber2 = chr(random.randint(ord('0'), ord('9')))
        randomnumber3 = chr(random.randint(ord('0'), ord('9')))
        randomnumber4 = chr(random.randint(ord('0'), ord('9')))
        randomnumber5 = chr(random.randint(ord('0'), ord('9')))
        randomnumber6 = chr(random.randint(ord('0'), ord('9')))
        randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
        randomLowerLetter = chr(random.randint(ord('a'), ord('z')))

        print(randomnumber + randomnumber2 + randomnumber3 + randomnumber4 + randomnumber5 + randomnumber6 + randomUpperLetter + randomLowerLetter, flush=True)
        time.sleep(0.000001)
