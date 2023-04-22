def decorator_timer(some_function):
    from time import time

    def wrapper(*args, **kwargs):
        t1 = time()
        some_function(*args, **kwargs)
        end = time()-t1
        return end
    return wrapper