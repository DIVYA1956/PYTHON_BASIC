def get_number():
    while True:
        user_input = input("Enter a number: ")
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def check_even_odd(number):
    if number % 2 == 0:
        return "Even number"
    else:
        return "Odd number"


def main():
    number = get_number()
    result = check_even_odd(number)
    print(result)


if __name__ == "__main__":
    main()