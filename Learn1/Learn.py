print('hello world')
# 这是单行注释
print('Hierarch')
'''多行注释
哈哈哈'''
a = 35
b = 12.345
c = 'hello world'
a += b
print(a)
a *= b
print(a)
print(a != b)
# 比较运算符的优先级高于赋值运算符
# 计算年份是否为闰年
year = int(input('请输入年份：'))
is_leap_year = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap_year)
