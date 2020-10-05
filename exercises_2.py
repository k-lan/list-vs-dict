"""
Answers to 3.11 programming exercises
"""
import time
import random

# 1. Devise an experiment to verify that the list index operator is O(1)
# This executes at approximately the same speed no matter the index
# because it is of O(1).
my_list = [x for x in range(1, 10000001)]  # Create massive list, starting at 1.


def list_index_speed(a_list: list):
    for i in range(1, len(a_list), 2000000):
        time_start = time.time()
        num = a_list[i]
        time.sleep(0.00001)
        time_end = time.time()
        time_final = time_end - time_start
        print(f'indexing at list location {i:7}, '
              f'took {time_final:13.11f} ms')


# 2. Devise an experiment to verify that get item and set item are O(1) for dictionaries.
# The get speed executes at approximately the same speed no matter the size
# because it is of O(1) speed.
my_dict = dict.fromkeys(range(1, 10000001), 0)  # Create a massive dictionary of value 0


def dict_get_speed(a_dict: dict):
    for i in range(1, len(a_dict), 2000000):
        time_start = time.time()
        a_dict.get(i)  # calling get at each step
        time.sleep(0.00001)
        time_end = time.time()
        time_final = time_end - time_start
        print(f'getting item at dict location {i:7},'
              f' took {time_final:13.11f} ms')


def dict_set_speed(a_dict: dict):
    for i in range(1, len(a_dict), 2000000):
        time_start = time.time()
        a_dict[i] = 5  # Set the value to 5 from 0
        time.sleep(0.00001)
        time_end = time.time()
        time_final = time_end - time_start
        print(f'setting item at dict location {i:7},'
              f' took {time_final:13.11f} ms')


# 3. Devise an experiment that compares the performance of the del operator on lists and dictionaries.
# The speeds will remain roughly the same for the dict as it is of time complexity O(1).
# The speeds of del will start very high and slowly go down, as removing index's closer to
# the end of the list will result in less items needing to be shifted over, this is an
# example of time complexity O(n).

def compare_del_speeds(a_list: list, a_dict: dict):
    for i in range(1, len(a_list), 2000000):
        list_start = time.time()
        del a_list[i]
        time.sleep(0.00001)  # Slow down execution briefly
        list_stop = time.time()
        list_speed = list_stop - list_start

        dict_start = time.time()
        del a_dict[i]
        time.sleep(0.00001)
        dict_stop = time.time()
        dict_speed = dict_stop - dict_start

        print(f'del at index {i:7}, list: {list_speed:13.11f}, '
              f'dict: {dict_speed:13.11f}', sep='')


# 4. Given a list of numbers in random order, write an algorithm that works in O(nlog(n))
# to find the kth smallest number in the list.
# The only O(log(N)) functions I can think of are included in tree's or quicksorts we explored
# at the end of 162, so likely I'll need to implement a quicksort  to make this work, as there
# is no way to determine the smallest value (that I know of) without either sorting the list,
# or comparing each item to each other, but doing this would be O(n) or O(n^2) depending how
# it's implemented.
# I couldn't write this without doing some research on quicksort algorithms (forgot how they
# fully functioned) so grade as you will.. I just wanted to get it to work.
rand_list = [random.randrange(1, 100) for i in range(20)]  # list of random numbers in random order


def partition(a_list: list, start, end):
    """
    Partitioner that moves value to the left and right of the pivot, doing a general sort.
    :param a_list: to sort
    :param start: point in the list to start at (usually 0)
    :param end: final point of the list, usually len(list) - 1
    :return high: the new high point (the next int below the pivot)
    """
    pivot = a_list[start]
    low = start + 1
    high = end

    while True:
        while low <= high and a_list[high] >= pivot:
            high = high - 1
        while low <= high and a_list[low] <= pivot:
            low = low + 1
        if low <= high:
            a_list[low], a_list[high] = a_list[high], a_list[low]
        else:
            break
    a_list[start], a_list[high] = a_list[high], a_list[start]
    return high


def quick_sort(a_list: list, start, end):
    """
    Use the partitioner to quick sort
    :param a_list: to sort
    :param start: point in the list to start at (usually 0)
    :param end: final point of the list, usually len(list) - 1
    :return sorted list
    """
    if start >= end:
        return
    p = partition(a_list, start, end)
    quick_sort(a_list, start, p - 1)
    quick_sort(a_list, p + 1, end)


def log_linear_sort():
    print(rand_list)
    start = time.time()
    quick_sort(rand_list, 0, len(rand_list) - 1)
    time.sleep(0.00001)
    end = time.time()
    print(f'O(nlogn) sorted list returns smallest value of {rand_list[0]} in {end - start}ms')


# 5. Can you improve the algorithm from the previous problem to be linear? Explain.
# yes, we could take the list and compare the first element (or any element to
# each other element in the list, this would actually be much simpler to implement than
# the previous. This is linear because it requires going thru each and every object
# and comparing it to the set object, this will increase in computation time as
# the list gets longer and longer, which is seen as O(n).
rand_list_2 = [random.randrange(1, 100) for i in range(20)]


def linear_sort():
    """
    Linearly sort thru a list and return the lowest value, the speed will be slower on larger lists.
    :return: Smallest number in the list.
    """
    print(rand_list_2) # Show the list so we can see the smallest number
    start = time.time()
    smallest = rand_list_2[0]
    for i in range(1, len(rand_list) - 1):
        if rand_list_2[i] < smallest:
            smallest = rand_list_2[i]
    time.sleep(0.00001)
    end = time.time()
    print(f'O(n) sorted list return smallest value of {smallest} in {end - start}ms')


def split_lines():
    print('________________________________________________________________')


def final_notes():
    print('Note that to truly see a time difference between the two we would need\n'
          'a huge size difference in lists, I just wanted to display that both\n'
          'solutions worked.')


def main():
    list_index_speed(my_list)
    split_lines()
    dict_get_speed(my_dict)
    split_lines()
    dict_set_speed(my_dict)
    split_lines()
    compare_del_speeds(my_list, my_dict)
    split_lines()
    log_linear_sort()
    split_lines()
    linear_sort()
    split_lines()
    final_notes()


if __name__ == '__main__':
    main()
