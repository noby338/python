# 列表

myList = ['one', 'tow', 'three', 'four', 'five']
myList2 = ['1', '2', '3', '4', '5']
myList3 = list(range(1, 4))  # 通过 list() 函数和 range() 函数生成 list
myList4 = [l ** 2 for l in range(0, 7) if l % 2 == 0]  # list 生成式(** 表示次方)
myList5 = [(x, y) for x in range(3) for y in range(30) if y % 10 == 0]
myList.append('four')
del myList[0]
print("输出某一元素：", myList[0])
print("输出最后一个元素：",myList2[-1])
print("输出[:3]范围的元素：", myList[:3])
print("输出[2:]范围的元素：", myList[2:])
print("输出[1:3]范围的元素：", myList[1:3])
print("输出整个列表：", myList)
print("两列表相加生成新的列表：", myList+myList2)
print("生成该列表的多倍元素的列表：", myList2*2)
print("MyList 列表中是否存在 six 元素：", 'six' in myList)
print("列表的长度：", len(myList))
print("列表的最大值，最小值：", max(myList2), min([1, 2, 3]))  # 可自动将字符串转换为数字
print("tow 出现在 MyList 中的次数：", myList.count('tow'))
print("第一个匹配的索引位置：", myList.index('tow'))
print("指定位置插入元素：", myList.insert(2, 'insert'))
print("排序列表(False 为升序)：", myList3.sort(reverse=False))

# 迭代
for x in myList3:
    print(x, end=' ')
print('\n-----------')
# 反向迭代
for x in reversed(myList3):
    print(x, end=' ')
print('\n-----------')

# 同时迭代多个序列
# zip() 函数生成一个元组迭代器，迭代长度跟参数中最短序列长度一致
for x,y in zip(myList2,myList5):
    print(x,y)
print('\n-----------')
print("myList3:", myList3)
print("myList4:", myList4)
print("myList5:", myList5)
print("mylist:", myList)








