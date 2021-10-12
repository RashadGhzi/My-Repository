from random import randint

if __name__ == '__main__':
    player_1 = input('Enter the name of first player:\n')
    player_2 = input('Enter the name of second player:\n')
    player_list = [player_1, player_2]

    chance_num = 5
    player_round1 = 0
    player_round2 = 0
    player_round = [player_round1, player_round2]

    run = 0
    while run < 2:
        random_num = randint(1, 20)
        print('Guesse the number from 1 to 20.')
        print(f'{player_list[run]} you have 5 more round to guess the correct number.')
        print(f'{player_list[run]} guess your number.')

        i = 0
        while i < 5:
            try:
                guess_num = int(input(f'Round No.{i+1}:\n'))
            except Exception:
                print('Enter the intiger number.')
                continue

            if guess_num == random_num:
                print('Congratulation! You guessed the correct number.\n')
                if player_list[run] == player_1:
                    player_round1=i + 1
                else:
                    player_round2=i + 1
                break

            elif guess_num < random_num:
                print(
                    'Your number is less then actual number. \nEnter greater number.\n')

            else:
                print(
                    'Your number is greater then actual number. \nEnter less number.\n')

            if i == 3:
                print('You have one more round to guess the actual number.')
            
            i += 1
        run += 1


    if (player_round1 == player_round2) & (player_round1 != 0):
        print('You both won the game.')

    elif (player_round1) > (player_round2 == 0):
        print(f"{player_1} guessed the number in the round of {player_round1}. \n{player_2} guessed the number in the round of {player_round2}\n"
              f"{player_1} won the game.\n")

    elif (player_round1==0) < (player_round2):
        print(f"{player_1} guessed the number in the round of {player_round1}. \n{player_2} guessed the number in the round of {player_round2}\n"
              f"{player_2} won the game.\n")

    elif (player_round1 == 0) and (player_round2 == 0):
        print("You both lose the game.")

    elif (player_round1 < player_round2):
        print(f"{player_1} guessed the number in the round of {player_round1}. \n{player_2} guessed the number in the round of {player_round2}\n"
              f"{player_1} won the game.\n")

    elif (player_round1 > player_round2):
        print(f"{player_1} guessed the number in the round of {player_round1}. \n{player_2} guessed the number in the round of {player_round2}\n"
              f"{player_2} won the game.\n")

    else:
        print('good luck bey')
