# 生成字面量

字面量文档: <https://docs.python.org/zh-cn/3.14/reference/lexical_analysis.html#literals>

创建的字面量都是常量，无法更改，赋值给变量只是让变量指向这个常量字符串

```python
a: str = "abc"
b: str = "\"qwe\""  # 不简洁
c: str = '"qwe"'  # 简洁
d: str = """a'b"c"""
```

Python 里双引号和单引号都可以用来括字符串，当字符串中有一种引号时，换用另一种引号括它，就不需要转义了

三连引号基本不用于创建字符串

转义规则文档: <https://docs.python.org/zh-cn/3.14/reference/lexical_analysis.html#escape-sequences>

```python
# 一些专有转义
print("|||\\|||'\"|||\b|||\n|||")

# 8 进制
print("\110\145\154\154\157")  # Hello

# 16 进制
print("\x48\x65\x6c\x6c\x6f")  # Hello

# 命名字符
print("\N{SNAKE}")  # 🐍


# Unicode 转义
# 4bit
print("\u4e2d\u6587")  # 中文
# 8bit
print("\U0001f600\U0001f44d")  # 😀👍
# 16bit 组合字符（字体层面的东西，需要字体支持才能正常显示）
print("\U0001f44d\U0001f3ff")  # 👍🏿
print("\U0001f44d\U0001f3ff" == "👍🏿")  # True

# 多行
s1 = "1\n2\n3"  # 最原始的换行符
print(
    s1
    == """1
2
3"""
)  # """xxx""" 可以直接换行，但很难看，不要用
print(
    s1
    == (
        "1\n"  # 字符串字面量间不加符号默认就是拼接
        "2\n"
        "3"
    )
)
```

# 拼接字符串

```python
a: str = "aaa" + "bbb"
b: str = f"{'aaa'}{'bbb'}"
print(a, a == b)  # aaabbb True
print("c1" * 4)  # c1c1c1c1
```

`str` 类重载了加法运算符用于拼接，重载了乘法运算符用于重复指定次数

```python
a = 13
b = [1, 2, 3]
c = {5, 6}
print(f"{a} - {b} - {c}")  # 13 - [1, 2, 3] - {5, 6}
```

`f-str` 语法糖可以接收任何实现了 `__str__` 的对象

```python
print("!?".join(str(v) for v in [1, 2, 3]))  # 1!?2!?3
```

把可迭代对象拼接为字符串，一个 `str.join` 方法就能搞定

# 格式化

格式化语法文档: <https://docs.python.org/zh-cn/3.14/library/string.html#format-string-syntax>

其实 `f-str` 是 `str.format` 的语法糖

```python
a, b = 111, "abc"
print("1: {} - 2: {}".format(a, b * 2))  # 1: 111 - 2: abcabc
print("1: {qwe} - 2: {_2}".format(qwe=a, _2=a))  # 1: 123 - 2: 123
```

`format` 支持按位置传参和按键名传参

```python
print("{:>06}".format("123"))  # 000123
print(f"{'\'"a\n'!r}")  # '\'"a\n'
print(f"{f'{123987.12345:,%}':<022}")  # 12,398,712.345000%0000
```

`{}` 中有大量用于格式化字符串的语法糖，详见官方文档

`{!r}` 是调用 [`repr` 内置函数](https://docs.python.org/zh-cn/3.14/library/functions.html#repr)，这个函数能还原对象构造时的代码，对应特殊方法 `__repr__`
