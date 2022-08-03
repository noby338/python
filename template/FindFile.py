# 使用系统模块
import os

path = "D:/null/dirt"
files = os.listdir(path)

for f in files:
    if '23-16-35' in f and f.endswith('.png'):
        print(f'found it :{f}')

