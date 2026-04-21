# [yield](https://docs.python.org/zh-cn/3/reference/expressions.html#yield-expressions)

```python
from collections.abc import Generator
from typing import Literal


def f() -> Generator[int, str, Literal[b"end"]]:
    for i in range(4):
        接收: str = yield i
        print(f"{接收=}", end=" | ")
    return b"end"


a = f()
print(type(a))  # <class 'generator'>
print(next(a))  # 0
print(a.send("111"))  # 接收='111' | 1
print(next(a))  # 接收=None | 2
next(a)  # 接收=None |
try:
    next(a)  # 接收=None |
except StopIteration as e:
    print()
    print(e.value)  # b'end'
```

函数中使用 `yield` 关键字后，函数的返回值是 `generator` 对象  
（async 函数返回 `async_generator` 对象）

`next` 函数将调用 `generator.__next__` 特殊方法，这个方法会执行函数直到遇到 `yield`

`yield` 的返回值是 `generator.send` 发送的值  
（执行到 `yield` 会直接暂停函数，下一次执行时才会拿到 `yield` 的返回值）

用于类型注释的 `Generator` 类型的三个子类型分别是 yield输出类型、send类型、return类型

生成器结束时会抛出 `StopIteration` 异常，`StopIteration.value` 就是 `return` 的值

```python
from collections.abc import Generator


def f(r: range) -> Generator[int]:
    yield from r
    # 等价于
    for i in r:
        yield i


a = f(range(4, 7))
for i in a:
    print(i, end=" ")  # 4 5 6 4 5 6
```

`yield from` 能直接对可迭代对象使用

对生成器对象使用 `for` 语句，不会抛出结束异常，可当作普通的可迭代对象使用

# [生成器表达式](https://docs.python.org/zh-cn/3/reference/expressions.html#generator-expressions)

```python
from types import GeneratorType

a = (i for i in range(4))
print(type(a), isinstance(a, GeneratorType))  # <class 'generator'> True
```

推导式语法可以返回生成器
