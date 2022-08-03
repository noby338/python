# 条件和循环


score = float(input("请输入一个分数: "))
if isinstance(score, int) and score > 90:
    print('优秀')
elif isinstance(score, int) and score > 60:
    print('良好')
else:
    print('不及格')

print('--------------')
for s in 'info':
    print(s, end=',')
else:
    print()

print('--------------')
for k in {'name': 'noby', 'age': 20}:
    print(k)

print('--------------')
for v in {'name': 'noby', 'age': 20}.values():
    print(v)

print('--------------')
for s in ({'one', 'tow', 'three'}):
    print(s)

print('--------------')
for r in range(1, 5, 2):  # range(开始值，结束值，递增数量)
    print(r)

print('-------------')
i = 0
while i < 3:
    print('good', end=',')
    i += 1

# next() 函数遍历迭代器
print('\n-------------')
iterator = iter('kace')
while True:
    try:
        print(next(iterator), end=' ')
    except StopIteration:
        break

print('\n-------------')
# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        # 打印语句中，大括号及其里面的字符 (称作格式化字段) 将会被 .format() 中的参数替换
        # print('{}x{}={}\t'.format(i, j, i*j), end='') 
        print(f'{i}x{j}={i*j}\t', end='')
    print()
