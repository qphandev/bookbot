from stats import (count_words, 
                   get_book_text, 
                   count_character_occurences,
                   print_character_occurrences)
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    current_book = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    count_words(current_book)
    print("--------- Character Count -------")
    print_character_occurrences(count_character_occurences(current_book))
    print("============= END ===============")

main()