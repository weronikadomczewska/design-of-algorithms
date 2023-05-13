import matplotlib.pyplot as plt
from robot_generator import *
from matplotlib.animation import FuncAnimation


def heap_sort_by_price(lst):
    n = len(lst)
    prices = [d["price"] for d in lst]
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(lst, n, i)

    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        max_heapify(lst, i, 0)
        prices[i] = lst[i]["price"]
    return lst


def max_heapify(lst, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and lst[left]["price"] > lst[largest]["price"]:
        largest = left
    if right < n and lst[right]["price"] > lst[largest]["price"]:
        largest = right
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        max_heapify(lst, n, largest)

def update_plot(i):
    ax.clear()
    ax.bar(range(len(heap_prices[i])), heap_prices[i])
    ax.set_xlabel("Index")
    ax.set_ylabel("Price")
    ax.set_title("Heap Sort Visualization")

    # Stop the animation after the last frame
    if i == len(heap_prices) - 1:
        ani.event_source.stop()


data = load_robots_from_file("robots.json")

heap_prices = []
heap_prices.append([d["price"] for d in data])

n = len(data)
for i in range(n // 2 - 1, -1, -1):
    max_heapify(data, n, i)
    heap_prices.append([d["price"] for d in data])

for i in range(n - 1, 0, -1):
    data[i], data[0] = data[0], data[i]
    max_heapify(data, i, 0)
    heap_prices.append([d["price"] for d in data])

fig, ax = plt.subplots()
ani = FuncAnimation(fig, update_plot, frames=len(heap_prices), interval=200)
plt.show()



