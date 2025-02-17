# Time complexity is O(1), because the algorithm has no loops and it executes the same steps independent of the imput.
def middle(numbers):
    n = len(numbers)
    return numbers[n // 2]

print(middle([1,2,3,4,5,6,7,7]))

# Single Loops is O(n), n = len of the numbers
# O(n), because the algorithm has a single loop that goes through the element f the list 
def calc_sum(numbers):
    result = 0
    for x in numbers:
        result += x
    return result

print(calc_sum([1,2,3,4,5,6,7,7]))

# Nested Loops is O(n^2)/0(n^k) --> k is depends on a sum of loops
# 0(n^2), bacause the algorithm contains a loop inside a loop
def has_sum(numbers, x):
    for a in numbers:
        for b in numbers:
            if a + b == x:
                return True
    return False

print(has_sum([1,2,3,4,5,6,7,7], 5))

# Sequential code segments
# Time complexity in stage 1 is O(n), stage 2 is O(n) and the whole algorithm is O(n)
def count_min(numbers):
    # stage 1
    min_value = numbers[0]
    for x in numbers:
        if x < min_value:
            min_value = x

    # stage 2
    result = 0
    for x in numbers:
        if x == min_value:
            result += 1
    
    return result

print(count_min([1,2,8,1,5,6,1,1]))