import random


WORD_LIST = ['apple', 'banana', 'carrot', 'dinosaur', 'python', 'project', 
             'fire', 'goat', 'shrimp', 'lobster', 'rabbit', 'house']


try:
    _input = raw_input
except NameError:
    _input = input


# Internal helpers
def _get_random_word(word_list):
    """
    Returns a random word from the word_list to use as the answer word.
    :param word_list: The list of possible answer words
    """
    idx = random.randint(0, len(word_list))
    return word_list[idx]


def _mask_word(word):
    """
    Takes the answer word and returns a string of '*' characters of the 
    same length to show the user the masked word.
    :param word: The answer word for the current game
    Example: word - 'cat'     masked word - '***'
    """
    return len(word) * '*'


def _guess_is_valid(guessed_letter, previous_guesses):
    """
    Checks if the letter guessed is one character long, has not already been 
    guessed, and verifies the character guessed is a letter in the alphabet. 
    :param guessed_letter: The letter the user guesses
    :param previous_guesses: A string of all the letters previously guessed
    Returns True if given guess is valid, False otherwise.
    """
    if (len(guessed_letter) == 1 and guessed_letter.isalpha() and 
            guessed_letter not in previous_guesses):
        return True
    print("Invalid guess. Try again.")
    return False


def _check_lose(remaining_misses):
    """
    Returns True if remaining guesses is equal to 0 and false otherwise.
    :param remaining_misses: How many misses are left before user loses
    """
    if remaining_misses == 0:
        print("You lose!")
        return True
    return False


def _check_win(answer_word, masked_word):
    """
    Returns True if answer word matches the masked word and False otherwise.
    This works because the masked word is updated each time a correct letter
    is guessed to replace that '*' character with the correct letter. If the 
    user has one, matched word and answer word will be the same.
    :param answer_word: The answer word for the current game
    :param masked_word: The answer word masked with '*' characters for letters
                        that haven't been guessed
    """
    if answer_word == masked_word:
        print("You win!")
        return True
    return False


def _check_game_over(answer_word, masked_word, remaining_misses):
    """
    Returns True if _check_win is True or _check_lose is True, and False
    otherwise.
    :param answer_word: The answer word for the current game
    :param masked_word: The answer word masked with '*' characters for letters
                        that haven't been guessed
    :param remaining_misses: How many misses are left before user loses
    """
    if _check_lose(remaining_misses) or _check_win(answer_word, masked_word):
        print("Game Over.")
        return True
    return False



# Public interface
def start_new_game(answer_word=None):
    """
    Creates and returns a new game configuration.
    :param answer_word: Optional manually chosen answer word for game with
                        default value of None if nothing is provided.
    This returns a collection that stores 4 pieces of game information:
    answer_word - The answer word that is the solution to the game
    masked_word - The answer word masked with '*' characters
    previous_guesses - The previous valid letter guesses the user has inputted
    remaining_misses - how many misses the user has left. Start with 5.
    """
    if answer_word == None:
        answer_word = _get_random_word(WORD_LIST)
    masked_word = _mask_word(answer_word)
    print(answer_word, masked_word)
    print("Welcome to Hangman!")
    print("This is the word to guess: " + masked_word)
    print("You have 5 misses remaining")
    return {
        'answer_word' : answer_word,
        'masked_word' : masked_word,
        'previous_guesses' : '',
        'remaining_misses' : 5
    }


def guess_letter(game, letter):
    """
    This function receives a valid guess and processes it.
    If it is a correct guess, it updates the masked_word in the collection
    by replacing the '*' characters with letters that have been correctly
    guessed. 
    If it is an incorrect guess, update remaining_misses in the game so it has 
    one less.
    Finally, update the previous_guesses in the game to reflect the letter that
    has been guessed.
    You are only updating values in your collection so no return required for
    this function.
    :param game: The collection storing current game information
    :param letter: The letter that is being guessed
    """
    game['previous_guesses'] += letter
    if letter in game['answer_word']:
        new_masked_str = ""
        for idx in range(len(game['answer_word'])):
            if letter == game['answer_word'][idx]:
                new_masked_str += letter
            else:
                new_masked_str += game['masked_word'][idx]
        game['masked_word'] = new_masked_str
    else:
        game['remaining_misses'] -= 1


def user_input_guess(game):
    """
    Repeats user input guesses until game is over. If guess is invalid,
    repeat input until it is valid. Once guess is valid, process the guess.
    :param game: The collection storing current game information
    """
    while not _check_game_over(game['answer_word'], game['masked_word'],
            game['remaining_misses']):
        guess = _input("Guess a letter: ")
        if not _guess_is_valid(guess, game['previous_guesses']):
            continue
        guess_letter(game, guess)
        print("This is the word to guess: " + game['masked_word'])
        print("You have " + str(game['remaining_misses'])+ " misses remaining")


game = start_new_game()
user_input_guess(game)


