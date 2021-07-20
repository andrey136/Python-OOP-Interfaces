import abc


def main():
    print('>>> issubclass(float, Double)')
    print(issubclass(float, Double))
    print('')

    print('>>> isinstance(1.53453, Double)')
    print(isinstance(1.53453, Double))
    print('')

    print('>>> issubclass(Double64, Double)')
    print(issubclass(Double64, Double))
    print('')


class Double(metaclass=abc.ABCMeta):
    ...


Double.register(float)


@Double.register
class Double64:
    ...


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
