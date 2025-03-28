from stats import get_num_words, character_count


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        text =  f.read()
    f.close()
    return text

def main():
    path = "books/frankenstein.txt"
    text = (get_book_text(path))
    num_words = get_num_words(text)
    print(f'{num_words} words found in the document')
    print(character_count(text))





if __name__ == "__main__":
    main()
