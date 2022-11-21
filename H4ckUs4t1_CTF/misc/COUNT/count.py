import random


# random letter
def random_letter():
    letter = ""
    letter_list = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    letter = random.choice(letter_list)
    return letter


def word_generator():
    word = ""
    with open("wordlist.txt", "r") as f:
        word_list = f.readlines()
        word = random.choice(word_list)
        word = word.strip()
    return word


if __name__ == "__main__":

    print(
        "Welcome in H4ckus4t1 CTF 2022",
        "You have to write the occurency of a letter in a word",
        "Example : How many a in gelato?",
        "1",
        sep="\n",
    )
    print("Let's start!")

    for i in range(500):
        word = word_generator()
        letter = random_letter()
        print("How many", letter, "in", word, "?")
        answer = input()
        if answer == str(word.count(letter)):
            print("Correct!")
        else:
            print("Wrong!")
            print("the correct answer was", word.count(letter))
            exit()
    print("Congratulations, your flag!")
    # read from flag.txt
    with open("flag.txt", "r") as f:
        flag = f.read()
        print(flag)
        exit()
