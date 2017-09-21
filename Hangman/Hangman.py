"""CS1- Hangman."""

# Scrape makeschool's website for words - Beautiful soup


def begin_game(word):
    """Choose the word and print blank spots."""
    chosen_word = word
    completed_word = ""
    for letters in chosen_word:
        completed_word += "_"
    print(completed_word)
    return completed_word


def guess(guesses):
    """Take in player guess."""
    guess = input("Make a guess: ")
    guessIsValid = isValid(guess, guesses)
    while(guessIsValid is False):
            guess = input("Please enter a valid character: ")
            guessIsValid = isValid(guess, guesses)
    return guess


def check_guess(guess, word):
    """Check the player's guess against the chosen word."""
    if guess in word:
        return True
    else:
        return False


def check_completion(completed_word):
    """Return True if word is complete."""
    if "_" in completed_word:
        return False
    else:
        print("Congrats! You Won!")
        return True


def isValid(guess, guesses):
    """Return True if the guess is valid."""
    if guess in guesses:
        print("You already guessed that ")
        return False
    elif type(guess) != str:
        return False
    elif len(guess) != 1:
        return False
    else:
        return True


def play_game(word, guesses, completed_word):
    """Play Main Function of the game."""
    playerGuess = guess(guesses)
    if check_guess(playerGuess, word):
        for index in range(len(completed_word)):
            if word[index] == playerGuess:
                completed_word[index] = playerGuess
        check_completion(completed_word)
    else:
        print("Sorry \'" + playerGuess + "\' is not in the word")
        guesses.append(playerGuess)
    print("Guesses: " + str(guesses))
    print(''.join(completed_word))


def setup_game():
    """Begin the game."""
    word = list("hangman")  # Should call choose word function when done
    guesses = []
    completed_word = list(begin_game(word))
    print(''.join(completed_word))
    while len(guesses) < 6 and check_completion(completed_word) is False:
        play_game(word, guesses, completed_word)
    if len(guesses) is 6:
        print("I'm sorry, you've used all your guesses and lost :(")
        print("The correct word was: " + str(word))
    else:
        if len(guesses) > 0:
            print("You only guessed " + str(len(guesses)) + " incorrect words")
        else:
            print("You guessed the word perfectly!!!")


setup_game()
