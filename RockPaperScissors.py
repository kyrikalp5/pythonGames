import random
player_score = 0
computer_score = 0
r = 1

print('WELCOME TO ROCK PAPER SCISSOR GAME. LETS PLAY')

while True:
    player = input("Press 'r' for rock, 'p' for paper, 's' for scissors :")
    computer = random.choice(['r', 'p', 's'])
    print('You chose ' + player + ' while computer chose ' + computer)

    if player == computer:
        print('Tie. The score remains the same for round ' + str(r))
    elif (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        print('Player won round ' + str(r))
        player_score += 1
    else:
        print('Computer won round ' + str(r))
        computer_score += 1

    print('Player ' + str(player_score) + ' Computer ' + str(computer_score))
    if player_score == 5 or computer_score == 5:
        break;
    r += 1

if player_score > computer_score:
    print('\nPlayer won the game')
else:
    print('\nComputer won the game')
