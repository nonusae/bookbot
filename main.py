def get_book_text(path):
    with open(path, "r") as file:
        return file.read()

def main():
    print(get_book_text("./books/frankenstein.txt"))

if __name__ == "__main__":
    main()
