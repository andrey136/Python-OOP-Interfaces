def main() -> None:
    print('>>> new()')
    new()


def is_called():
    def is_returned():
        print("Hello")
    return is_returned


new = is_called()

if __name__ == '__main__':
    main()
