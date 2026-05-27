#Sarah R
#Tortiose and the Hare

import random
#Initial Conditions
finish_line = 50 #Finish line
tortiose_pos = 0 #Starting position
hare_pos = 0 #Starting position
is_hare_asleep = False #hare starts awake

#Simulation loop

print("---- Tortiose and Hare Race ----")
print("Ready...Set....Go!!!")
print("---The Race Beings!---")
while tortiose_pos < finish_line and hare_pos < finish_line:
    asleep_number = random.randint(1,100)
    if asleep_number <= 30:
        is_hare_asleep = True
        status = "sleep"
    else:
        is_hare_asleep = False
        hare_pos= hare_pos + random.randint(1,10)
        status = "run"
    tortiose_pos = tortiose_pos + random.randint(1,3)

    print(f"Tortoise: {tortiose_pos} | Hare: {hare_pos}({status})")
if tortiose_pos >= finish_line:
    print("🐢 The tortiose Wins!")
else:
    print("🐇 The Hare Wins!")
