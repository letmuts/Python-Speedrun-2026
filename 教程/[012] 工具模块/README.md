# [math](https://docs.python.org/zh-cn/3/library/math.html)

```python
import math

print(math.sin(math.pi / 2))  # 1.0

print(math.log(math.e))  # 1.0
print(math.log10(10**6))  # 6.0

a, b = 123, 4
print(math.pow(a, b) == a**b == pow(a, b))  # True
```

`math` 内有大量数学函数和常量，需要时查文档，不过多赘述

# [random](https://docs.python.org/zh-cn/3/library/random.html)

*若需安全随机数，使用 [secrets](https://docs.python.org/zh-cn/3/library/secrets.html) 模块*

```python
import random

print(random.randint(9, 88))  # int [9, 88]
print(random.random())  # float [0, 1)
print(random.uniform(10, 20.5))  # float [10, 20.5]

print(random.binomialvariate())  # 二项式分布
print(random.gauss())  # 正态分布

# 随机打乱
a = [1, 2, 3, 4, 5, 6]
random.shuffle(a)
print(a)
```

`random` 内有大量随机数生成方式，建议简单看一遍文档，有个大致印象

# [itertools](https://docs.python.org/zh-cn/3/library/itertools.html)

```python
import itertools

a = [1, 2, 3, 4]
b = [7, 8, 9]

res1 = []
for v in itertools.chain(a, b):
    res1.append(v)
print(res1)  # [1, 2, 3, 4, 7, 8, 9]

res2 = []
for v in itertools.chain.from_iterable([a, b]):
    res2.append(v)
print(res2)  # [1, 2, 3, 4, 7, 8, 9]

res3 = []
num = 0
for v in itertools.cycle(b):
    if num > 9:
        break
    res3.append(v)
    num += 1
print(res3)  # [7, 8, 9, 7, 8, 9, 7, 8, 9, 7]

print(list(zip(a, b)))  # [(1, 7), (2, 8), (3, 9)]
print(list(itertools.zip_longest(a, b)))  # [(1, 7), (2, 8), (3, 9), (4, None)]
```

`itertools` 用于创建各种迭代器，实战中非常常用

迭代器拼接与切割、惰性求值、排列组合、累计计算，有这些需求时查询该模块文档

# [collections](https://docs.python.org/zh-cn/3/library/collections.html)

Python 除了内置容器类型，还提供了这个容器模块

排序、映射、统计、基类，有这些需求时查询该模块文档

```python
from collections.abc import Callable, Collection, Iterable
import itertools


def f1(_: Iterable):
    pass


def f2(_: Collection):
    pass


def f3(_: Callable[[Iterable], None]):
    pass


a = []
b = itertools.chain(a, [])


def c(_: Iterable) -> None:
    pass


f1(a)
f1(b)

f2(a)
f2(b)  # Pylance 报错

f3(lambda a: None)
f3(c)
```

前面文章中介绍可迭代对象时就用到过这个模块，最常用的部分也是基类

# [functools](https://docs.python.org/zh-cn/3/library/functools.html)

偏函数、装饰器、缓存，有这些需求时查询该模块文档

建议简单看一遍文档，有个大致印象
