# 函数
# def 函数名(参数1，参数2....参数n):
#     函数说明
#     函数体
#     return 结果

def doMath(i, i2, method='sum'):  # 第三个参数为默认参数(只能位于参数列表的后面)
    "这是一个用于两数加法的运算函数"
    if not (isinstance(i, (int, float)) and isinstance(i2, (int, float))):
        raise TypeError('参数类型错误')  # 抛出异常
    if method == 'sum':
        return '{}+{}'.format(i, i2), i+i2  # 可以返回多个值(多个值组成一个元组)
    elif method == 'sub':
        return '{}-{}'.format(i, i2), i-i2
    else:
        raise TypeError('参数类型错误')


print(doMath(2, 3))


# 可变长参数
def print_user_info(name,  age, * hobby):
    # 打印用户信息
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('爱好：{}'.format(hobby))
    return


print_user_info('noby', 18, '打篮球', '打羽毛球', '跑步')


# 强制关键字参数
def print_user_info2(*, name, age, sex='男'):
    # 打印用户信息
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex))
    return


print_user_info2(name='两点水', age=18, sex='女')

# 这种写法会报错，因为 age ，sex 这两个参数强制使用关键字参数
#print_user_info( '两点水' , 18 , '女' )
#print_user_info2('两点水', age='22', sex='男')


# 匿名函数 lambda
