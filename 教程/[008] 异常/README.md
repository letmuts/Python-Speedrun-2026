# 异常类与基本语法

## try - except

```python
a = 2 / 0  # ZeroDivisionError: division by zero
```

Python 很多内置操作都会抛出异常

```python
try:
    a = 3 / 0
except ZeroDivisionError as e:
    print(e)  # division by zero

try:
    b = 4 / 0
except ArithmeticError as e:
    print(type(e))  # <class 'ZeroDivisionError'>
    print(e)  # division by zero

try:
    c = 5 / 0
except Exception as e:
    print(type(e))  # <class 'ZeroDivisionError'>
    print(e)  # division by zero

try:
    d = "1" + 2  # Pylance 报错
except Exception as e:
    print(type(e))  # <class 'TypeError'>
    print(e)  # can only concatenate str (not "int") to str
```

使用 `try` 关键字捕获异常，`except` 捕获指定类型的异常，并将异常赋值给 `as` 后的变量，在下面的块中操作异常对象

由于继承关系 `Exception -> ArithmeticError -> ZeroDivisionError`，且 `except` 会根据父类捕获子类，所以指定父异常类亦可捕获

*按住 Ctrl 左键点击异常类，即可看到它的定义*

```python
class E1(ValueError):  # ValueError 继承自 Exception
    pass


class E2(E1):
    def __init__(self, msg: str, nums: tuple[int, int]) -> None:
        super().__init__(f"{msg}。算式是 {nums[0]} / {nums[1]}")


def f(a: int | str, b: int | str) -> float | str:
    """拼接字符串或计算int的商"""
    if isinstance(a, str) and isinstance(b, str):
        return a + b
    if isinstance(a, str):
        raise  # RuntimeError: No active exception to reraise
    if isinstance(b, str):
        e = E1("a 是 int 但 b 是 str")
        print(e.args)  # ('a 是 int 但 b 是 str',)
        raise e  # E1: a 是 int 但 b 是 str

    if b == 0:
        raise E2("除数不能为 0", (a, b))  # E2: 除数不能为 0。算式是 1 / 0
    return a / b


try:
    f(1, 0)
except E1 as err:
    print(err)  # 除数不能为 0。算式是 1 / 0
    raise  # E2: 除数不能为 0。算式是 1 / 0

# 假设不确定入参的类型
try:
    a, b = input("a="), input("b=")
    if a.isdigit():
        a = int(a)
    if b.isdigit():
        b = int(b)
    f(a, b)
except E2 as e:
    # 单独处理 E2
    print(e)
except E1 as e:
    # 处理其他 E1 的子类或自身
    print(e)
except Exception as e:
    # 处理其他未知异常并抛出
    print(e)
    raise
except KeyboardInterrupt:
    # 处理 Ctrl+C 手动中断程序
    print("手动中断程序")
except BaseException:
    # 最低层的异常基类
    print("看来你触发了几乎不可能触发的异常")
    raise
```

定义自己的异常类，自己处理继承关系，自己定义消息处理逻辑

使用 `raise` 关键字抛出异常

* 如果没有指定异常对象，则抛出 `RuntimeError`
* 如果在 `except` 块中不指定异常对象，则抛出 `except` 捕获的异常

## finally

```python
class A:
    def __init__(self) -> None:
        self.data = 111

    def 清理资源(self) -> None:
        print("触发清理")
        del self.data


a = A()

try:
    b = a.data / 0
except Exception as e:
    print(e)
    raise
finally:
    a.清理资源()
```

假设无论异常有没有触发，都需要清理资源（例如资源对象是文件操作对象，则需要手动关闭文件），在 `finally` 关键字的块中写清理代码，这个块无论 `try` 中有没有异常都会执行

## else

```python
try:
    a = 1 / 0
except Exception:
    print("有异常")
else:
    print("无异常")
```

如果 `try` 中无异常，则会执行 `else` 块中的代码

# 断言

```python
assert False  # AssertionError:
```

使用 `assert` 关键字断言，入参为 `True` 则无事发生，否则抛出 `AssertionError` 异常

```python
a = input("a=")
if a.isdigit():
    a = int(a)

# 一般的类型检查
if isinstance(a, int):
    print("a 是 int")
else:
    print("a 是 str")

# 断言: 输入的一定是 int
assert isinstance(a, int), "输入的不是 int"  # AssertionError: 输入的不是 int
print("a 是 int")
```

第二个形参可以指定异常的消息

断言通常用于改变静态检查，但又希望如果真的不匹配则抛出异常
