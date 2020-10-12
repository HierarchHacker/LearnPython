# Print Fibonacci sequence.
# a, b = 1, 1
# print(a, b, end=' ')
# for _ in range(18):
#     a, b = b, a + b
#     print(b, end=' ')
# print()
# # Print prime.
# for num in range(2, 100):
#     is_prime = True
#     for factor in range(2, num):
#         if num % factor == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=' ')

# 阶乘代码
# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# fm_n = 1
# for num in range(1, m - n + 1):
#     fm_n *= num
# print(fm // fn // fm_n)

# 构造函数
# def f(num):
#     result = 1
#     for x in range(1, num + 1):
#         result *= x
#         return result
# # 函数和下面的代码应该空两行
#
#
# m = int(input('m = '))
# n = int(input('n = '))
# print(f(m) // f(n) // f(m - n))


# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# fm_n = 1
# for num in range(1, m - n + 1):
#     fm_n *= num
# print(fm // fn // fm_n)

# def f(num):
#     result = 1
#     for x in range(1, num + 1):
#         result *= x
#     return result
#
#
# m = int(input('m = '))
# n = int(input('n = '))
# print(f(m) // f(n) // f(m - n))


# def add(*args):
#     total = 0
#     for val in args:
#         total += val
#     return total
#
#
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 2, 4, 5, 6, 6, 4, 3))


import module
import module2


module.foo()
module2.foo()


abs(-1)
print(abs(-1))
