for num in range(100, 1000):
    ge = num % 10
    shi = num // 10 % 10
    bai = num // 100
    if num == ge ** 3 + shi ** 3 + bai ** 3:
        print(num)
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if x * 5 + 3 * y + z == 100:
            print(x, y, z)
            