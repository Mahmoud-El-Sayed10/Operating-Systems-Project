import threading
import time
import psutil
import os

total_sum = 0
sum_lock = threading.Lock()

def partial_sum(arr, start, end):

    global total_sum
    partial_result = sum(arr[start:end])
    with sum_lock:
        total_sum += partial_result

def multi_threaded_sum(array, num_threads):

    global total_sum
    total_sum = 0
    chunk_size = len(array) // num_threads
    threads = []

    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size if i != num_threads - 1 else len(array)
        thread = threading.Thread(target=partial_sum, args=(array, start_index, end_index))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return total_sum

def single_threaded_sum(array):

    return sum(array)

def measure_performance():

    array = list(range(1, 1000001))
    num_threads = 4

    start_time = time.time()
    single_result = single_threaded_sum(array)
    single_time = time.time() - start_time

    start_time = time.time()
    multi_result = multi_threaded_sum(array, num_threads)
    multi_time = time.time() - start_time

    process = psutil.Process(os.getpid())
    cpu_usage = process.cpu_percent(interval=1)
    memory_usage = process.memory_info().rss / (1024 * 1024)

    print("Performance Analysis:")
    print(f"Single-threaded result: {single_result}, Time: {single_time:.6f} seconds")
    print(f"Multi-threaded result: {multi_result}, Time: {multi_time:.6f} seconds")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage:.2f} MB")

if __name__ == "__main__":
    measure_performance()
