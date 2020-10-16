# num = int(input('Please input a N*:'))
# end = int(num ** 0.5)
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print(f'{num} is prime.')
# else:
#     print(f'{num} is not prime.')
# 以上为素数重学版

# 寻找水仙花数
# for x in range(100, 1000):
#     bai = x // 100
#     shi = x % 100 // 10
#     ge = x % 10
#     if bai ** 3 + shi ** 3 + ge ** 3 == x:
#         print(x)
# 妙啊，竟然写出来了！

# num = int(input('num = '))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(reversed_num)
# nb，以上为颠倒数字，12345 ==> 54321

# for male in range(0, 21):
#     for female in range(0, 34):
#         little = 100 - male - female
#         if male * 5 + female * 3 + little / 3 == 100 and little % 3 == 0:
#             print(f'male:{male},female:{female},little:{little}')
# 买鸡题

from random import randint

money = 1000
while money > 0:
    print(f'你的资产为：{money}元')
    go_on = False
    while True:
        debt = int(input('请下注:'))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print(f'\n玩家摇出了{first}点')
    if first == 7 or first == 11:
        print('玩家胜!\n')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!\n')
    else:
        go_on = True
    while go_on:
        go_on = False
        current = randint(1, 6) + randint(1, 6)
        print(f'玩家摇出了{current}点')
        if current == 7:
            print('庄家胜！\n')
            money -= debt
        elif current == first:
            print('玩家胜！\n')
            money += debt
        else:
            go_on = True
print('你破产了！')


# import module
# import module2
#
#
# module.foo()
# module2.foo()
