def duplicate_count(text):
    return sum([text.lower().count(c) > 1 for c in set(text.lower())])

print(duplicate_count("Indivisibilities"), 2)
print(duplicate_count("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"), 26)
