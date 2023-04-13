#FUNKTIONER

#1. Plussa
def merge_strings(str1, str2):
    return str1 + str2

def add():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    result = merge_strings(str1, str2)
    print("The merged string is:", result)

#2. Moms och pris
def calculate_vat():
    amount = 100.0
    vat_rate=0.25
    vat = amount * vat_rate
    print("VAT on", amount, "is", vat)

#3. Age
def check_legal_age(age):
    return age >= 18

def check_age():
    if check_legal_age(int(input("How old are you? "))):
        print("You are of legal age!")
    else:
        print("You are not of legal age yet.")

#4. Longest word
def longest_word():
    words = ['apple', 'banana', 'cherry']
    longest_word = max(words, key=len)
    print(f'The longest word is {longest_word}.')

#5. Calculate taxes
def calculate_taxes_on_salary(salary):
    tax_rate = 0.33 if salary >= 30000 else 0.12 if salary >= 15000 else 0.28
    return salary * tax_rate

def calculate_taxes():
    salary = 25000
    estimated_tax = calculate_taxes_on_salary(salary)
    print(f'The estimated tax on a monthly salary of {salary} is {estimated_tax:.2f}.')


if __name__ == '__main__':
    calculate_taxes()
