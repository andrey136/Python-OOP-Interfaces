def main() -> None:
    print('>>> multiply(4, 5)')
    print(multiply(4, 5))
    # print('>>> ()')


def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner


@works_for_all
def multiply(a, b):
    return a * b


if __name__ == '__main__':
    main()
