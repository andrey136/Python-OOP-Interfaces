def main() -> None:
    print('>>> ordinary()')
    ordinary()


def make_pretty(func):
    def inner() -> None:
        print('I got decorated')
        func()
    return inner


@make_pretty
def ordinary() -> None:
    print('I am ordinary')


if __name__ == '__main__':
    main()
