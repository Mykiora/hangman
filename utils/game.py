from random import randint

class Hangman:
    def __init__(self) -> None:
        """
        Constructor method. Initializes the possible words list, empty lists for
        player's guesses, turn/life/error counters, and selects randomly a word in the list.
        """
        self.possible_words = ['becode', 'learning', 'mathematics', 'session']
        # Select a word randomly in the possible_words list
        self.word_to_find = self.possible_words[randint(0, len(self.possible_words) - 1)]
        self.lives = 5
        # Generate a list containing underscores depending of the words's number of letters.
        self.correctly_guessed_letters = ['_' for letter in self.word_to_find]
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0
    
    def play(self) -> None:
        """
        Function that will manage a single turn. Gets player's input, check for validity,
        then updates the word's correctly and wrongly guessed as well as life, error, and
        turn count.
        """
        letter = input('Choose a letter : ')
        # Stay in the loop as long as the user input is not a single alpha character.
        while not letter.isalpha() or len(letter) > 1 or letter in self.wrongly_guessed_letters or letter.upper() in self.correctly_guessed_letters:
            print('Invalid input. Enter only one letter that you have not already used.')
            letter = input('Please try again : ')
        # When the input is correct, we are out of the loop. Check if the input is in the word.
        if letter in self.word_to_find:
            # Keep track of the letters' index to have an easier time replacing underscores.
            for index, current_letter in enumerate(self.word_to_find):
                if current_letter == letter:
                    self.correctly_guessed_letters[index] = letter.upper()
        else:
            self.wrongly_guessed_letters.append(letter)
            self.error_count += 1
            self.lives -= 1
        self.turn_count += 1

    def start_game(self) -> None:
        """
        Starts the game and manages the main loop. Displays the game's state every turn
        as long as the player has lives left.
        """
        while '_' in self.correctly_guessed_letters:
            self.play()
            if self.lives == 0:
                self.game_over()
            print(f'\nTurn {self.turn_count}')
            print(f"Your word : {' '.join(self.correctly_guessed_letters)}")
            print(f"Wrong letters : {', '.join(self.wrongly_guessed_letters)}")
            print(f'You have {self.lives} live(s) left.')
            print(f'You have made {self.error_count} mistake(s) so far.\n')
        self.well_played()

    def game_over(self) -> None:
        """
        Displays game over message and stops the program.
        """
        print('No more lives. Game Over.')
        exit()

    def well_played(self) -> None:
        """
        Displays a "congratulations" message to the user.
        """
        print(f'You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} error(s) !')
    