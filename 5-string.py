import re

#1. Concatenate strings
def concatenate_strings_default():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    string3 = input("Enter the third string: ")
    concatenated_string = string1 + string2 + string3
    print("The concatenated string is:", concatenated_string)

def concatenate_strings():
    strings = [input("Enter string {}: ".format(i)) for i in range(1, 4)]
    concatenated_string = ''.join(strings)
    print("The concatenated string is:", concatenated_string)

#2. Edit string remove w
def string_index():
    text = "Hello, world"
    w_position = text.index('w')
    print(f"The position of the first 'w' in the text is {w_position}")
    text = text[:w_position] + text[w_position+1:]
    print(text)

#3. Capitalize
def capitalize_names():
    name = "johan lindqvist"
    names = name.split()
    capitalized_names = [n.capitalize() for n in names]
    capitalize_names = ' '.join(capitalized_names)
    print(capitalize_names)

#4. Replace and count
def replace_and_count():
    text = "Detta är en sträng som du skall ändra"
    text = text.replace(' ', '*')
    count = text.count('*')
    print(text)
    print(f"The number of asterisks in the string is {count}")

#5. Mail address
def check_email():
    email = "hellothere@gmail.com"
    #email = input("Enter an email address: ")
    pattern = r'^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$'
    if re.match(pattern, email):
        print("The email address is valid.")
    else:
        print("Error: The email address is invalid.")

#6. count words in sentence
def count_words():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    word_count = len(words)
    print(f"The sentence '{sentence}' consists of {word_count} words.")

#7. Palindrome
def check_palindrome():
    text = input("Enter a word or sentence: ").lower().replace(" ", "")
    print("The input is a palindrome." if text == text[::-1] else "The input is not a palindrome.")

if __name__ == '__main__':
    check_email()
