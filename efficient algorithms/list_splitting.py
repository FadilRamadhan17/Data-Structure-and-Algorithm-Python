# You are given a list containing n integers. Your task is to count how many ways one can split the list into two parts so that both parts have the same total sum of elements.

number = [1,-1,1,-1,1,-1,1,-1]

# O(n^2)
def count_splits(numbers):
    n = len(numbers)
    result = 0
    for i in range(n-1):
        left_sum = sum(numbers[0:i+1])
        right_sum = sum(numbers[i+1:])
        if left_sum == right_sum:
            result += 1
    return result

# O(n^2)
def count_splits1(numbers):
    n = len(numbers)
    result = 0
    left_sum = 0
    for i in range(n-1):
        left_sum += numbers[i]
        right_sum = sum(numbers[i+1:])
        if left_sum == right_sum:
            result += 1
    return result

# O(n)
def count_splits2(numbers):
    n = len(numbers)
    result = 0
    left_sum = 0
    total_sum = sum(numbers)
    for i in range(n-1):
        left_sum += number[i]
        right_sum = total_sum - left_sum
        if left_sum == right_sum:
            result += 1
    return result

print(count_splits2(number))