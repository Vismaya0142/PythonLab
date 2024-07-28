
def print_even_and_squares(start, end):
    for num in range(start, end):
        if num % 2 == 0:
            print(f"The square of {num} is {num ** 2}")

print("Even numbers and their squares in range(1, 50):")
print_even_and_squares(1, 50)

print("\nEven numbers and their squares in range(1, 100):")
print_even_and_squares(1, 100)
