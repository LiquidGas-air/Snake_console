from time import sleep
from keyboard import is_pressed as check
from random import randint as rand
import copy
pole = [[' ']*11 for i in range(9)]

s= {
    'w':0,
    'a':0,
    's':0,
    'd':0
}
snake = [[rand(0, 10), rand(0, 8)]]
fruit = [rand(0,10), rand(0,8)]
a = True

def zero(speed):
    for i in speed.keys():
        speed[i]=0


while True:
    sleep(1/5)

    if check('a') and s['d'] != 1:
        zero(s)
        s['a']= -1

    if check('d') and s['a'] != -1:
        zero(s)
        s['d'] = 1

    if check('s') and s['w'] != -1:
        zero(s)
        s['s'] = 1

    if check('w') and s['s'] != 1:
        zero(s)
        s['w'] = -1


    for i in range(len(pole)):
        for g in range(len(pole[i])):
            pole[i][g]=' '

    pole[fruit[1]][fruit[0]]='*'

    snake_c = copy.deepcopy(snake)

    for i in range(len(snake)):
        if i==0:
            continue
        snake[i][0]= snake_c[i-1][0]
        snake[i][1]= snake_c[i-1][1]

    snake[0][0] += s['a']
    snake[0][0] += s['d']
    snake[0][1] += s['w']
    snake[0][1] += s['s']



    if fruit[0] == snake[0][0] and fruit[1] == snake[0][1]:
        fruit = [rand(0, 10), rand(0, 8)]
        if s['a'] == -1:
            a = snake[-1][0] + 1
            b = snake[-1][1]
        if s['w'] == -1:
            a = snake[-1][0]
            b = snake[-1][1] + 1
        if s['s'] == 1:
            a = snake[-1][0]
            b = snake[-1][1] - 1
        if s['d'] == 1:
            a = snake[-1][0] - 1
            b = snake[-1][1]
        snake.append([a,b])

    if len(snake)>1:
        for i in range(1, len(snake)):
            if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                print("YOU LOST")
                exit()

    if (snake[0][0] < 0 or snake[0][0] > 10) or (snake[0][1] < 0 or snake[0][1] > 8) :
        print("YOU LOST")
        exit()


    for i in snake:
        pole[i[1]][i[0]] = '0'

    for i in pole:
        for g in i:
            print(g, end=' ')
        print()
    print('-------------')
    print('-------------')