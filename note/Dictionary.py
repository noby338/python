# 字典

from email.mime.audio import MIMEAudio


myDict = {
    'name': 'noby',
    'age': 20,
}
myDict['age'] = 21
myDict['gender'] = 'male'
print("myDict['age']:",myDict['age'])
print(myDict)
print("随机取出一个键值对(删除)",myDict.popitem())
print("返回字典中的所有值",myDict.values())
print("返回字典中的所有键值",myDict.items())

# 删除某一字典元素
del myDict['name']
# 清除字典
myDict.clear()
# 删除字典
del myDict

# dict （字典）键必须不可变，可是键可以用数字，字符串或元组充当，但是就是不能使用列表
