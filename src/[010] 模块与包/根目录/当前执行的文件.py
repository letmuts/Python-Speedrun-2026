import name_3 as n3  # 导入了 3
import 文件夹1  # 导入了 __init__ 导入了 1
import 文件夹1.__main__  # 导入了 __main__

# 刚才导入过包了，所以 __init__.py 不会执行第二次
from 文件夹1 import name_2  # 导入了 2

n3.fun_3_1()  # 函数名: fun_3_1

name_2.fun_2_1()  # 函数名: fun_2_1

文件夹1.fun_1_1()  # 函数名: fun_1_1

# 不会执行 __main__ 中 if __name__ == "__main__" 的内容
print(文件夹1.__main__.__name__)  # 文件夹1.__main__
