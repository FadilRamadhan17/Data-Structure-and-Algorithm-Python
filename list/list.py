numbers = [1,2,3,4,5]

# O(1) bcause the elements are in consecutive memory locations.
print(numbers[2]) # 3
numbers[2] = 5
print(numbers[2]) # 5

def list(numbers, type):
    # searching list
    if type == "search":
        print(3 in numbers)
        print(8 in numbers)

        print(numbers.index(3))
        print(numbers.count(3))

    # adding an elements
    elif type == "add":
        
        # O(1) because adding an element to the end pf a list does not require changes to other memory locations
        numbers.append(5)
        print(numbers)

        # O(n) because when an element is added to somewhere aele than the end of thelist, other elements need to be moved forwaed to make room for the new element
        numbers.insert(1,6)
        print(numbers)

    # removing an element
    elif type == "remove":
        
        # O(1) because other element are not affected
        numbers.pop()
        print(numbers)

        # O(n) because all the following elements have to be relocated in memory
        numbers.pop(1)
        print(numbers)
        
        # O(n), because it first has to find the first occurrence (similarly to the method index), and then remove the element and relocate the following elements.
        numbers.remove(3)
        print(numbers)

nums = [1,2,3,4,3,5,6,3]
list(nums, "search")

# O(n) because they have to scan through the list
def count(items, target):
    result = 0
    for item in items:
        if item == target:
            result += 1
    return result

print(count(numbers, 2))

# references and copying
def refandcopy(a, type):
    # the output comes was same a and b because a and b refer to the same list in memory
    if type == "ref":
        # 0(1) because copying the reference
        b = a
        a.append(6)
        print(f"a = {a}")
        print(f"b = {b}")
    
    elif type == "copy":
        # O(n) because copying the contents
        b = a.copy()
        a.append(6)
        print(f"a = {a}")
        print(f"b = {b}")


# side effects of functions
def double(numbers, type):
    if type == "ref":
        result = numbers
        for i in range(len(result)):
            result[i] *= 2
        return result
    elif type == "copy":
        result = numbers.copy()
        for i in range(len(result)):
            result[i] *= 2
        return result
    

numbers = [1,2,3,4,5]
numbers1 = [1,2,3,4,5]
print(double(numbers, "ref")) # [2,4,6,8,10]
print(numbers) # [2,4,6,8,10]
print(double(numbers1, "copy")) # [2,4,6,8,10]
print(numbers1) # [1,2,3,4,5]

# slicing and concatenation
numbers = [1,2,3,4,5,6,7,8]
# O(n) because it copies the contents form the old list to the new list
print(numbers[2:6]) # [3, 4, 5, 6]

first = [1,2,3,4]
second = [5,6,7,8]
print(first+second) # [1, 2, 3, 4, 5, 6, 7, 8]
