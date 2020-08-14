def split_words(sentence):
    return sentence.split(" ")

def camel_case(sentence):
    words = split_words(sentence)
    new_word = words.pop(0).lower()
    for word in words:
        new_word += word.capitalize()
    return new_word
