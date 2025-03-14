# Python Concurrency: Threading vs. Processing

## Project Overview
This project demonstrates and compares the performance differences between Python's threading and multiprocessing approaches for concurrent programming. It provides practical examples of both methods applied to a simple summation task, along with performance measurements to highlight when each approach might be beneficial.

## Features
- **Multithreading Implementation**: Uses Python's `threading` module to compute sums across multiple threads
- **Multiprocessing Implementation**: Uses Python's `multiprocessing` module to compute sums across multiple processes
- **Performance Measurement**: Calculates execution time for both approaches vs. single-threaded execution
- **Resource Monitoring**: Tracks CPU and memory usage during execution

## Performance Comparison
Both implementations compute the sum of integers from 1 to 1,000,000 and compare:
- Execution time for single-threaded approach
- Execution time for multithreaded/multiprocessing approach (using 4 workers)
- CPU and memory utilization

## Key Differences

### Multithreading (`Multi-Threading.py`)
- Shares memory space between threads
- Uses a lock (`sum_lock`) to prevent race conditions when updating the shared total
- Typically better for I/O-bound tasks
- Limited by Python's Global Interpreter Lock (GIL) for CPU-bound tasks

### Multiprocessing (`Multi-Processing.py`)
- Creates separate processes with independent memory spaces
- Uses shared memory array to collect results from each process
- Better for CPU-bound tasks as it bypasses the GIL
- Higher memory overhead due to process creation

## Requirements
- Python 3.6+
- psutil library (`pip install psutil`)

## Usage
To run the multithreading example:
```bash
python Multi-Threading.py
```

To run the multiprocessing example:
```bash
python Multi-Processing.py
```

## Expected Output
The programs will display:
- The result of the summation
- Time taken for single-threaded execution
- Time taken for multi-threaded/multi-processing execution
- CPU and memory usage statistics

## Understanding the Results
- **For CPU-bound tasks** (like our summation example), multiprocessing typically outperforms multithreading due to the GIL.
- **For I/O-bound tasks** (like network operations or file reading), multithreading may be more efficient due to lower overhead.
- The performance difference will vary depending on:
  - Number of CPU cores available
  - Task complexity and nature (CPU vs I/O bound)
  - Size of the data being processed

## Learning Objectives
This project helps to understand:
1. Concurrent programming concepts in Python
2. Differences between threading and multiprocessing
3. Performance implications of the Global Interpreter Lock (GIL)
4. When to choose threading vs. multiprocessing
5. Basic performance measurement techniques
