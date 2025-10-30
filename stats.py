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

    #get multiple small dictonaries from one big and return them as a list
def get_list_from_dict(dicto):
    dict_list = []
    items_in_dict = dicto.items()
    for item in items_in_dict:
        small_dict = {}
        small_dict["char"] = item[0]
        small_dict["key"] = item[1]
        dict_list.append(small_dict)
    return dict_list

    #helper function so that sorting works
def sort_on(items):
    return items["key"]

    #Sort list of dictonaries by key (character count)
def sort_list_by_dict_keys(list):
    list.sort(reverse=True, key=sort_on)
    return list