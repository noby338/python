# 迭代器，生成器

# 1、字符串创建迭代器对象
str = 'noby'
strIter = iter(str)

# 2、list对象创建迭代器
list = [l for l in range(2, 5)]  # 列表生成式创建一个列表
listIter = iter(list)

# 3、tuple(元祖) 对象创建迭代器
tuple = (1, 2, 3, 4)
tupleIter = iter(tuple)

# for 循环遍历迭代器对象
for x in strIter:
    print(x, end=' ')

print('\n------------------------')

# next() 函数遍历迭代器
while True:
    try:
        print(next(listIter), end=' ')
    except StopIteration:
        break

print('\n------------------------')

# 生成器(一种特殊的迭代器，只能被迭代一次)
# 如果列表元素可以按照某种算法推算出来，那我们可以在循环的过程中不断推算出后续的元素
gen = (t for t in range(3))
for g in gen:
    print(g, end=' ')
# 生成器只能被迭代一次
for g in gen:
    print(g, end=' ')
print(gen)

print('\n------------------------')


# generator 的函数，在每次调用 next() 的时候执行，遇到 yield语句返回，再次执行时从上次返回的 yield 语句处继续执行。
def odd():
    print('第一步', end=':')
    yield (1)
    print('第二步', end=':')
    yield (3)
    print('第三步', end=':')
    yield (5)


o = odd()
while True:
    try:
        print(next(o))
    except StopIteration:
        break


# 生成器实现斐波那契数列(生成器中的元素边执行，边生成，相对函数占用更少的内存)
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
# 与以上写法等同
# def fibon(n):
#     a = b = 1
#     i = iter(range(n))
#     while True:
#         try:
#             next(i)
#             yield a
#             a, b = b, a + b
#         except StopIteration:
#             break


# 函数实现斐波那契数列
def fibon2(n):
    a = b = 1
    list = []
    for i in range(n):
        a, b = b, a + b
        list.append(a)
    return list


print('\n生成器------------------------')
for x in fibon(100):
    print(x)


print('\n------------------------')
