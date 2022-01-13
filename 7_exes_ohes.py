def xo(s):
    s = s.lower()
    if s.count("x") == s.count("o"):
        return True
    return False


print(xo("zpzpzpp"))