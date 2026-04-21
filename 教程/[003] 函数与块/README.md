# 定义

编程中的函数跟数学中的函数没有太大区别

在数学中，函数的作用是输入值 a、输出值 b，每次输出 a 都一定输出 b，是一个 a -> b 的映射关系

在编程中亦是如此，我们可以创建一套映射关系

```python
def 求和函数(a: int, b: int) -> int:
    return a + b


c = 求和函数(1, 3)
print(c)  # 打印求和后的值 4
d = 求和函数(c, 5)
print(d)  #  9
print(求和函数(d, c))  #  13
```

使用 `def` [**关键字**](https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#keywords)创建函数，如示例中的语法，可以标注输入输出值的类型，使用 `return` 关键字返回类型

我们称输入为 `形式参数` ，简称**形参**；  
称输出这个动作为 `返回`，return 的中文就是返回；  
称返回的值为 `返回值`。

所以 `print` 也是个函数，它是一个 Python [**内置函数**](https://docs.python.org/zh-cn/3/library/functions.html)

# 用途

如果函数仅仅只有这点用途，那肯定没有意义

## 基础用途

```python
a: int = 123


def fun_01(a: int, b: int) -> int:
    print(a, b)  # 打印 2 3
    c = a * b
    a = c + b
    return c + a


c = fun_01(2, 3)
print(a, c)  # 打印 123 15
```

1. 函数内可以进行任意复杂操作，最后返回指定的值即可
2. 函数内的变量是独立于外部的，例如函数内的 `print` 打印的是形参 `a` 的值，而不是外部 `a` 的值，外部 `a` 的值也没有因为内部的 `a` 重赋值而变化

## 改变外部

但这并不代表函数无法改变外部

```python
a: int = 123


def 示例_1():
    def fun() -> None:
        global a
        a = 456

    c = fun()
    print("示例_1", a, c)  # 示例_1 456 None


def 示例_2():
    a: int = 123

    def fun() -> None:
        nonlocal a
        a = 789

    fun()
    print("示例_2", a)  # 示例_2 789


print("初始", a)  # 初始 123
示例_1()
print("示例_1 之后", a)  # 示例_1 之后 456
示例_2()
print("示例_2 之后", a)  # 示例_2 之后 456
```

这个示例中，使用 `global` 关键字修改最顶级（全局）的 `a`，使用 `nonlocal` 关键字修改与函数同级（同作用域、同块）的 `a`

**不推荐**在函数中修改外部状态，尽量遵守函数式编程（FP）思想，仅在需要特殊需要时才在函数内使用或修改函数外的信息，一般新手的小项目中完全不需要让函数使用或修改函数外的信息

# 块

在 Python 中，使用缩进表示块范围，相同缩进的行处于同一个块

```python
def 函数1():
    # 函数1 的块
    pass
```

Python 的块内不能什么都不写，如果想什么都不做，写个关键字 `pass` 即可

块的特点就是不影响外部，所以前文中函数内的变量重赋值不会影响外部的变量

```cpp
// C++
int a = 1;
std::println(a); // 1
{
    int a = 2;
    std::println(a); // 2
}
std::println(a); // 1
```

不像其他语言中可以使用 `{}` 随地创建块，Python 的块不能随便创建
