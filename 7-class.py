import random
import pickle
import os
#KLASSER

#1. Dish
class Dish:
    def __init__(self, name, price, food_type, calories):
        self.name = name
        self.price = price
        self.food_type = food_type
        self.calories = calories

food_list = [
    Dish("Veggie burger", 10.50, "vegetarian", 450),
    Dish("Chicken sandwich", 12.50, "meat", 600),
    Dish("Vegan sushi", 8.00, "vegan", 350),
    Dish("Salmon salad", 15.00, "meat", 300),
    Dish("Falafel wrap", 9.00, "vegetarian", 400),
    Dish("Grilled tofu", 11.00, "vegan", 250),
]

def get_lunch_menu(food_list):
    vegetarian_options = []
    vegan_options = []
    meat_options = []

    for food in food_list:
        if food.food_type == "vegetarian":
            vegetarian_options.append(food.name)
        elif food.food_type == "vegan":
            vegan_options.append(food.name)
        else:
            meat_options.append(food.name)

    menu = "Today's lunch menu:\n"
    if vegetarian_options:
        menu += f"\nVegetarian options:\n{', '.join(vegetarian_options)}"
    if vegan_options:
        menu += f"\nVegan options:\n{', '.join(vegan_options)}"
    if meat_options:
        menu += f"\nMeat options:\n{', '.join(meat_options)}"
    return menu

def show_today_dishes():
    print(get_lunch_menu(food_list))

#2. Person - Moving in with someone
class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        self._address  = None
    
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    def move_in_with(self, other_person):
        self._address = other_person.address

def person_moving_in():
    john = Person("John", "1990-01-01")
    jane  = Person("Jane", "1995-02-15")

    john.address = "123 Main St."
    jane.address = "456 Elm St."

    print(f"{john.name}'s address is {john.address}")
    print(f"{jane.name}'s address is {jane.address}")

    john.move_in_with(jane)

    print(f"{john.name}'s address is {john.address}")
    print(f"{jane.name}'s address is {jane.address}")

#3. Kennel with dogs - Array and File
class Dog:
    def __init__(self, name, race, age, weight):
        self.name = name
        self.race = race
        self.age = age
        self.weight = weight
        
    def tail_length(self):
        if self.race == 'dachshund':
            return 3.7
        else:
            return self.age * self.weight / 10

# create a kennel list to hold the dogs
dogs = []
filename = "dogs.txt"

# Default functions
def add_ten_dogs():
    # create a list of random names, races, ages, and weights
    names = ['Fido', 'Rex', 'Buddy', 'Daisy', 'Max', 'Charlie', 'Rocky', 'Luna', 'Toby', 'Bailey']
    races = ['labrador', 'poodle', 'bulldog', 'beagle', 'golden retriever', 'chihuahua', 'dachshund', 'boxer', 'shih tzu', 'husky']
    ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    weights = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    # add 10 random dogs to the kennel
    for i in range(10):
        name = random.choice(names)
        race = random.choice(races)
        age = random.choice(ages)
        weight = random.choice(weights)
        dog = Dog(name, race, age, weight)
        dogs.append(dog)
    return dogs

def add_dog():
    name = input("Enter dog's name: ")
    race = input("Enter dog's race: ")
    age = int(input("Enter dog's age: "))
    weight = int(input("Enter dog's weight: "))
    return Dog(name, race, age, weight)

def list_dogs():
    min_tail_length = int(input("Enter minimum tail length: "))
    print("Dogs with longer tail length than", min_tail_length)
    return min_tail_length

def formula_dog(dog, min_tail_length):
    if dog.tail_length() >= min_tail_length:
        print(f"{dog.name} {dog.race} {dog.age} years {dog.weight} kg tail = {dog.tail_length():.1f}")

class Kennel:
    def __init__(self):
        self.dogs = dogs

    def add_to_array(self):
        new_dog = add_dog()
        self.dogs.append(new_dog)
        print(f"{new_dog.name} has been registered in the kennel!")

    def add_to_file(self):
        new_dog = add_dog()
        with open(filename, 'a') as f:
            f.write(f"{new_dog.name},{new_dog.race},{new_dog.age},{new_dog.weight}\n")
        print(f"{new_dog.name} has been added to the file!")

        
    def list_dogs_from_array(self):
        min_tail_length = list_dogs()
        for dog in self.dogs:
            formula_dog(dog, min_tail_length)

    def list_dogs_from_file(self):
        min_tail_length = list_dogs()
        with open(filename, "r") as f:
            for line in f:
                name, race, age, weight = line.strip().split(",")
                age, weight = int(age), float(weight)
                dog = Dog(name, race, age, weight)
                formula_dog(dog, min_tail_length)

        
    def remove_dog_from_array(self):
        name = input("Enter name of dog to remove: ")
        for dog in self.dogs:
            if dog.name == name:
                self.dogs.remove(dog)
                print(f"{dog.name} removed from kennel.")
                break
        else:
            print(f"No dog named {name} was found in the kennel.")

    def remove_dog_from_file(self):
        name = input("Enter name of dog to remove: ")
        with open(filename, 'r+') as f:
            lines = f.readlines()
            filtered_lines = [line for line in lines if name not in line]
            f.seek(0)
            f.writelines(filtered_lines)
            f.truncate()
        if len(lines) == len(filtered_lines):
            print(f"No dog named {name} was found in the file.")
        else:
            print(f"{name} removed from file.")

    def add_all_dogs_to_array(self):
        add_ten_dogs()

    def add_all_dogs_to_file(self):
        dogs = add_ten_dogs()

        with open(filename, 'w') as f:
            for dog in dogs:
                dog_str = f"{dog.name},{dog.race},{dog.age},{dog.weight}\n"
                f.write(dog_str)
        
    def run(self):
        type = input("1. array, 2. file: ")

        if type == '1':
            # add 10 random dogs to the kennel
            self.add_all_dogs_to_array()

            while True:
                print("\n1. Add to array")
                print("2. List from array")
                print("3. Remove from array")
                print("4. Quit")
            
                choice = input("Enter your choice: ")
                if choice == '1':
                    self.add_to_array()
                elif choice == '2':
                    self.list_dogs_from_array()
                elif choice == '3':
                    self.remove_dog_from_array()
                elif choice == '4':
                    print("Exiting program.")
                    break
                

        elif type == '2':
            while True:
                print("\n1. Add to file")
                print("2. List from file")
                print("3. Remove from file")
                print("4. Quit")
                print("5. Add dogs to file")

                choice = input("Enter your choice: ")
                if choice == '1':
                    self.add_to_file()
                elif choice == '2':
                    self.list_dogs_from_file()
                elif choice == '3':
                    self.remove_dog_from_file()
                elif choice == '4':
                    print("Exiting program.")
                    break
                elif choice == '5':
                    self.add_all_dogs_to_file()
                else:
                    print("Invalid choice, try again.")


def run_kennel():
    kennel = Kennel()
    kennel.run()

if __name__ == '__main__':
    run_kennel()