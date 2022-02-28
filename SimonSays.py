import random
import cv2 as cv
import numpy as np

height = width = 600
moves = np.array([], dtype='int')
flag = repeat = score = i = 0
cnt = stage = 1
life = 3

print('WELCOME TO SIMON SAYS GAME')
print('Lets Play')
level = int(input('for beginner press 1 // for pro press 2 // for world class press 3 :'))
if level == 1:
    time = 4000
elif level == 2:
    time = 3000
else:
    time = 2000

# Game begin
while True:
    if stage == 1:
        print('LEVEL ' + str(stage) + ' // ' + str(stage) + ' move')
    else:
        print('LEVEL ' + str(stage) + ' // ' + str(stage) + ' moves')
        print('Current score : ' + str(score))
    if stage <= 5:
        val = 10
    elif stage <= 10:
        val = 100
    else:
        val = 1000

    # Chose randomly Simon moves
    while True:
        x = random.randint(0, 4)
        color = np.zeros((height, width, 3), dtype='uint8')

        if x == 1:
            color[:height//2, :width//2] = 255, 0, 0
        elif x == 2:
            color[:height//2, width//2:] = 0, 255, 0
        elif x == 3:
            color[height//2:, :width//2] = 0, 0, 255
        elif x == 4:
            color[height//2:, width//2:] = 255, 0, 255
        elif x == 0:
            cv.circle(color, (width//2, height//2), 50, (0, 255, 255), thickness=-1)

        cv.imshow('Simon says', color)
        cv.waitKey(time)
        moves = np.append(moves, np.array([x]))
        #print(moves)

        cnt += 1
        if cnt > stage:
            break;

    cv.destroyAllWindows()

    while True:
        y = int(input('Give ' + str(i+1) + 'th move: '))
        repeat = 0
        if y != moves[i]:
            life -= 1
            if life == 0:
                print('\nWrong move // THE END')
                flag = 1
                break;
            else:
                print('Wrong move // ' + str(life) + ' lives left // Play again level ' + str(stage))
                for j in range(len(moves)):
                    color = np.zeros((height, width, 3), dtype='uint8')
                    if moves[j] == 1:
                        color[:height // 2, :width // 2] = 255, 0, 0
                    elif moves[j] == 2:
                        color[:height // 2, width // 2:] = 0, 255, 0
                    elif moves[j] == 3:
                        color[height // 2:, :width // 2] = 0, 0, 255
                    elif moves[j] == 4:
                        color[height // 2:, width // 2:] = 255, 0, 255
                    elif moves[j] == 0:
                        cv.circle(color, (width // 2, height // 2), 50, (0, 255, 255), thickness=-1)
                    cv.imshow('Simon says', color)
                    cv.waitKey(time)
                cv.destroyAllWindows()
                repeat = 1
                i = 0
        if repeat == 0:
            i += 1
            if i == cnt - 1:
                score += val * i
                i = 0
                break;

    moves = np.array([], dtype='int')
    cnt = 1
    stage += 1
    if flag == 1:
        break;

print('Total score ' + str(score))
print('Congratulations')
