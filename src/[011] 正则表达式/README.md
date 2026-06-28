# re

<https://docs.python.org/zh-cn/3/library/re.html#module-re>

Python 内置模块 `re` 提供了完整的正则表达式功能，本文不介绍正则语法（自行查看官方文档），仅介绍 `re` 模块的重点用法

## search

```python
import re

s1 = "aaa123bbb"
m1 = re.search(r"\d+", s1)
print(type(m1))  # <class 're.Match'>
print(m1)  #  <re.Match object; span=(3, 6), match='123'>
assert m1 is not None
print(m1.group())  # 123

m2 = re.search(r"a(\d*)b", s1)
print(m2)  #  <re.Match object; span=(2, 7), match='a123b'>
assert m2 is not None
print(m2.group())  # a123b
```

`re.search` 返回第一个匹配项，返回类型是 `re.Match | None`，`Match` 对象的属性中包含了匹配的字符串

`re.Match` 对象的 `group` 方法用于返回捕获的子串

## match

```python
import re

s1 = "aaa123bbb"
m1 = re.match(r"\d+", s1)
print(m1)  #  None

m2 = re.match(r"a+(\d*)b+", s1)
print(m2)  #  <re.Match object; span=(0, 9), match='aaa123bbb'>
assert m2 is not None
print(m2.group())  # aaa123bbb
print(m2.group(1))  # 123
```

`re.match` 与 `re.search` 基本一样，区别在于必须完整匹配整个字符串

## findall

```python
import re

pattern = r"^[a-z]+(\d+)[a-z]+$"
s = (
    "aaa123bbb\n"  # 1
    "qqqqwwww2222\n"
    "yyyyy1111\n"
    "ttttt55555tttt\n"  # 2
    "ppppp66666666\n"
    "FFFF77777BBBB\n"  # 3
    "oooooolllllll\n"
    "uuuuuiiiiii99999\n"
)

m1 = re.findall(pattern, s)
print(m1)  # []

m2 = re.findall(pattern, s, flags=re.MULTILINE)
print(m2)  # ['123', '55555']

m3 = re.findall(pattern, s, flags=re.M | re.I)
print(m3)  # ['123', '55555', '77777']
```

`re.findall` 配合 `re.M` 即可获取每行的匹配

每个 flag 都有对应的单字符简写，`re.MULTILINE` 仅在 `^` `$` 时生效

## sub

```python
import re

s = "aaa123bbb0c4d55e"

m1 = re.sub(r"\d+", "666", s)
print(m1)  #  aaa666bbb666c666d666e

m2 = re.subn(r"\d+", "777", s)
print(m2)  #  ('aaa777bbb777c777d777e', 4)
```

`re.sub` 正则替换，`re.subn` 会统计替换次数
