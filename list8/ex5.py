from ex1 import *
from ex2 import *
from ex3 import *
from ex4 import *
import timeit
import matplotlib.pyplot as plt


def make_prices_unique(list_of_robots):
    unique_prices = set()
    for robot in list_of_robots:
        while robot["price"] in unique_prices:
            robot["price"] += 1
        unique_prices.add(robot["price"])
    return list_of_robots

def hash_function_times(list_of_robots, feature_name, alpha):
    hash_function_times = []
    for price in robots_prices:
        print(price)
        timing = timeit.timeit(lambda: robot_search(list_of_robots, feature_name, price, alpha), number=3)
        hash_function_times.append(timing)
        print(timing)
    return hash_function_times


robots_loaded_from_file = load_robots_from_file("robots.json")
sorted_robots = sort_robots_by_feature(robots_loaded_from_file, "price")
sorted_robots_with_unique_prices = make_prices_unique(sorted_robots)
robots_prices = [x["price"] for x in sorted_robots_with_unique_prices]

linear_search_times = []
for price in robots_prices:
    timing = timeit.timeit(
        lambda: find_robots_with_given_features_linear(sorted_robots_with_unique_prices, [None, price, None, None]),
        number=3)
    linear_search_times.append(timing)
    print(timing)

binary_search_times = []
for price in robots_prices:
    timing = timeit.timeit(lambda: binary_search(sorted_robots_with_unique_prices, "price", [price]), number=3)
    binary_search_times.append(timing)
    print(timing)

fig = plt.figure()
grid = plt.GridSpec(2, 2)

ax1 = plt.subplot2grid((1, 2), (0, 0))
ax1.plot(robots_prices, linear_search_times)
ax1.set_title("Linear search")
ax1.set_xlabel("price")
ax1.set_ylabel("time")

ax2 = plt.subplot2grid((2, 2), (0, 1))
ax2.plot(robots_prices, binary_search_times)
ax2.set_title("Binary search")
ax2.set_xlabel("price")
ax2.set_ylabel("time")
plt.tight_layout()
plt.show()

# fig = plt.figure()
# grid = plt.GridSpec(2, 2)
#
# # number_of_alphas = int(input("Enter number of alphas: "))
# number_of_alphas = 4
# alphas = [0.75, 0.6, 0.8, 0.9]
# # for i in range(number_of_alphas):
# #     alphas.append(float(input("Enter alpha: ")))
#
# ax3 = plt.subplot2grid((2, 2), (0, 0))
# ax4 = plt.subplot2grid((2, 2), (0, 1))
# ax5 = plt.subplot2grid((2, 2), (1, 0))
# ax6 = plt.subplot2grid((2, 2), (1, 1))
#
# hash_function_timings = {}
# cnt = 3
#
# for alpha in alphas:
#     hash_function_timings[f"ax{cnt}"] = hash_function_times(sorted_robots_with_unique_prices, "price", alpha)
#     cnt += 1
#
#
# ax3.plot(robots_prices, hash_function_timings["ax3"])
# ax3.set_title(f"Search with hash function alpha={alphas[0]}")
# ax3.set_xlabel("price")
# ax3.set_ylabel("time")
#
# ax4.plot(robots_prices, hash_function_timings["ax4"])
# ax4.set_title(f"Search with hash function alpha={alphas[1]}")
# ax4.set_xlabel("price")
# ax4.set_ylabel("time")
#
# ax5.plot(robots_prices, hash_function_timings["ax5"])
# ax5.set_title(f"Search with hash function alpha={alphas[2]}")
# ax5.set_xlabel("price")
# ax5.set_ylabel("time")
#
# ax6.plot(robots_prices, hash_function_timings["ax6"])
# ax6.set_title(f"Search with hash function alpha={alphas[3]}")
# ax6.set_xlabel("price")
# ax6.set_ylabel("time")
#
# plt.tight_layout()
# plt.show()





