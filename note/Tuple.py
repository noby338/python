# 元组

myTuple = ('one', 'tow', 'three', 'four', 'five')
myTuple2 = ('1', '2', '3', '4', '5')
myTuple3 = (2, 1, 3)
myTuple4 = (0,)  # 元组只有一个元素时，元素结尾使用','，以便以与运算符'()'进行区分

# myTyple[0]=3 元组的元素值不可以被修改
print(myTuple[0])
print(myTuple[1:3])
print(myTuple4)

# 删除元组
del myTuple4

# 列表转换为元组
alist = tuple(myTuple)
print("列表转换为元组", alist)

# 元组转换为列表
aTuple = list(alist)
print("元组转换为列表", aTuple)
