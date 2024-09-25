import sys


def analyzer(text: str):
    """
    text: The text to analyze

    Prints the following information:
        . The number of characters in the text
        . The number of upper case letters
        . The number of lower case letters
        . The number of punctuation marks
        . The number of spaces
        . The number of digits

    """
    upperLetters = sum(1 for c in text if c.isupper())
    lowerLetters = sum(1 for c in text if c.islower())
    punctuation_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    punctuations = sum(1 for c in text if c in punctuation_characters)
    spaces = sum(1 for c in text if c.isspace())
    digits = sum(1 for c in text if c.isdigit())

    print(f"The text contains {len(text)} characters:")
    print(f"{upperLetters} upper letters")
    print(f"{lowerLetters} lower letters")
    print(f"{punctuations} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """
    Main entry point. Handles command-line arguments and user input.

    - If no arguments are provided, it prompts
    the user to input text and analyzes it.
    - If exactly one argument is passed,
    it analyzes the provided argument.
    - If more than one argument is provided,
    raises an AssertionError and exits the program.

    Workflow:
    1. Prompts for input if no command-line arguments are given.
    2. Raises an AssertionError if more than one argument is provided.
    3. Analyzes the text provided via input or argument.

    """

    if len(sys.argv) == 1:
        text = input("What is the text to count?\n")
        print(text)
        analyzer(text)
        sys.exit(1)
    try:
        assert len(sys.argv) == 2, "more than one argument is provided"
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        sys.exit(1)
    argument = sys.argv[1]
    analyzer(argument)


if __name__ == "__main__":
    main()
