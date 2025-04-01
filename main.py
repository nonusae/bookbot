def get_book_text(path):
    with open(path, "r") as file:
        return file.read()

def count_words(text):
    return len(text.split())

def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = count_words(text)

    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()
