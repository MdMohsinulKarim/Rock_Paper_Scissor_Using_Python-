import random
import os

while(True):
    os.system("cls")
    Player = int(input("1.Rock\n2.Paper\n3.Scissor\n\n\t:"))
    Opponent = random.randint(1,3)
    if Player==1 and Opponent==1:
        print(f"{Player} Draw {Opponent}")
    elif Player==2 and Opponent==1:
        print(f"{Player} Player wins {Opponent}")
    elif Player==3 and Opponent==1:
        print(f"{Player} Opponent wins {Opponent}")
    elif Player==1 and Opponent==2:
        print(f"{Player} Opponent wins {Opponent}")
    elif Player==2 and Opponent==2:
        print(f"{Player} Draw {Opponent}")
    elif Player==3 and Opponent==2:
        print(f"{Player} Player wins {Opponent}")
    elif Player==1 and Opponent==3:
        print(f"{Player} Player wins {Opponent}")
    elif Player==2 and Opponent==3:
        print(f"{Player} Opponent wins {Opponent}")
    elif Player==3 and Opponent==3:
        print(f"{Player} Draw {Opponent}")
    elif Player==-1:
        exit()
    else:
        continue
    os.system("pause")