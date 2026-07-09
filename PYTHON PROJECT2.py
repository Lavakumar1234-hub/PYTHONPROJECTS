import random
user_input=int(input("ENTER YOUR CHOICE TYPE 0 FOR ROCK,TYPE 1 FOR PAPER,TYPE 2 FOR SCISSOR :"))
if user_input >= 3 or user_input<0:
    print("YOU LOOSE")
else:
    computer_input=random.randint(0,2 )
    print("COMPUTER CHOICE :",computer_input)
    if user_input==0 and computer_input==2:
        print("YOU WIN")
    elif user_input==2 and computer_input==0:
        print("YOU LOSS")
    elif user_input > computer_input:
        print("YOW WIN")
    elif computer_input > user_input:
        print("YOU LOSE")
    else:
        print("ITS A DRAW")

