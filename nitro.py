import requests
import random
import string
import time

print(""" 
NITRO GEN + CHECKER | BY WORLDWARRIOR |
                                                """)
time.sleep(2)
print("GET YOUR VALID NITROS AT VALID CODES.TXT")
time.sleep(0.3)
print("MADE BY WORLDWARRIOR\n\n")
time.sleep(0.2)

num = int(input('HOW MANY CODES YOU WANT : '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("STATUS : OK")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"GENERATED {num} CODES | TIME TAKEN : {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Valid | {nitro} ")
            break
        else:
            print(f" Invalid | {nitro} ")

input("\nCHECK VALID CODES.TXT FOR VALID CODES")
