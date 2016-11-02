import random
import pprint

WORD_LIST = ['apple', 'banana', 'carrot', 'dinosaur', 'python', 'project',
             'fire', 'goat', 'shrimp', 'lobster', 'rabbit', 'house']

try:
    _input = raw_input
except NameError:
    _input = input

# Internal helpers
def _get_random_word(word_list):
    new_word=word_list[random.randint(0,len(word_list)-1)]
    return new_word

def _mask_word(word):
    return len(word)*'*'

def _guess_is_valid(guessed_letter, previous_guesses):
    if len(guessed_letter)>1 or guessed_letter in '123456789' or guessed_letter in previous_guesses:
        return False
    return True

def _check_lose(remaining_misses):
    if remaining_misses==0:
        return True
    return False

def _check_win(answer_word, masked_word):
    if answer_word==masked_word:
        return True
    return False

def _check_game_over(answer_word, masked_word, remaining_misses):
    if _check_win(answer_word, masked_word) or _check_lose(remaining_misses):

        return True
    else:

        return False

# Public interface
def start_new_game(word_list, answer_word=None):
    if answer_word:
        new_word=answer_word
    else:
        new_word=_get_random_word(word_list)
        
    print (new_word)        
    info ={'answer_word':new_word,
           'masked_word':_mask_word(new_word),
           'previous_guesses':'',
           'remaining_misses':5 }
    return info

def guess_letter(game, letter):
    game['previous_guesses']+=letter
    if letter in game['answer_word']:
        a=''
        for i,j in enumerate(game['answer_word']):
            if letter==j:
                a+=j
            else:
                a+=game['masked_word'][i]
        else:
            game['masked_word']=a
        
    else:
        game['remaining_misses']-=1

def user_input_guess(game):
    while not _check_game_over(game['answer_word'], game['masked_word'],game['remaining_misses']):
        pprint.pprint(game)
        guess = _input("Guess a letter: ")
        if not _guess_is_valid(guess, game['previous_guesses']):
            continue
        guess_letter(game, guess)
        print("This is the word to guess: %s" % game['masked_word'])
        print("You have %s misses remaining" % game['remaining_misses'])

    else:
        print('end')

if __name__ == '__main__':
    game = start_new_game(WORD_LIST,answer_word='santiago')
    user_input_guess(game)
