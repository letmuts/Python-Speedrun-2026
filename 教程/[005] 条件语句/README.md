# 用途

前文提到了 bool 类型，新手一定想根据判断条件执行相应代码，这个需求也是所有语言必有的

```python
a: bool = True
if a:
    print("执行块1")
else:
    print("执行块2")
```

像这样，根据 `a` 的值，执行指定的块，是条件分支最基本的需求

# if 语句

```python
a = 1
if a == 3:
    print("执行块1")
elif a == 2:
    print("执行块2")
elif a == 1:
    print("执行块3")
else:
    print("执行块4")
```

当 `if` 右边的值为 `True` 时，执行当前块内的代码，忽略其他分支块内的代码

如果不成立，跳到下一个 `elif` 判断，直到 `else` 语句

*自行调整 `a` 的值，查看打印结果，即可立即理解*

```python
if []:  # 相当于 bool([])
    print("执行块1")
else:
    print("执行块2")
```

如果条件值不是 bool 类型，其结果相当于调用了 `bool()` 类名构建 bool 对象

# 条件运算符

## 三元运算符

```cpp
// C++
int a = 1, b = 2;
std::println(a > b ? "分支1" : "分支2"); // 分支2
```

很多语言都有三元运算符，Python 的三元运算符长得稍微有点不同

```python
a, b = 1, 2
print("分支1" if a > b else "分支2")  # 分支2
```

条件放在中间，值放在两边

```python
a, b, c = 1, 2, 3
print("分支1" if a > b else "分支2" if b > c else "分支3")  # 分支3
```

支持这样一直叠叠乐，因为本质上整个右边都是第 2 个分支

```python
"分支1" if a > b else "分支2" if b > c else "分支3"
"分支1" if a > b else ("分支2" if b > c else "分支3")
```

所以这样加不加括号是一模一样的

## 布尔运算符

```cpp
// C++
auto a = 0 || 2;
std::println(typeid(a).name()); // bool
```

在很多语言中，布尔运算符的结果是 bool 类型，但 Python 不一样

```python
a = 0 or 2
print(a)  # 2

b = a
print(
    id(a), id(b), id(0), id(2)
)  # 140707623883928 140707623883928 140707623883864 140707623883928
print(a is 0, a is 2, a is b, a is not b)  # False True True False

print(a in [1, 2, 3])  # True
print(a not in [5, 6, 7])  # True

print(not a)  # False
print(not not a)  # True

print(None and True)  # None
print(True and 1 and 3)  # 3

print(False or [] or 4)  # 4

# 组合使用
print(1 and not 0 or 2)  # True
print(1 and not (0 or 2))  # False
```

*不要用 `is` 比较值，示例中用来比较 int 对象仅供展示比较 ID 的原理*

Python 的 `and` 和 `or` 的结果不会转为 bool 类型，但在比较时相当于给每个值加了个 `bool()`，比较的是转为 bool 类型后的值

* `is` / `is not` 判断两个对象的 ID 是否一致，通常用于比较 `True` `False` `None` 这三个内置变量
* `in` / `not in` 判断元素的值是否在可迭代对象中
* `not` 返回取反后的 bool 值
* `and` 返回第一个 False 值，都为 True 则返回最后一个值
* `or` 返回第一个 True 值，都为 False 则返回最后一个值

就像四则运算符一样，布尔运算符也有优先级 `is` > `in` > `not` > `and` > `or`，当然也可以用括号 `()` 使括号内优先级最高

# match 语句

如果分支太多，或者一些其他需求，if 语句会很麻烦

```python
i: int = 0
a: list[str] = [
    "a",
    "b",
    "q",
    "666",
    "677",
]

match a[i]:
    case "b":
        print("块1")
    case "q":
        print("块2")
    case str() as s if s.startswith("6"):
        print("块3: 字符串头部有 6")
    case _:
        print("最后一块")
```

*`startswith` 是 `str` 对象的方法*

调整索引 `i`，看看打印结果，立即就能理解

`case 类() as 对象 if 条件` 是固定语法，表示当类型匹配且条件成立则执行当前块

`_` 是通用匹配，匹配一切

```python
match "abc":
    case str() as s if s.startswith("a"):
        print("块1")  # 执行
    case str() as s if s.startswith("ab"):
        print("块2")
```

`match` 自上而下挨个判断条件，跟 `if` 的执行顺序一样，所以即使后面的分支也匹配，也不会执行到后面

```python
match (1, 2, 3):
    case (1, 3, 3):
        print("块1")
    case (1, _, 3):
        print("块2")  # 执行
    case _:
        print("块3")

match {"a": 123, "b": 567}:
    case {"a": 123, "b": 123}:
        print("块1")
    case {"a": 123, "b": _}:
        print("块2")  # 执行
    case _:
        print("块3")
```

通用匹配符号可以放在条件对象的属性上
