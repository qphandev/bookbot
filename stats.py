def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

def count_words(file_contents):
    word_list = file_contents.split()
    num_words = len(word_list)
    print(f"Found {num_words} total words")

def count_character_occurences(file_contents):
    letter_dictionary = {}
    for i, letter in enumerate(file_contents):
        lowercase_letter = letter.lower()

        if lowercase_letter == " ":
            continue
        if lowercase_letter in letter_dictionary:
            letter_dictionary[lowercase_letter] += 1
        else:
            letter_dictionary[lowercase_letter] = 1
    return letter_dictionary

def sort_on(dict):
    return dict["num"]

def print_character_occurrences(char_occ_dict):
    char_occ_list = [] # should be in form of {"char": "b", "num": num}

    # traverse dictionary and add to list
    for item in char_occ_dict:
        occurence = char_occ_dict[item]
        char_occ_list.append({"char": item, "num": occurence})

    # sort list from highest occurence to smallest
    char_occ_list.sort(reverse=True, key=sort_on)

    # print list format
    for item in char_occ_list:
        print(f"{item["char"]}: {item["num"]}")