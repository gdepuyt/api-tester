class Formater:

    def __init__(self):
        pass

    @staticmethod
    def format_number(number: int, length: int = 3) -> str:
        """
        Formats a number with a specified number of zeros.

        Args:
            number (int): The number to format.
            length (int): The number of zeros to use (default: 3).

        Returns:
            str: The number formatted with zeros.
        """
        return f"{number:0{length}d}"
