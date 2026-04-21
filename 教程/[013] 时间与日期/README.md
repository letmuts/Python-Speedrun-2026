# [time](https://docs.python.org/zh-cn/3.14/library/time.html)

```python
import time

n = 2
time.sleep(n)  # 暂停线程 n 秒

print(time.time_ns())  # 系统时间，单位 ns

print(time.localtime())  # 系统时间的 time.struct_time 对象

print(time.strptime("30 Nov 00", "%d %b %y"))  # 字符串解析为 time.struct_time 对象
```

阻塞线程、获取系统时间、格式化与解析时间字符串

日期相关功能用更现代化的 `datetime` 模块平替

# [datetime](https://docs.python.org/zh-cn/3.14/library/datetime.html)

```python
import datetime

now = datetime.datetime.now()

print(type(now), now)  # <class 'datetime.datetime'>

delta = now - datetime.datetime.strptime("2000-12-1", "%Y-%M-%d")
print(type(delta), delta)  # <class 'datetime.timedelta'>

print(now.astimezone())  # 带时区的日期
```

日期类是 `datetime.datetime`，差值类是 `datetime.timedelta`，重载了运算符用于计算
