import sys

import ft_filter


def filterString(S: str, N: int):
    """
    Filters a given string by removing
    words that contain forbidden characters
    and returning words longer than a specified length.

    Args:
        S (str): The input string to be processed.
        N (int): The minimum length of words to be included in the result.

    Returns:
        list: A list of words from the input string that:
              1. Do not contain any forbidden characters.
              2. Have a length greater than N characters.

    Process:
        1. The input string `S` is split into words based on spaces.
        2. Words that contain forbidden characters
        (punctuation, control characters, etc.)
        are filtered out.
        3. From the remaining words,
        only those that have a length greater than `N` are returned.
    """
    forbidenCracters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~\n\0\f\r\b\t"
    split = S.split(" ")
    filter = ft_filter.ft_filter(
        lambda word: not any(c in forbidenCracters for c in word), split
    )

    return [word for word in filter if len(word) > N]


def main():
    """
    Main function to handle command-line input
    and execute the filterString function.

    Raises:
        AssertionError: If the number of arguments is not 3,
        or if the arguments are of invalid types.
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert (
            not sys.argv[1].isdigit() and sys.argv[2].isdigit()
        ), "the arguments are bad"
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        sys.exit(1)
    print(filterString(sys.argv[1], int(sys.argv[2])))


if __name__ == "__main__":

    main()
