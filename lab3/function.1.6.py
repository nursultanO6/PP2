def rev(sentence : str) -> str:
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence
uinput = input()
print(rev(uinput))