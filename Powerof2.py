def power(numbers):
    """

    :param numbers: Entering a number to get power
    :return:
    """
    print(pow(numbers, 2))
    for num in range(10):  # Taking range to get power
        print(num ** 2)


if __name__ == '__main__':
    numbers = int(input("Enter a number to get power: "))
    power(numbers)
