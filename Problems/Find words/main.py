input_sentence = input()


def find_words(sentence):
    words = sentence.split()
    found_words = []
    for word in words:
        last_letter = word[-1]
        if last_letter == 's':
            found_words.append(word)
    return "_".join(found_words)


print(find_words(input_sentence))
