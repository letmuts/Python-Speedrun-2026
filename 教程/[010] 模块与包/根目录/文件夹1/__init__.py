print("导入了 __init__")

from .name_1 import fun_1_1  # noqa: E402

__all__ = [
    "fun_1_1",
]
