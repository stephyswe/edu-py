import random
import pickle
#SPEL

#1. Gissa ett tal mellan 1 och 100
def play_game_guess():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = input("Guess a number between 1 and 100: ")
        if not guess.isdigit():
            print("You can only write a number with numbers. Try again!")
            continue
        guess = int(guess)
        attempts += 1
        if guess < number:
            print("The number is bigger.")
        elif guess > number:
            print("The number is smaller.")
        else:
            print(f"Right! You guessed right on {attempts} attempts.")
            break

    play_again = input("Do you want to play again (yes/no)? ").lower()
    if play_again == "yes":
        play_game_guess()
    else:
        print("Thanks for playing!")

#2. Add Highscore to Gissa ett tal
HIGHSCORE_FILE = 'highscores.pkl'

class Highscore:
    def __init__(self):
        self.scores = []
        try:
            with open(HIGHSCORE_FILE, 'rb') as f:
                self.scores = pickle.load(f)
        except FileNotFoundError:
            pass
    
    def save(self):
        with open(HIGHSCORE_FILE, 'wb') as f:
            pickle.dump(self.scores, f)
    
    def add_score(self, name, attempts):
        self.scores.append((name, attempts))
        self.scores.sort(key=lambda x: x[1])  # sort by attempts
        self.scores = self.scores[:10]  # keep only top 10
        self.save()
    
    def show_highscore(self):
        print('Highscore:')
        for i, (name, attempts) in enumerate(self.scores):
            print(f'{i+1}. {name}: {attempts} attempts')
        print()


def play_game_guess_with_highscore():
    # initialize game
    answer = random.randint(1, 100)
    attempts = 0

    # play game
    while True:
        guess = input('Guess a number between 1 and 100: ')
        attempts += 1

        if not guess.isnumeric():
            print('You can only write a number with numbers. Try again!')
            continue

        guess = int(guess)

        if guess < 1 or guess > 100:
            print('Your guess must be between 1 and 100. Try again!')
            continue

        if guess < answer:
            print('The answer is bigger.')
        elif guess > answer:
            print('The answer is smaller.')
        else:
            print(f'Right! You guessed right on {attempts} attempts.')
            highscore = Highscore()
            highscore.show_highscore()
            if len(highscore.scores) < 10 or attempts < highscore.scores[-1][1]:
                name = input("You've made it into the highscore list! What's your name? ")
                highscore.add_score(name, attempts)
                highscore.show_highscore()
            play_again = input('Do you want to play again (yes/no)? ')
            if play_again.lower() in ['no']:
                break
    print('Thanks for playing!')

def start_game_guess_with_highscore():
        highscore = Highscore()
        while True:
            print("\nMenu:")
            print("1. Play")
            print("2. Show highscore")
            print("3. Quit")
            choice = input("Enter your choice: ")
            if choice == "1":
                play_game_guess_with_highscore()
            elif choice == "2":
                highscore.show_highscore()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Try again.")

        print("Thanks for playing!")

if __name__ == '__main__':
    start_game_guess_with_highscore()