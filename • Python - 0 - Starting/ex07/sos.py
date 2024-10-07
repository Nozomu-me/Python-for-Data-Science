import sys


def is_basic_alpanumeric(s: str) -> bool:
    """
    Checks if a given string contains only basic alphanumeric characters.

    Args:
        s (str): The string to be checked.

    Returns:
        bool: True if the string contains only basic alphanumeric characters,
              False otherwise.
    """
    alph_nums = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return all(letter in alph_nums for letter in s)


def main():
    """
    Convert a given string input to its equivalent Morse code representation.

    The function reads the input string
    from the command line argument, checks that the input contains
    only alphanumeric characters and spaces,
    then converts each character to Morse code using a predefined
    dictionary.
    The Morse code for each character is separated by spaces,
    and spaces in the input are represented
    as '/'. The function will print the resulting Morse code to the console.

    Returns:
    - Prints the Morse code equivalent of the input string to the console.

    """

    morse_code = dict(
        {
            " ": "/",
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "0": "-----",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
        }
    )
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        assert is_basic_alpanumeric(
            sys.argv[1].replace(" ", "").upper()
        ), "the arguments are bad"
    except AssertionError as e:
        print(AssertionError.__name__ + ":", e)
        sys.exit(1)

    argument = sys.argv[1].upper()
    result = ""
    for i, letter in enumerate(argument):
        if i == len(argument) - 1:
            result += morse_code[letter]
            break
        result += morse_code[letter] + " "
    print(result)


if __name__ == "__main__":
    main()
