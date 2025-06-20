from stats import count_words, count_characters, print_report

def get_book_text(book_path):
    with open(book_path) as f:
        book_path = f.read()
        return book_path

    
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    characters = count_characters(book_text)    
    words = count_words(book_text)
    return print_report(characters, words, book_path)

main()