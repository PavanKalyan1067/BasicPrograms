# Flip Coin using Function
import random


def flipcoin():
    result = random.randrange(2)
    if result == 0:
        print("Heads")
    else:
        print("Tails")


if __name__ == "__main__":
    for x in range(6):
        flipcoin()
