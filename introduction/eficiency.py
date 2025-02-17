import random
import time

def max_diff(numbers, v=1):
    if v==1:
        result = 0
        for x in numbers:
            for y in numbers:
                result = max(result, abs(x - y))
        return result
    
    if v==2:
        sorted_num = sorted(numbers)
        return sorted_num[-1] -  sorted_num[0]
    
    if v==3:
        return max(numbers) - min(numbers)

n = 10000
print('n:', n)
random.seed(1337)
numbers = [random.randint(1, 10**6) for _ in range(n)]

start_time1 = time.time()
resultV1 = max_diff(numbers, v=1)
end_time1 = time.time()

start_time2 = time.time()
resultV2 = max_diff(numbers, v=2)
end_time2 = time.time()

start_time3 = time.time()
resultV3 = max_diff(numbers, v=3)
end_time3 = time.time()

print(f"resultV1: {resultV1}")
print(f"timeV1: {round(end_time1 - start_time1, 2)} s")

print(f"resultV2: {resultV2}")
print(f"timeV2: {round(end_time2 - start_time2, 2)} s")

print(f"resultV3: {resultV3}")
print(f"timeV3: {round(end_time3 - start_time3, 2)} s")