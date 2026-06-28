# 内置模块

```python
import tkinter as tk

root = tk.Tk()
root.title("窗口的标题111aaa")
root.geometry("300x200")

root.mainloop()
```

Python 内置了大量模块，通过 `import` 关键字导入模块，`as` 可以给模块起别名

该示例使用内置的 `tkinter` 模块创建了一个 GUI 窗口

# 定义模块

在我们自己的项目中，希望把各个功能放在不同的 `.py` 文件位置，则需要使用模块语法

```
根目录
├─ 文件夹1
│  ├─ __init__.py
│  ├─ __main__.py
│  ├─ name_1.py
│  └─ name_2.py
├─ 当前执行的文件.py
└─ name_3.py
```

演示代码的目录结构如上

在 VSCode 中打开 `当前执行的文件.py`，按 `F5` 执行

或者在 `根目录` 下执行 `python`: `\根目录> python .\当前执行的文件.py`

```
导入了 3
导入了 __init__
导入了 1
导入了 __main__
导入了 2
函数名: fun_3_1
函数名: fun_2_1
函数名: fun_1_1
文件夹1.__main__
```

每个 `.py` 文件都可以作为模块导入，而目录可以作为一种特殊的模块导入，称之为 `包`，在导入包时，`__init__.py` 中的代码会先导入

`from` 关键字会直接导入子代的包或对象

`.<包名>` 将从相对路径导入

使用 `python -m <模块名>` 直接执行模块的 `__main__.py`: `\根目录> python -m 文件夹1`

```
导入了 __init__
导入了 1
导入了 __main__
__main__ 的执行内容
```

`__name__` 变量存储了当前模块的模块名，如果当前模块是执行入口，则 `__name__` 的值是 `"__main__"`，所以使用 `if __name__ == "__main__"` 能防止在 `import` 当前模块时执行入口代码

很多内置模块都有 `__main__` 可以执行

* `> python -m pip --version`  
  `pip 26.0.1 from C:\Users\Administrator\AppData\Local\Programs\Python\Python314\Lib\site-packages\pip (python 3.14)`
* `> python -m http.server 8123`  
  `Serving HTTP on :: port 8123 (http://[::]:8123/) ...`
* `> python -m pydoc str`

  ```
  Help on class str in module builtins:

  class str(object)
  |  str(object='') -> str
  |  str(bytes_or_buffer[, encoding[, errors]]) -> str
  |
  |  Create a new string object from the given object. If encoding or
  |  errors is specified, then the object must expose a data buffer
  |  that will be decoded using the given encoding and error handler.
  |  Otherwise, returns the result of object.__str__() (if defined)
  |  or repr(object).
  |  encoding defaults to 'utf-8'.
  |  errors defaults to 'strict'.
  |
  -- More  --
  ```

# 包管理器

Python 官方提供了 [PyPI](https://pypi.org/) 供任何人上传发布自己的包

使用 `pip` 模块安装 PyPI 中的包，例如安装 numpy: `python -m pip install numpy`

```cmd
>where pip
C:\Users\Administrator\AppData\Local\Programs\Python\Python314\Scripts\pip.exe
```

因为 `pip` 有个 exe 在环境中，所以可以直接调用: `pip install numpy`

如果包不在 PyPI 中也可以安装，例如从 Git 仓库安装: `pip install git+<地址>`

常用命令:

* 卸载包: `pip uninstall <包名>`
* 更新包: `pip install -U <包名>`
* 查看已安装包列表: `pip list`  
  更详细: `pip list -v`
* 查询可安装版本: `pip index versions <包名>`
* 查看已安装包的信息: `pip show <包名>`

如果安装的包没有打包好的文件，会直接在本地打包整个项目

旧版 Python 的打包的配置入口是 `setup.py`，新版是 `pyproject.toml`
