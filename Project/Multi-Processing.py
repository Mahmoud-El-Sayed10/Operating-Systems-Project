import multiprocessing
import time
import psutil
import os

def partial_sum(arr, start, end, result_array, index):

    partial_result = sum(arr[start:end])
    result_array[index] = partial_result

def multi_processing_sum(array, num_processes):

    result_array = multiprocessing.Array('d', num_processes)
    chunk_size = len(array) // num_processes
    processes = []

    for i in range(num_processes):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size if i != num_processes - 1 else len(array)
        process = multiprocessing.Process(
            target=partial_sum,
            args=(array, start_index, end_index, result_array, i)
        )
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_sum = sum(result_array)
    return total_sum

def single_threaded_sum(array):

    return sum(array)

def measure_performance():

    array = list(range(1, 1000001))
    num_processes = 4

    start_time = time.time()
    single_result = single_threaded_sum(array)
    single_time = time.time() - start_time

    start_time = time.time()
    multi_result = multi_processing_sum(array, num_processes)
    multi_time = time.time() - start_time

    process = psutil.Process(os.getpid())
    cpu_usage = process.cpu_percent(interval=1)
    memory_usage = process.memory_info().rss / (1024 * 1024)

    print("Performance Analysis:")
    print(f"Single-threaded result: {single_result}, Time: {single_time:.6f} seconds")
    print(f"Multi-processing result: {multi_result}, Time: {multi_time:.6f} seconds")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage:.2f} MB")

if __name__ == "__main__":
    measure_performance()
