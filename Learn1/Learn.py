import random   # 此为导入random模块，导入后需要空一行再写代码
# 此为空出来的一行
print(random.random())    # 随机生成一个0~1的浮点数
print(random.uniform(3, 4))    # 随机生成3~4的浮点数
print(random.randint(0, 100))    # 随机生成0~100的整数
print(random.randrange(1, 100, 2))   # 随机生成1~100的奇数，2为步长
print(random.choice(['as', 2, 5, 7]))    # 随机选择 as，2，5，7中的任一字符，
print(random.choice('dksajfla'))    # 随机生成dksajfla中的任一字符
x = list(range(1, 10))  # 生成一个1，10区间的整数列表，前闭后开
print(x)
random.shuffle(x)   # 此为洗牌，即打乱列表中的顺序
print(x)
y = list(range(2, 14))
print(y)
s = random.sample(x, 4)  # 样品抽取，从指定序列中随机获取指定长度的片段。4，为获取的长度
print(s)
