
def name(x):
    if x > str(3):
        print("Hello" + " " + x + " " + "How are you")
    else:
        print("none")


if __name__ == '__main__':
    x = input("Enter your Name : ")
    name(x)
