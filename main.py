import sys

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_counts(text)
    sort_char_count = chars_dict_to_sorted_list(char_count)
    print_report(book_path, num_words, sort_char_count)

def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, sort_char_count):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for char, count in sort_char_count:
        if char.isalpha:
            print(f"{char}: {count}")
    print(f"============= END ===============")

from stats import get_num_words, get_char_counts, chars_dict_to_sorted_list

main()

