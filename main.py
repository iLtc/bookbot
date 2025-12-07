import sys

from stats import get_num_words, get_num_characters, get_sorted_characters


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    text = get_book_text(path)

    num_words = get_num_words(text)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    num_characters = get_num_characters(text)
    sorted_characters = get_sorted_characters(num_characters)

    print("--------- Character Count -------")

    for char, count in sorted_characters:
        if not char.isalpha():
            continue

        print(f"{char}: {count}")


if __name__ == "__main__":
    main()
