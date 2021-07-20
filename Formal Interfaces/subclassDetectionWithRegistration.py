from abc import ABCMeta


def main():
    print('>>> issubclass(PdfParserNew, FormalParserInterface)')
    print(issubclass(PdfParserNew, FormalParserInterface))
    print('')

    print('>>> issubclass(EmlParserNew, FormalParserInterface)')
    print(issubclass(EmlParserNew, FormalParserInterface))
    print('')


class FormalParserInterface(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text) or
                NotImplemented)


class PdfParserNew:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        ...

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        ...


@FormalParserInterface.register
class EmlParserNew:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        ...

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        ...


if __name__ == '__main__':
    main()
