def main():
    say_hello('John')


def star(func):
    def inner(*args, **kwargs):
        print('*' * 30)
        func(*args, **kwargs)
        print('*' * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print('%' * 30)
        func(*args, **kwargs)
        print('%' * 30)
    return inner

@percent
@star
def say_hello(name: str) -> None:
    print(f'Hello {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
