import random
# LOOPAR

# 1. Skriv 0-10. For- & while loop.
def print_numbers_with_for():    
    for i in range(11):
            print(i)


def print_numbers_with_while():
    i = 0
    while i < 11:
        print(i)
        i += 1

# 2. Skriv input från användaren. For- & while loop.
def printNumbers():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Using for loop:")
    for num in range(num1, num2+1):
        print(num)
    print("Using while loop:")
    num = num1
    while num <= num2:
        print(num)
        num += 1

# 3. Add number and ask if user wants to continue
def get_valid_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def addNumbers():
    num1 = get_valid_number("Enter the first number: ")
    num2 = get_valid_number("Enter the second number: ")
    
    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}.")
    
    while True:
        answer = input("Do you want to continue (Y/N)? ")
        if answer.lower() == 'y':
            addNumbers()
            break
        elif answer.lower() == 'n':
            print("Goodbye!")
            return
        else:
            print("Invalid input. Please enter either Y or N.")
            continue

#4. Sum of 10 inputs. Combine for loop, while loop and try/except
def sum_of_inputs():
    total_sum = 0
    for i in range(10):
        while True:
            try:
                num = float(input("Enter a number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
        total_sum += num

    print("The sum of what you entered is:", total_sum)

#5. Print numbers less than input
def print_digits_less_than():
    num = int(input("Enter a number: "))
    i = 1
    while i < num:
        print(i)
        i += 1

#6. Throw two dice

def roll_dice():
    while True:
        print("Rolling the dice...")
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print("You rolled {} and {} for a total of {}".format(dice1, dice2, dice1+dice2))
        play_again = input("Roll the dice again? (Y/N): ")
        if play_again.lower() in ['y', 'yes']:
            continue
        else:
            break

if __name__ == '__main__':
    roll_dice()

