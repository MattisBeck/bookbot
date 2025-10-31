def get_word_num(text):
    word_list = text.split()
    return len(word_list)

    #returns one big, unsorted dictonary with character and count pairs
def get_character_count(text):
    text = text.lower()
    character_count = {}
    for character in text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

    #get multiple small tuples from one big and return the sorted ones
def get_list_from_dict(dicto):
    items_in_dict = list(dicto.items())
    print(items_in_dict)
    items_in_dict.sort(reverse=True, key=sort_on)
    return items_in_dict

    #helper function so that sorting works
def sort_on(items):
    return items[1]