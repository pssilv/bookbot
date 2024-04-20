def main():
    num_words = get_num_words()
    num_chars = get_chars()
    num_letters = get_letters()
    longest_word = get_longest_word()
    print(f"{"START":=^50}")
    print(f"WORD COUNTER:\n{num_words} words has been found in the document")
    print(f"CHAR COUNTER:\n{num_letters} chars has been found in the document")
    print(f"LONGEST WORD: {longest_word}\nMOST COMMON CHARS:")
    sorted_chars = get_sorted(num_chars)
    for dict in sorted_chars:
        char = dict["char"]
        num = dict["num"]
        print(f"{char} was found {num} times")
    print(f"{"END":=^50}")

def get_book_text():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        return f.read()

def get_num_words():
    text = get_book_text()
    words = text.split()
    return len(words)



def get_chars():
    chars = {}
    text = get_book_text()
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def get_sorted(dict):
    sorted_list = []
    for key in dict:
        if key.isalpha():
            sorted_list.append({"char": key, "num": dict[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_letters():
    total_letters = 0
    text = get_book_text()
    for letter in text:
        total_letters += 1
    return total_letters

def get_longest_word():
    text = get_book_text()
    words = text.split()
    longest_word = ""
    longest_word_counter = 0
    for word in words:
        if len(longest_word) < len(word):
            longest_word = word
    for word in words:
        if longest_word.lower() == word.lower():
            longest_word_counter += 1
    return longest_word, f"The longest word appeareared: {longest_word_counter} time(s)"

def search_word(*search_string):
    text = get_book_text()
    words = text.split()
    string_counter = {}

    for pos in search_string:
        string_counter[pos.lower()] = 0

    for key in string_counter:
        for word in words:
            if key == word.lower():
                string_counter[key] += 1

    return f"searched word dict: {string_counter}"

main()
