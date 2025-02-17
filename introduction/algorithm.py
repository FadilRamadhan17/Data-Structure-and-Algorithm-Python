def count_even(numbers, v=1):
    if v==1:
        result = 0
        for i in numbers:
            if i % 2 == 0:
                result += 1
        return result
    
    if v==2:
        return sum(i % 2 == 0 for x in numbers)
    
def max_dif(numbers, v=1):
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
