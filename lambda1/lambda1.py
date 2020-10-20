def main():
    x = 1

    print("Incrementing {0}".format(x))
    print(inc(x))

    print("Decrementing {0}".format(x))
    print(dec(x))


def inc(x):
    return x + 1


def dec(x):
    return x - 1


if __name__ == "__main__":
    main()
