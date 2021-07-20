import abc


def main():
    print('>>> issubclass(PdfParserNew, FormalParserInterface)')
    print(issubclass(PdfParserNew, FormalParserInterface))
    print('')

    print('>>> issubclass(EmlParserNew, FormalParserInterface)')
    print(issubclass(EmlParserNew, FormalParserInterface))
    print('')

    print('>>> PdfParserNew.__mro__:')
    print(PdfParserNew.__mro__)
    print('')

    print('>>> EmlParserNew.__mro__:')
    print(EmlParserNew.__mro__)
    print('')


class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text))


class PdfParserNew:
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass


class EmlParserNew:
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
