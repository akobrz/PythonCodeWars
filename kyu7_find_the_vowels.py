def vowel_indices(word):
    return [i for i, v in enumerate(word,1) if v in "aeouiyAEOUIY"]

print(vowel_indices("mmm"), [], "failed on the word 'mmm'")
print(vowel_indices("apple"), [1,5], "failed on the word 'apple'")
print(vowel_indices("123456"), [], "failed on the word '123456'")
print(vowel_indices("UNDISARMED"), [1,4,6,9], "failed on the word 'UNDISARMED'. Consider case")
print(vowel_indices("9D54308lERj3i4pIzqB2VvEez77MkkqCCIZ9uZFcsocKntcnVJOAVDj0iJu3h"), [9, 13, 16, 23, 24, 34, 37, 42, 51, 52, 57, 59], "")