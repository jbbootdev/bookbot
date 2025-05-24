
def count_words(book_text):
    return len(book_text.split())

def count_characters(book_text):
    return {char: book_text.count(char) for char in set(book_text)}

    
def sort_dict_by_value(dictionary):
    """
    Sorts a dictionary by its values in descending order (highest to lowest)

    Args:
        dictionary (dict): The input dictionary

    Returns:
        dict: A new dictionary with the same keys as the original, but sorted by value
    """
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

def print_report(word_dictionary, word_count):
    sorted_words = sort_dict_by_value(word_dictionary)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for key, value in sorted_words.items():
        if key.isalpha():
            print(f"{key}: {value}")
  
