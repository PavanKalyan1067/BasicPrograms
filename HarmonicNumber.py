# Harmonic Number
def harmonic_sum(n):
    """

    :param n:
    :return:
    """
    if n < 2:
        return 1
    else:
        return 1 / n + (harmonic_sum(n - 1))


if __name__ == '__main__':
    print(harmonic_sum(int(input("Enter the nth Number :"))))
