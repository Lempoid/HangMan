import random
word_list = ["ardvaark", "baboon", "camel"]
GUESSES = 5

chosen_word = random.choice(word_list)
user_guess = ["_"] * len(chosen_word)
guesses_remaining = GUESSES
letters_to_guess = len(chosen_word)

while(letters_to_guess > 0 and guesses_remaining > 0):
    print(user_guess)
    user_chosen_character = input("choose a character to guess a word\n")

    if user_chosen_character in chosen_word:
        for i, char in enumerate(chosen_word):
            if user_chosen_character == char:
                user_guess[i] = user_chosen_character
                letters_to_guess -= 1
    else:
        guesses_remaining -= 1
        print(f"That character is not in the word, guesses remaining {guesses_remaining}")

if guesses_remaining > 0:
    print("you won!")
else:
    print("you lost")