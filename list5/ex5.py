from ex2 import *
from ex3 import mergesort
import random
import timeit
import matplotlib.pyplot as plt


def generate_random_list(n, low, high):
    A = []
    for i in range(n):
        A.append(random.randint(low, high))
    return A


def single_test_mergesort(number_of_data):
    lst = generate_random_list(number_of_data, 0, 100)
    stmt = "mergesort(lst)"
    setup = "from ex3 import mergesort; lst = {}".format(lst)
    times = timeit.repeat(stmt=stmt, setup=setup, repeat=3, number=1)
    return sum(times) / 3

def single_test_find_max_elem(number_of_data):
    lst = generate_random_list(number_of_data, 0, 100)
    stmt = "find_max_elem_dividing(lst)"
    setup = "from ex2 import find_max_elem_dividing; lst={}".format(lst)
    times = timeit.repeat(stmt=stmt, setup=setup, repeat=3, number=1)
    return sum(times)/3


def single_test_find_second_max_elem(number_of_data):
    lst = generate_random_list(number_of_data, 0, 100)
    stmt = "find_second_max_elem_dividing(lst)"
    setup = "from ex2 import find_second_max_elem_dividing; lst={}".format(lst)
    times = timeit.repeat(stmt=stmt, setup=setup, repeat=3, number=1)
    return sum(times)/3

def single_test_find_mean(number_of_data):
    lst = generate_random_list(number_of_data, 0, 100)
    stmt = "find_mean(lst)"
    setup = "from ex2 import find_mean; lst={}".format(lst)
    times = timeit.repeat(stmt=stmt, setup=setup, repeat=3, number=1)
    return sum(times)/3



def get_mergesort_data(max_number_of_data):
    res = []
    for i in range(max_number_of_data):
        res.append(single_test_mergesort(i))
    return res


def get_find_max_value_data(max_number_of_data):
    res = []
    for i in range(1, max_number_of_data+1):
        res.append(single_test_find_max_elem(i))
    return res


def get_find_second_max_value_data(max_number_of_data):
    res = []
    for i in range(1, max_number_of_data+1):
        res.append(single_test_find_second_max_elem(i))
    return res


def get_find_mean_data(max_number_of_data):
    res = []
    for i in range(1, max_number_of_data+1):
        res.append(single_test_find_mean(i))
    return res




n = int(input("Enter maximum number of numbers in list: "))
ns = range(1, n+1)

mergesort_times = get_mergesort_data(n)
find_max_elem_times = get_find_max_value_data(n)
find_second_max_elem_times = get_find_second_max_value_data(n)
find_mean_times = get_find_mean_data(n)

ax1 = plt.subplot2grid((4, 3), (0, 0), colspan=3)
ax1.plot(ns, find_max_elem_times)
ax1.set_title("find max element")
ax2 = plt.subplot2grid((4, 3), (1, 0), colspan=3)
ax2.plot(ns, find_second_max_elem_times)
ax2.set_title("find second max element")
ax3 = plt.subplot2grid((4, 3), (2, 0), colspan=3)
ax3.plot(ns, find_mean_times)
ax3.set_title("find mean")
ax4 = plt.subplot2grid((4, 3), (3, 0), colspan=3)
ax4.plot(ns, mergesort_times)
ax4.set_title("merge sort")
plt.tight_layout()
plt.show()