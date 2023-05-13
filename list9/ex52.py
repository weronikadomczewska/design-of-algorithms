import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from robot_generator import *

def quick_sort_by_price(list_of_robots):
    if len(list_of_robots) <= 1:
        return list_of_robots

    pivot = list_of_robots[len(list_of_robots) // 2]["price"]
    less = []
    equal = []
    greater = []

    for d in list_of_robots:
        if d["price"] < pivot:
            less.append(d)
        elif d["price"] == pivot:
            equal.append(d)
        else:
            greater.append(d)

    # Recursively sort the sublists
    sorted_robots = quick_sort_by_price(less) + equal + quick_sort_by_price(greater)
    return sorted_robots

def update_plot(i):
    ax.clear()
    ax.bar(range(len(prices[i])), prices[i])
    ax.set_xlabel("Index")
    ax.set_ylabel("Price")
    ax.set_title("Quick Sort Visualization")

    # Stop the animation after the last frame
    if i == len(prices) - 1:
        ani.event_source.stop()

data = load_robots_from_file("robots.json")

prices = []
prices.append([d["price"] for d in data])

sorted_data = quick_sort_by_price(data)
prices.append([d["price"] for d in sorted_data])

fig, ax = plt.subplots()
ani = FuncAnimation(fig, update_plot, frames=len(prices), interval=500)
plt.show()

print(sorted_data)
