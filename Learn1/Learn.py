for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i} * {j} = {i * j}', end='\t')
    print()
num = int(input('请输入一个整数：'))
end = int(num ** 0.5)
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')
