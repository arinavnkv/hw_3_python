sentence = input('sentence: ')

def capitalize(word):
    if len(word) == 0:
        return word

    return chr(ord(word[0]) - 32) + word[1:]

def capitalize_sentence(sentence):
    words = sentence.split()
    capitalized_words = [capitalize(word) for word in words]
    return ' '.join(capitalized_words)

print(capitalize_sentence(sentence))