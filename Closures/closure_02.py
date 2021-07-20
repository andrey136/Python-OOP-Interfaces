def main() -> None:
    print('>>> another()')
    another()


def print_msg(msg):
    # This is the outer enclosing function

    def printer() -> None:
        # This is the nested function
        print(msg)

    return printer  # returns the nested function


another = print_msg("Hello")

if __name__ == '__main__':
    main()
