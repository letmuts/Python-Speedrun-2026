# 循环语句

如果想让一个块执行 n 遍，可以通过复制 n 个块解决，但不可能有人这么写

Python 有两个用于循环的关键字 `for` `while`

## while

`while` 比较简单，条件为 True 则继续，否则终止

```python
a: int = 3
while a:
    print(a)  # 3 2 1
    a -= 1
```

与 `if` 一样，条件对象会隐式转为 bool 类型

## for

`for` 涉及可迭代对象

所谓 `迭代`，就是逐个遍历元素

```python
from collections.abc import Iterable, Iterator, Sequence

a: list[int] = [3, 6, 9]
b: set[int] = {5, 7, 8}


def f1(a: Iterable):
    # 可迭代对象
    for v in a:
        print(v)


def f2(a: Sequence):
    # 序列
    for v in a:
        print(v)


def f3(a: Iterator):
    # 迭代器
    for v in a:
        print(v)


f1(a)  # 3 6 9
f1(b)  # 8 5 7 （乱序）
f1(v for v in a)  # 3 6 9

f2(a)  # 3 6 9
f2(b)  # Pylance 报错
f2(v for v in a)  # Pylance 报错

f3(a)  # Pylance 报错
f3(b)  # Pylance 报错
f3(v for v in a)  # 3 6 9
```

`for 元素 in 可迭代对象` 是 `for` 的基本语法

# 可迭代对象

常见类型继承关系表（大量省略）

```
Iterable (可迭代对象)
├─ Sequence (序列)
│  ├─ list
│  ├─ tuple
│  ├─ str
│  └─ range
├─ Set (集合)
├─ Mapping (映射)
└─ Iterator (迭代器)
   ├─ Generator (生成器)
   │  ├─ 生成器函数 (def ... yield)
   │  └─ 推导式 (x for x in ...)
   ├─ enumerate
   ├─ zip
   ├─ map
   ├─ filter
   └─ reversed
```

序列和迭代器都是可迭代对象，迭代器是一次性的，序列是有序的

迭代器每取一个值生成一个值，不会一次性生成完，所以在部分情况下能节约性能

## 常用类

```python
r = range(20, 50, 6)

for i in r:
    print(i, end=" ")  # 20 26 32 38 44

print()

for i in r:
    print(-i, end=" ")  # -20 -26 -32 -38 -44

print()

for i in range(9, -2, -3):
    print(i, end=" ")  # 9 6 3 0
```

`range` 是一个非常常用的序列类，左闭右开的区间，配上步长，可以用它生成任意的等差整数序列

```python
for i, v in enumerate(range(4, 9)):
    print(i, v, end=" | ")  # 0 4 | 1 5 | 2 6 | 3 7 | 4 8 |

print()

for i, v in enumerate(range(3), 6):
    print(i, v, end=" | ")  # 6 0 | 7 1 | 8 2 |
```

使用 `enumerate` 即可同时获取索引和值，第二个形参指定索引的起始值

# 语法糖

## 成员运算符

```python
a = [1, 3, 7, 1]
print(3 in a, 2 in a, 2 not in a)  # True False True

b = (v for v in a)
print(1 in b, 1 in b, 1 in b)  # True True False
```

使用 `in` `not in` 判断可迭代对象中存不存在指定值

*很多人在循环语句里记得迭代器是一次性的，到了 `in` 这里就忘了，然后就会出现示例里对迭代器 `b` 用 `in` 的情况*

## 推导式

平时项目里迭代器类很少见，但推导式很常见

`元素 for 元素 in 可迭代对象 if 条件` 是推导式的基本语法，它会生成一个迭代器

```python
a = [1, 3, 7, 9]

print(
    type(v for v in a),  # <class 'generator'>
    type([v for v in a]),  # <class 'list'>
    type({v for v in a}),  # <class 'set'>
    type({i: v for i, v in enumerate(a)}),  #  <class 'dict'>
    {f"-{i}-": v * 2 for i, v in enumerate(a) if v > 3},  # {'-2-': 14, '-3-': 18}
    [v2 for v1 in a if v1 > 4 for v2 in range(v1) if v2 > 6],  # [7, 8]
)
```

推导式外面套个容器语法返回的就是对应容器而不是迭代器

`if` 是可选的，`for` 是可叠加的
