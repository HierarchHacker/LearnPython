x = float(input('x = '))
if x > 1:
    y = 3 * x + 23
else:
    if x >= -1:
        y = 2 * x ** 2 - 78
    else:
        y = 3 * 23 + x
print(f'f({x:.4f}) = {y:.5f}')
'''以上为嵌套结构
以下为扁平化结构'''
score = float(input('Please input your score:'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('grade : ', grade)
# 三角形的周长和面积
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    C = a + b + c
    half = C / 2
    area = (half * (half - a) * (half - b) * (half - c)) ** 0.5
    print(f'C = {C:.2f}')
    print(f'area = {area:.3f}')
else:
    print('NO')
