import random

def main():
    x = 0
    y = 10

    print('Getting random integer between {0} and {1}'.format(x, y))
    print(get_random_int(x, y))
    

def get_random_int(x, y):
    return random.randint(x, y)


if __name__ == "__main__":
    main()
