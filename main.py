def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        text =  f.read()
    f.close()
    return text

def main():
    path = "books/frankenstein.txt"
    print(get_book_text(path))





if __name__ == "__main__":
    main()
