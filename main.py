import sys
from stats import count_words, count_characters, print_report

def get_book_text(book_path):
    with open(book_path) as f:
        book_text = f.read()
        return book_text    

    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    characters = count_characters(book_text)    
    words = count_words(book_text)
    return print_report(characters, words, book_path)

main()