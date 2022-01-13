def spin_words(sentence):
    return " ".join([b if len(b) < 5 else b[::-1] for b in sentence.split()])

print(spin_words("This is another test"), "This is rehtona test")
print(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")