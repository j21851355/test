import time
import random

def measure_performance(func, size):
    start_time = time.time()
    func([random.randint(1, 1000) for _ in range(size)])
    end_time = time.time()
    return end_time - start_time

# Compare sorting algorithms
sizes = [100, 1000, 5000]
for size in sizes:
    time_taken = measure_performance(bubble_sort, size)
    print(f"Time taken for size {size}: {time_taken:.4f} seconds")
