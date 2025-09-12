import functools
import time
from typing import Callable, Any


def timer(func: Callable) -> Callable:
    """计算函数运行时间的装饰器

    Args:
        func: 被装饰的函数

    Returns:
        包装后的函数，会在执行时计算并打印运行时间
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        # 记录开始时间
        start_time = time.perf_counter()

        # 执行被装饰的函数
        result = func(*args, **kwargs)

        # 记录结束时间
        end_time = time.perf_counter()

        # 计算并打印运行时间
        run_time = end_time - start_time
        print(f"函数 {func.__name__!r} 运行时间: {run_time:.6f} 秒")

        return result

    return wrapper
