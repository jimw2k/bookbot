def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    word_count = count_words(text)
    print(word_count)
    letter_dict = count_letters(text)
    print(letter_dict)
    report(book_path, word_count,letter_dict)


def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    chars = {}
    for c in text:
        l = c.lower()
        if l in chars:
            chars[l] += 1
        else:
            chars[l] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def report(book, words, dict):
    print(f"---- Begin report of {book} ----")
    print(f"{words} words found in the document\n")
    
    lst = []
    for d in dict:
        if d.isalpha():
            lst.append({"char": d, "num":dict[d]})
    lst.sort(reverse=True, key=sort_on)
    for s in lst:
        print(f"The '{s["char"]}' character was found {s["num"]} times.")
    print("---- END Report ----")



    



def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()

