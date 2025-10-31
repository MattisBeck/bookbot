from stats import get_word_num, get_character_count, get_list_from_dict
import sys

    #get book text as a long string
def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    #check if all arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    book_contents = get_book_text(path)
    letter_counts = get_character_count(book_contents)    
    sorted_list = get_list_from_dict(letter_counts)
    word_count = get_word_num(book_contents)

    # output
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dictonary in sorted_list:
        if not dictonary[0].isalpha():
            continue
        print(f"{dictonary[0]}: {dictonary[1]}")
    print("============= END ===============")


main()