username = input('Please input your username:')
password = input('Please input your password:')
if username == 'Hierarch' and password == '123456':
    print('Yes!Hierarch,welcome!')
else:
    print('What the fuck are you?')
'''多分支结构'''
x = float(input('x = '))
if x > 1:
    y = 3 * x + 5
elif x >= -1:
    y = 4 * x - 3
else:
    y = x ** 2 - 213
print(f'f({x:.3f}) = {y:.4f}')
