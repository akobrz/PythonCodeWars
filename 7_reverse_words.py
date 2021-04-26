def reverse_words2(text):
    ret = []
    for w in text.split(' '):
        if len(w) > 0:
            ret.append(w[::-1])
        else:
            ret.append(w)
    return " ".join(ret)

def reverse_words(text):
    return " ".join( [w[::-1] for w in text.split(' ')] )


print(reverse_words('The quick brown fox jumps over the lazy dog.'))
print(reverse_words('double  spaced  words'))
print(reverse_words('apple'))
