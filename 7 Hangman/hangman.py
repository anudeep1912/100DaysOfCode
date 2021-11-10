import random
import hangman_art
import hangman_words


def generate_random_word():
    word = random.choice(hangman_words.word_list)
    print("A random word has been generated try to guess it!")
    return word


def generate_display_word(display_word):
    result = []
    for i in range(len(display_word)):
        result.append("_")
    return result


print(hangman_art.logo)
random_word = generate_random_word()
print(random_word)
result_word = generate_display_word(random_word)
lives = 6
while "_" in result_word:
    guess = input("Guess a letter: ").lower()
    if guess in result_word:
        print("You have already guessed this word. Please try again.")
        continue
    if guess not in random_word:
        lives -= 1

    for i in range(len(random_word)):
        if random_word[i] == guess:
            result_word[i] = guess
    print(result_word)
    print(hangman_art.stages[lives])
    if "".join(result_word) == random_word:
        print(f"You WIN! The word is {random_word}")
    elif lives == 0:
        print(f"You Have Exhausted all your chances. You Lose. The actual word is {random_word.capitalize()}")
        break


