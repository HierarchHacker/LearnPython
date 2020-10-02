import random

answer = random.randint(1, 11)
counter = 0
while True:  # 此步while true并不是“如果正确”，而是构造了一个条件恒成立的循环，也就意味着如果不做特殊处理，循环不会结束
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print('Bigger')
    elif number > answer:
        print('Smaller')
    else:
        print('Congratulation!')
        break
print(f'Counter = {counter}')
'''以上为break的用法，作用是提前结束循环
另一个关键字是continue，可以i放弃本次循环后续的代码直接让循环进入下一轮'''
for i in range(1,10):
    for j in range(1,i + 1):
        print(f'{i} * {j} = {i * j}', end='\t')
    print()
