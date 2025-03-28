def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        text =  f.read()
    f.close()
    return text

def main():
    path = "books/frankenstein.txt"
    text = (get_book_text(path))
    num_words = len(text.split())
    print(f'{num_words} words found in the document')





if __name__ == "__main__":
    main()
