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
一下为扁平化结构'''
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
