def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)

    print("BOOK REPORT")
    print("------------")
    print(" ")
    print(word_count)
    print(" ")
    for c in character_count:
        print(f"The letter '{c[0]}' is used {c[1]} times")


def get_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.lower().split()

    return f"This book has {len(words)} words."


def get_character_count(text):
    text_characters = list(text.lower())

    counts = {}

    for c in text_characters:
        if c.isalpha():
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_counts


main()
