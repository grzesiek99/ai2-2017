def cache(function):
    function._cache = {}
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in function._cache:
            return function._cache[key]
        retval = function(*args, **kwargs)
        function._cache[key] = retval
        return retval
    return wrapper


def fib(n):
    return fib(n-1) + fib(n-2) if n > 2 else 1
