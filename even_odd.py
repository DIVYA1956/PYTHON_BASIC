def check_even_odd(num):
    if num % 2 == 0:
        return "Even number"
    else:
        return "Odd number"


try:
    number = int(input("Enter a number: "))
    result = check_even_odd(number)
    print(result)
except ValueError:
    print("Please enter a valid integer.")