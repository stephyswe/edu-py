import datetime

# IF-SATSER

# 1. Check if a number is greater than 10
def check_number():
    number = int(input("Enter a number: "))
    if number > 10:
        print("The number is greater than 10.")
    else:
        print("The number is less than 10.")

# 1. Check num_packets of milk and order more if needed
def order_milk():
    num_packets = int(input("Enter the number of packets of milk left: "))
    
    if num_packets < 10:
        print("Order 30 packages.")
    elif num_packets >= 10 and num_packets <= 20:
        print("Order 20 packages.")
    else:
        print("You do not need to order any milk.")

# 3. Check which number is larger
def find_largest():
    # Prompt the user to enter two numbers
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    # Find the larger of the two numbers
    largest = max(number1, number2)

    # Print the result
    print("The largest number is:", largest)

# 4. Check the larger of the three numbers
def find_largest_by_three():
    # Prompt the user to enter three numbers
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    number3 = float(input("Enter the third number: "))

    # Find the largest of the three numbers
    largest = max(number1, number2, number3)

    # Print the result
    print("The largest number is:", largest)

# 5. Calculate the trip cost based on the category
def calculate_trip_cost():
    category = ""
    while category != "pensioner" and category != "student" and category != "adult":
        # Prompt the user to enter their category
        category = input("Enter your category (pensioner, student, adult): ")

        # Determine the trip cost based on the category
        if category == "pensioner" or category == "student":
            cost = 20
        elif category == "adult":
            cost = 30
        else:
            print("Invalid input. Please enter either pensioner, student, or adult.")
    # Print the result
    print("The trip cost for a", category, "is SEK", cost)

# 6. Determine the decade of birth
def decadeOfBirth():
    current_year = datetime.datetime.now().year
    while True:
        year_of_birth = input("Enter your year of birth: ")
        if not year_of_birth.isdigit():
            print("Invalid input. Please enter a valid year of birth.")
            continue
        year_of_birth = int(year_of_birth)
        if year_of_birth < 1900 or year_of_birth > current_year:
            print("Invalid input. Please enter a valid year of birth.")
            continue
        break
    
    if 1980 <= year_of_birth < 1990:
        print("You were born in the 1980s.")
    elif 1990 <= year_of_birth < 2000:
        print("You were born in the 1990s.")
    else:
        print("You were not born in 1990 or the 1980s.")

# 7. check if a country is in Scandinavia
def checkScandinavia():
    country = input("Enter the name of the country where you live: ")
    if country.lower() in ["sweden", "denmark", "norway", "finland"]:
        print("You live in Scandinavia.")
    else:
        print("You do not live in Scandinavia.")

# 8. Check ordering food based on the sum of money and discount
def orderFood():
    while True:
        try:
            sum_of_money = float(input("Enter how much money you have: "))
            if sum_of_money < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a valid sum of money.")
            continue
    
    while True:
        discount = input("Do you have a discount? (yes/no): ")
        if discount.lower() not in ['yes', 'no']:
            print("Invalid input. Please enter either yes or no.")
            continue
        break
    
    if 15 <= sum_of_money <= 25:
        if discount.lower() == 'yes':
            print("You can buy a small hamburger and fries.")
        else:
            print("You can buy a small hamburger.")
    elif 25 < sum_of_money <= 50:
        if discount.lower() == 'yes':
            print("You can buy a large hamburger and fries.")
        else:
            print("You can buy a large hamburger.")
    elif sum_of_money > 50 or (50 < sum_of_money <= 60 and discount.lower() == 'yes'):
        print("You can buy a meal with a drink.")
    else:
        print("Sorry, you don't have enough money to buy anything.")


if __name__ == '__main__':
    decadeOfBirth()