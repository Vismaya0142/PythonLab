
numbers = [1, 2, 3, 4, 5]

def sum_list(lst):
    return sum(lst)

total = sum_list(numbers)
print(f"The sum of all the items in the list is: {total}")


def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result


product = multiply_list(numbers)
print(f"The product of all the items in the list is: {product}")


def get_largest_number(lst):
    return max(lst)

largest_number = get_largest_number(numbers)
print(f"The largest number in the list is: {largest_number}")

def get_smallest_number(lst):
    return min(lst)

smallest_number = get_smallest_number(numbers)
print(f"The smallest number in the list is: {smallest_number}")
