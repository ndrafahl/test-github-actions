def main():
    x = 6
    y = 2

    print("Multiplying {0} by {1}".format(x, y))
    print(mul(x, y))

    print("Dividing {0} by {1}".format(x, y))
    print(div(x, y))


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def not_used_function():
    return True


if __name__ == "__main__":
    main()
