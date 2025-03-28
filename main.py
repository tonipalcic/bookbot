from stats import get_num_words, character_count


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        text =  f.read()
    f.close()
    return text

def main():
    path = "books/frankenstein.txt"
    text = (get_book_text(path))
    word_count = get_num_words(text)
    char_dict = character_count(text)
    
    print_string = f'''============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------\n'''
    
    sorted_chars = dict(sorted(((k, v) for k, v in char_dict.items() if k.isalnum()), key=lambda x: x[1], reverse=True))

    for key, value in sorted_chars.items():
        print_string += f"{key}: {value}\n"

    print_string += "============= END ==============="

    print(print_string)





if __name__ == "__main__":
    main()
