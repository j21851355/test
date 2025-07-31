def timing_decorator(func):
    import time
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute")
        return result
    
    return wrapper

@timing_decorator
def slow_function():
    import time
    time.sleep(2)
    return "Function completed"

# Test the decorated function
print(slow_function())
