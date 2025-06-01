import random

word_list=["python","hangman","Nice","Experience","code","alpha","internship"]

def choose_word():
    return random.choice(word_list).lower()

def display_word(word,guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])
def hangman():
    word=choose_word()
    guessed_letters=set()
    attempts_left=6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while attempts_left > 0:
        print("\nWord:",display_word(word,guessed_letters))
        print("Guessed letters:", ' '.join(sorted(guessed_letters)))
        print(f"Attempts left: {attempts_left}")

        guess=input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) !=1:
            print("Please enter a single alphabetical character.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.add(guess)

        if guess in word:
            print("correct guess!")
        else:
            print("Wrong Guess.")
            attempts_left -=1
        
        if all(letter in guessed_letters for letter in word):
            print(f"\n Congragulations! You Guessed the word: {word}")

hangman()