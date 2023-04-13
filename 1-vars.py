# 3. String och Int
"""
Skapa en variabel string name med ditt namn
Skapa en int age med din ålder.
Skriv sedan ut Jag heter Kalle (innehållet i name) och är 27(innehållet i age) år.
"""


def stringInt():
    name = "Kalle"
    age = 27
    print("Jag heter", name, "och är", age, "år.")

# 4. Skriv ett program som frågar efter förnamn och efternamn och skriver ut en hälsning.


def firstNameLastName():
    firstname = input("Förnamn: ")
    lastname = input("Efternamn: ")
    print("Hej", lastname, firstname)

# 5. Operators - Skapa en applikation där användaren matar in två tal (heltal!)


def twoNumbers():
    # int numbers - number1 = input('mata in tal 1\n')
    number1 = float(input('mata in tal 1\n'))
    number2 = float(input('mata in tal 2\n'))

    # Calculate number1 raised to number2
    result1 = number1 ** number2
    print("Number 1 raised to number 2:", result1)

    # Calculate number1 times number2
    result2 = number1 * number2
    print("Number 1 times number 2:", result2)

    # Calculate number1 divided by number2
    result3 = number1 / number2
    print("Number 1 divided by number 2:",
          result3, "Data Type:", type(result3))

    # Calculate number1 plus number2
    result4 = number1 + number2
    print("Number 1 plus number 2:", result4)

    # Calculate number1 minus number2
    result5 = number1 - number2
    print("Number 1 minus number 2:", result5)

    # Calculate number1 integer divided by number2
    result6 = number1 // number2
    print("Number 1 integer divided by number 2:", result6)

    # Calculate the remainder from integer division of number1 and number2
    result7 = number1 % number2
    print("Remainder from integer division of number 1 and number 2:", result7)


# 7. Strängoperatorer (String operators)
def repeat_name():
    # Prompt the user to enter their name
    name = input("What is your name: ")

    # Create a new variable with the name repeated five times
    repeated = name * 5

    # Print the new variable
    print(repeated)

# 8. Jämför-operatorer (Compare operators)


"""
Skriv ett program som tar ett TAL (int) som input. 
Det ska skriva ut False om talet är mindre än 100 och True om det är större eller lika med 100,
OBS: Utan If-satser. (skriv direkt ut resultat från jämförelsen)
"""


def check_number():
    number = int(input("Enter a number: "))
    print(number >= 100)


if __name__ == '__main__':
    check_number()
