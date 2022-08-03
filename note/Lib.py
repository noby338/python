# 模块

from sys import version,path # 部分的导入某个模块的属性
from sys import * # 导入某个模块的所有属性(不推荐过多使用)
import math # 导入整个模块
import luigi

print(math.pi)
print(luigi.__file__) # 查看包的路径
print(version)
print(path) # 系统中模块存在的所有路径
print(executable)


print('\n--------------')
# 主模块与非主模块
print("是不是主模块？",__name__=='__main__') # __name__是系统给出的变量，用于判断本模块是否为主模块
print("__name__:",__name__)

str='info' # 用于 Lib2 导入模块引用测试
