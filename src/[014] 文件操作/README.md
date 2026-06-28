# [pathlib](https://docs.python.org/zh-cn/3/library/pathlib.html)

在 Python 3.4 加入 `pathlib` 模块前，路径的解析、拼接等操作是基于字符串的，使用 `os` 模块中的路径操作函数完成

现在有了更先进的 `pathlib` 模块，路径操作大大简化了

```python
from pathlib import Path

p1 = Path(".")
print(p1)  # Path 对象
print(p1.absolute())  # 解析为绝对路径
print(p1.resolve())  # 解析为绝对路径且自动解析软链接

p2 = Path("..")
print(p1.resolve().parent == p2.resolve())  # True


print(
    Path("123/abc") / "qwe"
    == Path("123") / "abc" / "qwe"
    == Path("123") / "abc/qwe"
    == Path(R"123\abc\qwe")
    == Path("123", "abc/qwe")
    == Path("123", "abc", "qwe")
)  # True
```

能想到的方便的操作基本都有，除了字符串方面的各种解析和合并，还包括目录和文件的判空、创建、复制、移动、删除、重命名等，功能太多，需要时再查找即可

# 读写

文件的读写需要使用内置函数 `open` 打开文件 <https://docs.python.org/zh-cn/3/library/functions.html#open>

直接按二进制读写文件，或者按字符串读写，如果是字符串的话，需要指定编码

写入又分为覆盖和追加，所以 `open` 打开文件时需要指定以什么模式打开

每个模式对应的字符见文档

```python
with open(
    "示例文件.txt",
    "rt",
    encoding="utf-8",
) as f:
    for line in f.readlines():
        print(line, end="")
```

**形参 `encoding` 默认是平台的默认编码，Windows 中是 ANSI，而大部分文件都不是 ANSI，所以一定要手动指定编码**

更现代的写法是使用 `Path` 对象的方法

```python
from pathlib import Path

path = Path("示例文件.txt")

with path.open("rt", encoding="utf-8") as f:
    for line in f.readlines():
        print(line, end="")
print()

print(path.read_text(encoding="utf-8"))

for line in path.read_text(encoding="utf-8").splitlines():
    print(line)
```

# with 语句

新手第一次接触 `with` 关键字的地方就是 `open`

`open` 函数返回的对象是个文件操作对象，它会一直占用系统文件，直到手动释放或内存回收时自动释放

如果用 `try ... finally ...` 释放的话过于冗余

而 `with` 就是用来解决这个问题的

`with` 关键字后面跟的对象需要实现 `__enter__` `__exit__` 特殊方法

* `__enter__` 的返回对象会赋值给 `as` 后面跟的变量
* `__exit__` 会在 `with` 块结束后执行（包括异常和提前退出）
