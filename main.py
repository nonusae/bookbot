from stats import *
import sys


def get_book_text(path):
    with open(path, "r") as file:
        return file.read()

REPORT_TEMPLATE = """\
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {word_count} total words
-------- Character Count --------
{char_count_report}
============= END ==============="""

def format_character_count(characters):
    return "\n".join(f"{char}: {count}" for char, count in characters)

def main():
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    num_characters = map_characters_count(text)
    sorted_characters = sort_characters_count_dict(num_characters)
    filtered_characters = list(filter(lambda x: x[0].isalpha(), sorted_characters))
    print(f"{num_words} words found in the document")

    report = REPORT_TEMPLATE.format(
        book_path="books/frankenstein.txt",
        word_count=num_words,
        char_count_report=format_character_count(filtered_characters)
    )
    print(report)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        main()
