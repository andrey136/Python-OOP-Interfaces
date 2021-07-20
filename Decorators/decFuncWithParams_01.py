def main() -> None:
    print('>>> divide(3, 2)')
    print(divide(3, 2))
    print('>>> divide(3, 0)')
    print(divide(3, 0))


def smart_divide(func):
    def inner(a, b):
        print(f"I'm going to divide {a} and {b}")
        if b == 0:
            return 'You can\'t divide by 0'
        else:
            return func(a, b)
    return inner


@smart_divide
def divide(a: int, b: int) -> float:
    return a / b


if __name__ == '__main__':
    main()
