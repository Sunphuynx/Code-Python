def ex01():
    age = int(input("Enter your age: "))

    if age >=18:
        print("Eligible for voting")
    else:
        print("Not eligible for voting")

def ex02():
    number = int(input("Enter number: "))

    if number % 2 == 1:
        print("The number is odd")
    else:
        print("The number is even")

def ex03():
    number = int(input("Enter number: "))

    if number % 7 == 0:
        print("The number is divisible by 7")
    else:
        print("The number is not divisible by 7")

def ex04():
    number = int(input("Enter number: "))

    last_digit = number % 10

    if last_digit % 3 == 0:
        print("The number is divisible by 3")
    else:
        print("The number is not divisible by 3")

def ex05():
    correct_number = 7

    user_guess = int(input("Guess a number between 1 and 9: "))

    if user_guess == correct_number:
        print("Congratulations! You guessed the correct number.")
    elif user_guess < correct_number:
        print("Your guess is too low. Try again!")
    else:
        print("Your guess is too high. Try again!")


def ex06():
    day_number = int(input("Enter a number between 1 and 7: "))

    if day_number == 1:
        print("Sunday")
    elif day_number == 2:
        print("Monday")
    elif day_number == 3:
        print("Tuesday")
    elif day_number == 4:
        print("Wednesday")
    elif day_number == 5:
        print("Thursday")
    elif day_number == 6:
        print("Friday")
    elif day_number == 7:
        print("Saturday")
    else:
        print("Invalid input! Please enter a number between 1 and 7.")

if __name__ == '__main__':
   #ex01()
   #ex02()
   #ex03()
   #ex04()
   ex05()
   #ex06()