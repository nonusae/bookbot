from stats import get_num_words, map_characters_count


def get_book_text(path):
    with open(path, "r") as file:
        return file.read()

def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(text)
    num_characters = map_characters_count(text)
    print(f"{num_words} words found in the document")
    print(num_characters)

if __name__ == "__main__":
    main()
