# 赋值与解包

在前面的文章中，使用过 `a, b = 1, 2` 这种写法

实际上这是对 `tuple` 对象的解包语法 \([PEP 3132](https://peps.python.org/pep-3132/)\)

```python
t: tuple = (1, 2, 3)

a, b, c = t
print(a, b, c)  # 1 2 3

d, *e = t
print(d, e)  # 1 [2, 3]
```

关键字 `*` 可以将后续所有的解包后的元素放到变量里，所以 `e` 是个 `list`

```python
t = range(12)

a, *b, c, d = t
print(a, b, c, d)  # 0 [1, 2, 3, 4, 5, 6, 7, 8, 9] 10 11

a, b, *c, d = set(t)
print(a, b, c, d)  # 0 1 [2, 3, 4, 5, 6, 7, 8, 9, 10] 11
```

各种可迭代对象都可以解包

```python
t1 = range(6)
print([666, *t1, 666])  # [666, 0, 1, 2, 3, 4, 5, 666]
print({666, *t1, 666})  # {0, 1, 2, 3, 4, 5, 666}


t2 = tuple(range(i * 3, i * 3 + 3) for i in range(3))
print([*t2[2], *t2[0], *t2[1]])  # [6, 7, 8, 0, 1, 2, 3, 4, 5]
```

理所当然的，创建容器的语法糖里也可以使用 `*`

字典也是可以解包的，关键字是 `**` \([PEP 448](https://peps.python.org/pep-0448/)\)

```python
t = {1: 2, 7: 6}
print({9: 4, **t})  # {9: 4, 1: 2, 7: 6}
```

# 函数传参与解包

## 解包

```python
def f(a, b, *c, d=None, **e):
    print([a, b, c, d, e])


f(1, 2, 3, 4, 5, q=6, w=7)  # [1, 2, (3, 4, 5), None, {'q': 6, 'w': 7}]
f(1, 2, d=3)  # [1, 2, (), 3, {}]
```

在函数形参里使用 `*` 和 `**` 是最常见的用法

```python
def f(
    a: int,
    b: str,
    *c: bytes,
    d: int | None = None,
    **e: tuple,
):
    print([a, b, c, d, e])


f(
    1, "2", b"3", b"4", d=5, q=(), w=(7, 8)
)  # [1, '2', (b'3', b'4'), 5, {'q': (), 'w': (7, 8)}]
```

配合类型注释才是实战中的正确用法

`*` 的类型注释是元素的类型，因为变量本身的类型一定是 `tuple`  
`**` 的类型注释是值的类型，因为键的类型一定是 `str`

## [特殊参数](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#special-parameters)

形参中使用 `*` 和 `/` 特殊参数能强制形参仅位置传参和仅键值传参

```python
def f(a, /, b, *, c):
    print([a, b, c])


f(1, b=2, c=3)  # √
# f(a=1, 2, c=3)  # ×
f(1, 2, c=3)  # √
```

`/` 前面的形参只能位置传参，`*` 后面的形参只能键值传参

实战中特殊参数非常常用，能有效防止位置传参和键值传参混用的问题
