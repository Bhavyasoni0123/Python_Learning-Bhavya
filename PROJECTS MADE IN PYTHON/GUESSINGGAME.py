# GUESSING GAME...
import random
def play_game():
    Lucky_Number = random.randint(1 , 50)
    while True:
        User_Number = int(input('GUESS YOUR LUCKY NUMBER: '))
        if User_Number == Lucky_Number:
            print('CONGRATULATIONS YOU WON THE GAME')
            break
        elif User_Number < Lucky_Number:
            print('TOO LESS') 
        else:
            print('TOO HIGH')

    print('THANK YOU FOR PLAYING THE GAME')


play_game()        


    