def main() -> None:
    global ordinary
    print('>>> ordinary()')
    ordinary()

    print('\n>>> pretty = make_pretty(ordinary)')
    pretty = make_pretty(ordinary)
    print('>>> pretty()')
    pretty()

    print('\n>>> ordinary = make_pretty(ordinary)')
    ordinary = make_pretty(ordinary)
    print('>>> ordinary()')
    ordinary()



def make_pretty(func):
    def inner():
        print('I got decorated')
        func()
    return inner


def ordinary():
    print('I am ordinary')


if __name__ == '__main__':
    main()
