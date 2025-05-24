from stats import count_words, count_characters, print_report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book")
        sys.exit(1)

    file_contents = get_book_text(sys.argv[1])
    num_words = count_words(file_contents)
    word_dict = count_characters(file_contents.lower()) 
    print_report(word_dict, num_words)

main()
