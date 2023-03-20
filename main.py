import random
import string
import time

print('''


\033[37m ▐▄▄▄ ▐▄▄▄ ▄▄· ▄▄▄  ▄▄▄▄· ▄▄▄  ▄• ▄▌▄▄▄▄▄▄▄▄ .
\033[34m  ·██  ·██▐█ ▌▪▀▄ █·▐█ ▀█▪▀▄ █·█▪██▌•██  ▀▄.▀·
▪▄ ██▪▄ ████ ▄▄▐▀▀▄ ▐█▀▀█▄▐▀▀▄ █▌▐█▌ ▐█.▪▐▀▀▪▄
▐▌▐█▌▐▌▐█▌▐███▌▐█•█▌██▄▪▐█▐█•█▌▐█▄█▌ ▐█▌·▐█▄▄▌
 ▀▀▀• ▀▀▀•·▀▀▀ .▀  ▀·▀▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀  ▀▀▀ 
   
        tiktok: jahsehrare
        insta: spookyle4n
''')

num_passwords = int(input("[?] How many passwords would you like to generate?: "))
start_attack = input("[?] Start Attack? [y/n]: ")

if start_attack.lower() == 'y':
    output_file = open('generated_passwords.txt', 'w')
    print("\033[31mStarting bruteforce on", num_passwords, "passwords:\033[37m")
    start_time = time.time()
    for i in range(num_passwords):
        random_numbers = ''.join(random.choices(string.digits, k=6))
        random_upper_letter = random.choice(string.ascii_uppercase)
        random_lower_letter = random.choice(string.ascii_lowercase)
        password = random_numbers + random_upper_letter + random_lower_letter
        print("\033[31m[!] attempting...", password, flush=True)
        output_file.write(password + '\n')
        time.sleep(0.000005)
    output_file.close()
    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes = int(elapsed_time / 60)
    seconds = int(elapsed_time % 60)
    milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)
    print(f"\033[34mGenerated passwords saved to generated_passwords.txt\n [+] Estimated time of finish: {minutes}m {seconds}s {milliseconds}ms")
    
    search_password = input("[?] Do you want to search for a specific password? [y/n]: ")
    if search_password.lower() == 'y':
        with open('generated_passwords.txt') as f:
            passwords = f.read().splitlines()
        password_to_search = input("[?] Enter the password to search for: ")
        if password_to_search in passwords:
            print("\033[32m[+] Password found in generated_passwords.txt")
