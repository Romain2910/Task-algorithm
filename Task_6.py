import random
import string
import time

def create_product():
    return {
        "name": ''.join(random.choices(string.ascii_uppercase, k=5)),
        "price": round(random.uniform(5, 500), 2),
        "rating": round(random.uniform(1, 5), 1),
        "popularity": random.randint(1, 10000)
    }

def create_product_list(count):
    return [create_product() for _ in range(count)]

def merge_sort(items, key):
    if len(items) <= 1:
        return items
    middle = len(items) // 2
    left_half = merge_sort(items[:middle], key)
    right_half = merge_sort(items[middle:], key)
    return merge(left_half, right_half, key)

def merge(left_list, right_list, key):
    merged = []
    i = j = 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i][key] <= right_list[j][key]:
            merged.append(left_list[i])
            i += 1
        else:
            merged.append(right_list[j])
            j += 1
    merged.extend(left_list[i:])
    merged.extend(right_list[j:])
    return merged

def quick_sort(items, key):
    if len(items) <= 1:
        return items
    pivot_item = items[0]
    lower_items = [item for item in items[1:] if item[key] <= pivot_item[key]]
    higher_items = [item for item in items[1:] if item[key] > pivot_item[key]]
    return quick_sort(lower_items, key) + [pivot_item] + quick_sort(higher_items, key)

def run_sorting_interface():
    print("Welcome to the product sorting system!")

    while True:
        try:
            product_count = int(input("How many products would you like to generate? (e.g., 10 or 10000): "))
            if product_count <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a positive integer.")

    product_list = create_product_list(product_count)

    sorting_algorithms = {
        "1": ("MergeSort", merge_sort),
        "2": ("QuickSort", quick_sort)
    }

    print("\nChoose the sorting algorithm:")
    print("1 - MergeSort")
    print("2 - QuickSort")
    while True:
        algorithm_choice = input("Your choice (1 or 2): ")
        if algorithm_choice in sorting_algorithms:
            algorithm_name, sort_function = sorting_algorithms[algorithm_choice]
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    sorting_keys = ["price", "rating", "popularity", "name"]
    print("\nChoose the attribute to sort by:")
    for idx, attr in enumerate(sorting_keys, 1):
        print(f"{idx} - {attr}")
    while True:
        key_input = input("Your choice (1-4): ")
        if key_input in ["1", "2", "3", "4"]:
            sorting_key = sorting_keys[int(key_input) - 1]
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    print(f"\nSorting {product_count} products by '{sorting_key}' using {algorithm_name}...")
    start_time = time.time()
    sorted_list = sort_function(product_list.copy(), sorting_key)
    elapsed = time.time() - start_time
    print(f"Sorting completed in {elapsed:.5f} seconds.\n")

    print("Top 10 sorted products:")
    for idx, product in enumerate(sorted_list[:10], 1):
        print(f"{idx}. {product}")

if __name__ == "__main__":
    run_sorting_interface()
