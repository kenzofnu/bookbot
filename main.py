from stats import (
    count_words,
    count_characters,
    sort_dict      
)
import sys

def main():

    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

    text = get_book_text(sys.argv[1])
    count = count_words(text)
    dict = count_characters(text)
    sorted_dic = sort_dict(dict)

    print_report(count,sorted_dic)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def print_report(count,sorted_dic):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")

    print("--------- Character Count -------")
    for key in sorted_dic:
        if key["name"].isalpha():
            print(f"{key["name"]}: {key["num"]}")


main()
