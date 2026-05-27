#Sarah R
#Tortiose and the Hare

import random
#Initial Conditions
finish_line = 50 #Finish line
is_hare_asleep = False #hare starts awake
tortiose_wins = 0
hare_wins = 0

#Simulation loop
print("---- Tortiose and Hare Race simulation ----")
print("Ready...Set....Go!!!")
print("---The Race Beings!---")
for i in range(100000):
    tortiose_pos = 0 #Starting position
    hare_pos = 0 #Starting position

    while tortiose_pos < finish_line and hare_pos < finish_line:
        asleep_number = random.randint(1,100)
        if asleep_number <= 80:
            is_hare_asleep = True
            status = "sleep"
        else:
            is_hare_asleep = False
            hare_pos= hare_pos + random.randint(1,10)
            status = "run"
        tortiose_pos = tortiose_pos + random.randint(1,3)

    if tortiose_pos >= finish_line:
        tortiose_wins = tortiose_wins + 1
    else:
        hare_wins = hare_wins + 1
print(f"Tortiose wins: {tortiose_wins} | Hare wins: {hare_wins}")
