if __name__ == '__main__':
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = len(file_contents.split())
    lower_case = file_contents.lower()
    letter_count = {}
    for word in lower_case.split():
        for letter in word:
            if letter.isalpha():
                if letter not in letter_count:
                    letter_count[letter] = 1
                else:
                    letter_count[letter] += 1

    sorted_dict = dict(sorted(letter_count.items()))
    print("-----------------")
    print("Begin Book Report")
    print(" of Frankenstein ")
    print("-----------------")
    print(f"Words in book: {words}")
    print("--Letter count--")
    for letter, count in sorted_dict.items():
        print(f"{letter}: {count}")
    print("-----------------")
    print("---END OF BOOK---")
    print("-----------------")