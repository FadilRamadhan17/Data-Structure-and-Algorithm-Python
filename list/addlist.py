import sys

n = 100

numbers = []
old_size = 0

for i in range(n):
    new_size = sys.getsizeof(numbers)

    if new_size != old_size:
        print(len(numbers), new_size)
        old_size = new_size

    numbers.append(1)