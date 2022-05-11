def leapYear(x):
    return x % 400 == 0 or (x % 4 == 0 and x % 100 != 0)


if __name__ == "__main__":
    print(leapYear(int(input("Enter The Year : "))))

