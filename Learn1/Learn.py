import random

answer = random.randint(1, 11)
counter = 0
while True:
    player = int(input('Please input your answer:'))
    counter += 1
    if player < answer:
        print('Bigger!')
    elif player > answer:
        print('Smaller!')
    else:
        print('Congratulations!')
        break
print(f'Counter = {counter}')
