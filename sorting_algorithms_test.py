import random
import time
import csv

# Sorting Algorithm Implementations

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def quick_sort(arr):
    """Refactored Quick Sort to avoid recursion depth exceeded errors"""
    if len(arr) <= 1:
        return arr

    # Use an iterative approach with a stack to simulate recursion
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Test Data Generation

def generate_random_data(size):
    return [random.randint(0, 1000) for _ in range(size)]

def generate_sorted_data(size):
    return list(range(size))

def generate_reverse_sorted_data(size):
    return list(range(size, 0, -1))

def generate_nearly_sorted_data(size, swaps=10):
    arr = list(range(size))
    for _ in range(swaps):
        i, j = random.sample(range(size), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def generate_data_with_duplicates(size, unique_elements=10):
    unique_vals = [random.randint(0, 1000) for _ in range(unique_elements)]
    return [random.choice(unique_vals) for _ in range(size)]

# Experiment Runner

def run_experiment(algorithm, data, algorithm_name, test_case_name):
    start_time = time.perf_counter()
    algorithm(data)
    end_time = time.perf_counter()
    return {
        "algorithm": algorithm_name,
        "test_case": test_case_name,
        "input_size": len(data),
        "execution_time": end_time - start_time
    }

def main():
    algorithms = {
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort,
        "Bubble Sort": bubble_sort,
        "Quick Sort": lambda arr: quick_sort(arr.copy()),  # Quick Sort returns a new array
        "Merge Sort": lambda arr: merge_sort(arr.copy()),  # Merge Sort modifies inplace
        "Heap Sort": heap_sort,
    }
    
    test_cases = {
        "Random": generate_random_data,
        "Sorted": generate_sorted_data,
        "Reverse Sorted": generate_reverse_sorted_data,
        "Nearly Sorted": generate_nearly_sorted_data,
        "With Duplicates": generate_data_with_duplicates,
    }
    
    input_sizes = [100, 1000, 5000, 10000]
    results = []

    for algo_name, algo_func in algorithms.items():
        for case_name, case_func in test_cases.items():
            for size in input_sizes:
                data = case_func(size)
                data_copy = data.copy()  # Ensure sorting does not modify the original test case
                result = run_experiment(algo_func, data_copy, algo_name, case_name)
                results.append(result)
    
    # Save results to CSV
    with open("performance_analysis.csv", "w", newline="") as csvfile:
        fieldnames = ["algorithm", "test_case", "input_size", "execution_time"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    print("Performance analysis saved to 'performance_analysis.csv'.")

if __name__ == "__main__":
    main()