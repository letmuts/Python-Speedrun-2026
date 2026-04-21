# 何为 Python

Python 代码就是**纯文本**，运行代码就是用 Python 解释器读取纯文本代码后按代码内容执行

所以新手需要

1. 下载 Python 解释器
2. 运行 Python 解释器

# 安装 Python

安装环境是新手最大的门槛，跨过它，前路畅行无阻

*若下文网站打不开，需要使用代理（挂梯子）*

1. 进入 Python 官网 <https://www.python.org/>
2. 找到下载的英文 `Downloads`，点进去 <https://www.python.org/downloads/>
3. 映入眼帘的是一个 Python 版本图，红色的是已弃用版本，绿色的是不稳定新版，黄色的是稳定版  
   写此教程时（2026.3.21），3.12 是最新的黄色稳定版，3.14 是最新的绿色。  
   我们下载最新的可用版 3.14（一般认为 Python 版本 a.b.c 的 c ≥ 2 即为相对稳定可用）。  
   Python 版本图下方列举了各个版本的 `Download` 按钮，点击 3.14 的 `Download` 按钮。  
   进入 3.14 下载页面后，根据你的平台下载
   * [Windows installer (64-bit)](https://www.python.org/ftp/python/3.14.3/python-3.14.3-amd64.exe)
   * [macOS installer](https://www.python.org/ftp/python/3.14.3/python-3.14.3-macos11.pkg)
4. 假设你是 Windows 用户，下载得到安装程序，双击运行程序，弹出安装界面，在安装前勾选 `将 python.exe 添加到 PATH` （英文是 `Add python.exe to PATH`），然后安装即可
5. 安装结束（显示 `Setup was successful`）后，`win + R` 输入 `cmd` 打开终端，输入 `python --version` 看到 Python 版本，输入 `py -0` 查看已安装的 Python 版本

*Python 在 Windows 端有安装管理器 `Python install manager`，这里不用这个管理器举例是因为这个管理器对新手来说更难用*

# 运行 Python

## REPL

在终端输入 `python` 以运行 Python

这是一个可直接输入并运行 Python 代码的输入输出系统 （REPL Read-Eval-Print Loop）

例如输入 `1 + 2` 回车，它会输出 `3`

## 执行 py 文件

随便找一个文件夹，在文件夹内新建文本文件，然后修改整个文件名前后缀，例如改为 `1.py`

用记事本打开它，写入 `print(12345)`

在文件资源管理器的路径栏里输入 `cmd` 回车，就可以在当前目录打开终端

终端中输入 `python 1.py` 即可用 Python 解释器执行这个 `1.py` 文件

执行后，终端内输出 `12345`

# 安装 Visual Studio Code

用记事本写代码效率太低，我们使用 VSCode 写代码

## 安装与配置

在官网 <https://code.visualstudio.com/> 下载并安装即可

使用 VSCode 打开 Python，会自动安装 Python 插件（扩展），如果没有自动安装，按 `Ctrl + Shift + X` 打开扩展侧栏，搜索并安装以下插件

* [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)  
  用于类型静态检测
* [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)  
  用于以 Debug 模式执行 Python
* [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)  
  用于格式规范静态检测与代码格式化

## 尝试编辑

用 VSCode 打开刚才的 `1.py` 文件，删光文字，然后将 `print([1, (2, 3),])` 复制到编辑器内，按 `Ctrl + Alt + F`，代码会格式化为

```python
print(
    [
        1,
        (2, 3),
    ]
)
```

这就是 Ruff 插件的格式化的功能，以后的代码我们都使用 Ruff 格式化，统一代码风格

## Debug 运行

按 `F5` 运行，会弹出使用什么运行的提示，第一个就是 Python Debugger，点击或直接回车选用，等待它启动后运行成功输出 `[1, (2, 3)]`

Debug 运行和直接 `python 1.py` 运行有什么区别？

鼠标指针放在行号上，左侧会冒出红点，点一下，红点停留在行号的坐标，这就是个断点

假设在 `print` 所在行放上断点，Debugger 运行到这行就会暂停，按 `F11` 执行下一行并暂停，按 `F5` 继续运行直到下一个断点

# 查询文档

想知道 Python 官方是怎么解释 Python 的规则的？<https://docs.python.org/3/> 这里就是官方文档页面

你可以查询所有 Python 内置的功能的解释，例如 `print`

1. 把左上角的语言改为简体中文
2. 右上角搜索栏搜索 `print`，点进搜索结果 <https://docs.python.org/zh-cn/3.14/library/functions.html#print>
3. 可以看到 Python 官方对 `print` 的详细解释
