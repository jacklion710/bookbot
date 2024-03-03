def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    
    sorted_chars = sorted(chars_dict.items(), key=lambda item: item[1], reverse=True)
    
    print_report(book_path, num_words, sorted_chars)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    text = text.lower()  
    for c in text:
        if c.isalpha():  
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, sorted_chars):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

main()