# estrai una sequenza di numeri e mi fai la media dei numeri primi
import random
import time


# generate random sequence of numbers
def generate_random_numbers(n):
    prime = [5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    random_numbers = []
    for i in range(0, n):
        random_numbers.append(random.randint(0, 100))
    random_numbers.append(random.choice(prime))
    return random_numbers


if __name__ == '__main__':
    cont = 0
    print("I give you a sequence of 15 numbers\n")
    print("Every list has at least one prime number")
    for _ in range(500):
        cont += 1
        # print(cont)
        numeri = generate_random_numbers(14)
        print("Your numbers are:")
        print(numeri)
        # is prime numeri
        prime_numbers = []
        for i in numeri:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_numbers.append(i)
        # time.sleep(0.3)
        # print(prime_numbers)
        media = int(sum(prime_numbers) / len(prime_numbers))
        # print(media)
        print("What is the arithmetic mean of the prime numbers in the list?")
        answer = int(input())
        if answer == media:
            print("Correct!")
        else:
            print("Wrong!")
            print("The correct answer was: ", media)
            exit()

    with open("flag.txt", "r") as f:
        flag = f.read()
        print(flag)
        exit()
