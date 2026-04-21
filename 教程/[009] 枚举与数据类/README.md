# [enum](https://docs.python.org/zh-cn/3.14/library/enum.html)

在编程中，枚举类型用于无副作用地给常量起名字，并将同一个类型的常量打包到一个类中

由于 Python 中每个变量都有自己的 ID，所以只要让每个变量能正常存储值，且 ID 不同，即可达到目的

```python
from typing import Final


class Color:
    red: Final = (0, object())
    green: Final = (1, object())
    blue: Final = (2, object())


def f(a):
    assert id(a) in {id(Color.red), id(Color.green), id(Color.blue)}


f(Color.red)  # 通过
f((0, object()))  # AssertionError
```

`object` 创建的每个对象都有不同 ID，所以每个枚举的 ID 都不同

虽然这样能实现枚举，但它的功能严重不足

* 它没法静态检查，必须动态判断 ID 是不是枚举变量的 ID
* 它不能指定类型，无法像继承那样指定基类的方便写法

Python 内置的 `enum` 模块中就有纯 Python 实现的枚举基类

```python
import enum
from dataclasses import dataclass


class Color(enum.Enum):
    red = enum.auto()
    green = enum.auto()
    blue = enum.auto()


def f1(color: Color):
    pass


f1(Color.blue)
f1(1)  # Pylance 报错


@dataclass(slots=True, kw_only=True, frozen=True)
class AniVal:
    name_cn: str
    voice: str


class Ani(enum.Enum):
    dog = AniVal(name_cn="狗", voice="汪")
    cat = AniVal(name_cn="猫", voice="喵")
    chicken = AniVal(name_cn="鸡", voice="美")
    gege = chicken  # 别名


def f2(ani: Ani):
    print(ani.name, end=" | ")
    print(f"{ani.value.name_cn} 叫：{ani.value.voice}")


f2(Ani.cat)  # cat | 猫 叫：喵

# 完整的映射字典视图
print(type(Ani.__members__), Ani.__members__)  # <class 'mappingproxy'>

# 下面三个私有属性虽然实用，但没有正式文档

# 不包括别名的所有名称的 list
print(
    type(Ani._member_names_), Ani._member_names_
)  # <class 'list'> ['dog', 'cat', 'chicken']

# 完整的映射字典
print(type(Ani._member_map_), Ani._member_map_)  # <class 'dict'>

# 值映射到枚举
# - 由于别名同值，所以不包括别名
# - 由于枚举的值要作为映射的键，所以值类型必须可哈希
print(type(Ani._value2member_map_), Ani._value2member_map_)  # <class 'dict'>
```

# [dataclasses](https://docs.python.org/zh-cn/3.14/library/dataclasses.html)

上文示例代码中用到了 `dataclass`，它不需要 `__init__` 等一堆需要自己实现的繁琐的特殊方法，开关它的形参，就会自动实现对应的特殊方法

Python 3.7 才加入的 `dataclasses` 模块，在这之前的原始人只能用 `TypedDict` 凑合

```python
from dataclasses import dataclass, field


@dataclass
class D:
    a: list = field(default_factory=list)


d1 = D()
d2 = D()

d1.a.append(1)
d2.a.append(2)

print(d1.a, d2.a)  # [1] [2]
```

`field` 函数让 `dataclass` 的元素可以自定义初始化方式

由于列表之类的对象会被 `append` 之类的方法修改，所以如果默认值直接赋值对象 `[]`，相当于所有变量共用一个对象，Python 不允许 dataclass 的元素的默认值是可变的

`field` 的 `default_factory` 形参可以自定义生成默认值的函数，类名 `list` 作为可调用对象传进去即可动态生成空 list
