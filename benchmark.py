import time


def benchmark(func):
    """
    A timer decorator
    """

    def function_timer(*args, **kwargs):
        """
        A nested function for timing other functions
        """
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "Benchmark: {func} took {time}s"
        print(msg.format(func=func.__name__, time=round(runtime, 3)))
        return value

    return function_timer
