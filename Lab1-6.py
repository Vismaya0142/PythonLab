
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def reverse_number(number):
    return int(str(number)[::-1])

number = int(input("Enter a four-digit number: "))

if 1000 <= number <= 9999:
    
    digit_sum = sum_of_digits(number)
    
    reversed_number = reverse_number(number)

    
    print(f"The sum of the digits is: {digit_sum}")
    print(f"The reverse of the number is: {reversed_number}")
else:
    print("Please enter a valid four-digit number.")
