import string

def is_pangram(s):
    return sum([(0 if x in str(s).lower() else -1 ) for x in "abcdefghijklmnopqrstuvwxyz"]) == 0

def is_pangram2(s):
    a = "abcdefghijklmnopqrstuwxyz"
    for c in a:
        if not c in s:
            return False
    return True



print(is_pangram("The quick, brown fox jumps over the lazy dog!"), True)
print(is_pangram("The quick, brown fox jumps over the lazy do!"), False)
print(is_pangram("Cwm fjord bank glyphs vext quiz"),True)