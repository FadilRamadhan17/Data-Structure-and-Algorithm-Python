import random
# outline of an efficient algorithm

# example:stock trading
# Your task is figure out the highest profit you could have made if you had bought the stock on one day and sold it on another day.

day = [0,1,2,3,4,5,6,7]
price = [3,7,5,1,4,6,2,3]

# Here the highest profit is 6 – 1 = 5, achieved by buying on day 3 and selling on day 5.

# 0(n^2) its slow for big n
def best_profits_brute(price):
    n = len(price)
    best = 0
    for i in range(n):
        for j in range(i+1, n):
            best = max(best, price[j] - price[i])
    return best

# O(n)
def best_profits_fast(price):
    n = len(price)
    best = 0
    for i in range(n):
        min_price = min(price[0:i+1])
        best = max(best, price[i] - min_price)
    return best

# not ending looping
while True:
    n = random.randint(1,20)
    prices = [random.randint(1,10) for _ in range(n)]

    result_brute = best_profits_brute(prices)
    result_fast = best_profits_fast(prices)

    print(prices, result_brute, result_fast)

    if result_brute != result_fast:
        print("ERROR")
        break