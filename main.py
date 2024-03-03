def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)

def word_count():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = (f.read()).split()
        count = len(file_contents)
        print(count)


word_count()