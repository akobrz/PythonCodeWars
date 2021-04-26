def to_weird_case(string):
    b = []
    for w in string.split(" "):
        nw = ""
        for i, c in enumerate(w):
            if i%2 == 0:
                nw += c.upper()
            else:
                nw += c.lower()
        b.append(nw)

    return " ".join(b)

print(to_weird_case('This is a test'))