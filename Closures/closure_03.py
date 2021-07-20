def main() -> None:
    times5 = make_multiplier_of(5)
    print('>>> times5 = make_multiplier_of(5)')
    print('>>> times5(8)')
    times5(8)

    times175 = make_multiplier_of(175)
    print('>>> times175 = make_multiplier_of(175)')
    print('>>> times175(87)')
    times175(87)

    print(times175.__closure__[0].cell_contents)


def make_multiplier_of(n: int):
    # This is the outer enclosing function
    def multiply(x: int) -> None:
        # This is the nested function
        print(x * n)
    return multiply  # returns the nested function


if __name__ == '__main__':
    main()
