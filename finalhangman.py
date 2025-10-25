import random
import time

alphabet = list("abcdefghijklmnopqrstuvwxyz")

penalty = 0
letter_tried = []
word_tried = []

# Load words
with open("words.txt") as file:
    words = file.read().splitlines()

x = random.choice(words)
print(x)
answer = ["_"] * len(x)


def gamebase():
    uinput = input("Choose a letter or guess the full word: ").lower()
    if len(uinput) > 1:
        wordp(uinput)
        word_tried.append(uinput)
    else:
        letterp(uinput)
        letter_tried.append(uinput)


def wordp(n):
    global penalty, answer
    if list(n) == list(x):
        answer = list(x)
    else:
        penalty += 5
        print("Nope! You have", 12 - penalty, "tries left.")


def letterp(n):
    global penalty, answer
    if n in alphabet:
        if n in x:
            for i, y in enumerate(x):
                if y == n:
                    answer[i] = n
            print(" ".join(answer))
        else:
            penalty += 1
            print("Nope! You have", 12 - penalty, "tries left.")
    else:
        penalty += 1
        print("Invalid input! +1 penalty.")


def hangman():
    global penalty, letter_tried, word_tried, answer
    penalty = 0
    letter_tried = []
    word_tried = []
    answer = ["_"] * len(x)

    while "_" in answer:
        print("\nThe word has", len(x), "letters.")
        print("Penalties:", penalty)
        print("Letters tried:", ", ".join(letter_tried))
        print("Words tried:", ", ".join(word_tried))
        print("Current progress:", " ".join(answer))
        gamebase()

        if penalty >= 12:
            print("\nYou lose! The word was:", x)
            break

        if answer == list(x):
            print("\nCongrats! The word was:", x)
            break


def p_score(n):
    try:
        with open("scores.txt", "r+") as f:
            content = f.read().strip()
            b_score = float(content) if content else float("inf")
            if n <= b_score:
                print("New best time!", n, "seconds")
                f.seek(0)
                f.write(str(n))
                f.truncate()
            else:
                print("Best score remains:", b_score)
    except FileNotFoundError:
        with open("scores.txt", "w") as f:
            f.write(str(n))
        print("First score recorded:", n, "seconds")


def p_wanna_p():
    p_input = input("Do you wanna play? (yes/no): ").lower()
    if "yes" in p_input or p_input == "y":
        start = time.time()
        hangman()
        player_time = round((time.time() - start), 2)
        p_score(player_time)
    else:
        print("See ya!")


# Start
p_wanna_p()
