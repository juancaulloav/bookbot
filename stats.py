def count_words(text):
    words = text.split()
    words = len(words)
    return words

def count_characters(text):
    characters = {}
    text = text.lower()
    for char in text:
        if char.isspace():  # Skip spaces
            continue
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(item):
    return item[1]  # Sort by the count (second element of tuple)
    
def print_characters(characters_list):
    for char, count in characters_list:
        print(f"{char}: {count}")
    print("===================================")

def print_report(characters, words, book_path):
    print("============ BOOKBOT =============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words     ")
    print("----------- Character Count --------")
    characters_list = list(characters.items())
    characters_list.sort(reverse=True, key=sort_on)
    print_characters(characters_list)
    print("============= END ===============")