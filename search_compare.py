import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found


def binary_search_iterative(a_list,item):
    first = 0

    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found
    
    
def binary_search_recursive(a_list,item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)

def linear_search(list, target):
    max_value_index = list[0]
    for i in range(0, len(list)):
        if list[i] > max_value_index:
            max_value_index = i
    return max_value_index


if __name__ == "__main__":
    """Main entry point"""
    list_sizes = [500, 1000, 5000]

    for the_size in list_sizes:
        total_time = 0
        for i in range(100):
            mylist = get_me_random_list(the_size)
            # sorting is not needed for sequential search.
            mylist = sorted(mylist)

            start = time.time()
            check = binary_search_iterative(mylist, 99999999)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Binary Search Iterative took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

    for the_size in list_sizes:
        total_time = 0
        for i in range(100):
            mylist = get_me_random_list(the_size)
            # sorting is not needed for sequential search.
            #mylist = sorted(mylist)

            start = time.time()
            check = sequential_search(mylist, 99999999)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

    for the_size in list_sizes:
        total_time = 0
        for i in range(100):
            mylist = get_me_random_list(the_size)
            # sorting is not needed for sequential search.
            mylist = sorted(mylist)

            start = time.time()
            check = ordered_sequential_search(mylist, 99999999)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Ordered Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")   

    for the_size in list_sizes:
        total_time = 0
        for i in range(100):
            mylist = get_me_random_list(the_size)
            # sorting is not needed for sequential search.
            mylist = sorted(mylist)

            start = time.time()
            check = binary_search_recursive(mylist, 99999999)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Binary Search Recursive took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")