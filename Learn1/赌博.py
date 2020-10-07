from random import randint

money = 1000
while money > 0:
    print(f'You have {money} dollar.')
    go_on = False
    while True:
        debt = int(input('Please make your debt:'))
        if 0 < debt <= money:
            break
    # first
    while True:
        player = randint(1, 6) + randint(1, 6)
        print(f'Player:{player}')
        if player == 7 or player == 11:
            print('Congratulations!')
            money += debt
            break
        elif player == 2 or player == 3 or player == 12:
            print('Zhuang win!')
            money -= debt
            break
        else:
            go_on = True
            while go_on:
                player2 = randint(1, 6) + randint(1, 6)
                print(f'player:{player2}')
                if player2 == player:
                    print('Congratulations!')
                    money += debt
                    go_on = False
                elif player2 == 7:
                    print('Zhuang win!')
                    go_on = False
                    money -= debt
                else:
                    go_on = True
        print()
        break

print('Poor Guy!')
