# 创建

前文中提到了变量的类型，我们可以自定义类型

```python
class MyType: ...


a: MyType = MyType()
```

使用 `class` 关键字就可以自定义类型，称为 `类`，使用 `类名()` 就可以创建该类型的值，称为 `对象`

类名头部大写是命名规范，方便区分头部小写的对象

按前文中的说法，`a` 应该是个变量，这里称作 `对象` 仅仅是看待角度不同

从词语本身来说

* `变量` 强调它用于存储 `量` 也就是值，且它的指向会变化。
* `对象` 强调它是一个“个体”，在面向对象（OOP）思想中，我们把具体的值看作一个个体，而这个个体内部的值是个体自身的属性。  
  像前文中说的运算，在 OOP 思想中就是对象个体之间的交互。

这些说法仅仅只是编程思想的抽象化表达，并非一定有什么本质区别

**Python 中所有的变量都是对象**

从 OOP 的角度说:

* `class MyType` 及其内部内容是对类 `MyType` 的定义
* 示例里的 `a` 变量是个类型为 `MyType` 的对象，简称 “`a` 是个 `MyType` 对象”
* 对 `a` 的赋值过程就是让变量 `a` 指向一个 `MyType` 的对象实例

# 容器

Python 内置了一些类型，用于存储数值，容器类型属于官方文档中序列类型: <https://docs.python.org/zh-cn/3.14/library/stdtypes.html#sequence-types-list-tuple-range>

| 容器类 | 简述                                            |
| :----- | :---------------------------------------------- |
| list   | 列表 - 有序存值                                 |
| tuple  | 元组 - 不可变列表                               |
| set    | 集合 - 无序且元素不重复                         |
| dict   | 字典 - 每个唯一的键（key）映射到一个值（value） |

```python
a: list = list()  # 列表
b: tuple = tuple()  # 元组
c: set = set()  # 集合
d: dict = dict()  # 字典
print(a, b, c, d)  # [] () set() {}

# 专门的语法
a = []
b = ()
# c = {/}  # 长得像空集符号 ∅，3.15 才有的语法
d = {}
```

可以直接从类名创建空容器，也可以用 list tuple dict 的专用语法创建容器

```python
# 存值

a1: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a2: list = [1]

b1: tuple = (1, 2, 3, 4, 5)
b2: tuple = (1,)  # 不加逗号是括号运算符

c1: set = {1, 2, 3, 4, 5}
c2: set = {1}

d: dict = {"a": 3, "qwe": 2, 123: "zzz"}


# 取值

# 取单个元素
print(a1[0], b1[-1], d["a"], d[123])  # 1 5 3 zzz

# 指定范围生成新容器对象
a3: list = a1[1:2]
b3: tuple = b1[1:]
print(a3, b3)  # [2] (2, 3, 4, 5)
print(a1[:-1])  # [1, 2, 3, 4, 5, 6, 7, 8]
print(a1[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(a1[-2:1:-2])  # [8, 6, 4]
```

`[index]` 是索引操作，`[a:b:c]` 是切片操作

索引从 `0` 开始，支持负索引，例如 `-1` 就是倒数第一个

注意切片是左闭右开，第三个值是步长，默认步长为 `1`

# 内置对象

Python 中内置了一些常量，详见文档 <https://docs.python.org/zh-cn/3/library/constants.html>

就像前篇中用到的 `None` 就是一个内置的常量对象

使用比较运算符可以生成 bool 对象，bool 类型只有两个对象 `True` `False`

```python
# 不显式 return 和 return None 的返回值都是 None
def 函数1() -> None:
    pass


print(函数1())  # None

a: bool = bool()
print(a)  # False

a = 2 > 1
print(a)  # True

# == 是用于判断是否相等的运算符
a = 3 == 3
print(a)  # True

# 不等于运算符是 !=
print(1 != 2)  # True
print(4 > 4, 4 >= 4)  # False True

# 可以从其他类型的值生成 bool 值，0、None、空容器都是 False
print(bool(0), bool(None))  # False False
print(bool([]), bool(()), bool(set()), bool({}))  # False False False False
```

# 属性

从编程的角度说，绑定在对象上的变量，称为对象的属性

从 OOP 的角度说，对象的属性就是它自身的属性，就像任何一个个体都有不一样的属性，调整对象的内部变量即可达到调整个体属性的作用

```python
class A:
    pass


a = A()
a.变量1 = 123
a.变量2 = 456
print(a.变量1, a.变量2)  # 123 456
```

使用成员运算符 `.` 即可访问对象的属性

*如果你复制这段代码到 VSCode，会发现 Pylance 报错一片红，因为这是不规范写法*

```python
class B:
    q = "aaa"
    w = 123
    e = [(), ()]


print(type(B))  # <class 'type'>
print(B.q, B.w, B.e)  # aaa 123 [(), ()]
```

类本身也是个对象，类 `B` 其实是个类型为 `type` 的变量

# 方法

方法仅仅只是 OOP 语境中绑定在对象上的函数

## 对象的方法

### 普通方法

绑定在对象上的函数，称为对象的方法

对象的方法的作用之一就是操作对象的属性，所以方法肯定得先知道当前的对象是哪个变量

```python
class A:
    def f(self, b):
        return self.a + b


a = A()
a.a = 3
print(a.f(4))  # 7
```

在定义函数时，第一个形参填 `self`，这个 `self` 对象就是调用方法的对象自身

### 特殊方法

<https://docs.python.org/zh-cn/3/reference/datamodel.html#special-method-names>

Python 规定了一些方法名，使用这些名称的方法有特殊作用

```python
class A:
    def __init__(self, a):
        self.a = a
        self.b = 4

    def f(self, c):
        return self.a * self.b + c


a = A(3)
print(a.f(5))  # 17
```

例如 `__init__` 可以定义使用类名创建对象时 `()` 里的传参

*这个示例 Pylance 不报错了，因为这是规范写法*

可以使用特殊方法定制很多解释器级的语法

```python
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other) -> "A":
        return A(self.a + other.a, self.b + other.b)

    def __str__(self) -> str:
        return f"{self.a}---{self.b}"


a, b = A(1, 2), A(3, 4)
c = a + b
print(str(c))  # 4---6
```

这个示例中:

* `__add__` 重新定义了加法运算符的功能（重载了加法运算符）
* `__str__` 重新定义了字符串化时返回的字符串

## 类的方法

绑定在类上的函数，称为类的方法

类的方法的作用之一就是操作类的属性，所以方法肯定得先知道当前的对象是哪个类

```python
class A:
    a = 123

    @classmethod
    def f(cls):
        print(cls.a)


A.f()  # 123
A.a = 456
A.f()  # 456
```

使用 `@classmethod` 修饰的方法就是类方法（`classmethod` 的中文就是 `类方法`），第一个形参 `cls` 就是类对象自身

# 继承

```python
class A:
    def m(self): ...


class B(A):
    pass


class C:
    def m(self): ...


def f(a: A): ...


a = A()
b = B()
c = C()

f(a)
f(b)
f(c)  # Pylance 报错
```

`B(A)` 这样在创建类时括号里填其他类，就是继承

继承会让新的类拥有被继承类的方法和属性

新的类叫 `子类`，被继承的类叫 `父类`

函数 `f` 需要类型为 `A` 的对象，本质上是需要这个对象拥有 `A` 的所有方法和属性；  
那么既然 `B` 继承了 `A` 的所有方法和属性，所以类型为 `B` 的对象 `b` 也可以作为函数 `f` 的输入。

由于静态检查只检查继承关系，所以即使 `C` 也有 `m` 方法，`c` 也不能作为 `f` 的输入
