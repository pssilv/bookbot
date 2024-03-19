def main():
    num_words = get_num_words()
    num_chars = get_chars()
    print(f"{"START":=^50}")
    print(f"WORD COUNTER:\n{num_words} words has been found in the document\nCHARS SORT:")
    sorted_chars = chars_dict_to_sorted_list(num_chars)
    for dict in sorted_chars:
        num = dict["num"]
        char = dict["char"]
        print(f"the {char} character was found {num} times")

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

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        if char.isalpha():
            sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()