def duplicate_encode(word):
    return "".join('(' if word.lower().count(x) == 1 else ')' for x in word)

print(duplicate_encode("din"),"(((")
print(duplicate_encode("recede"),"()()()")
print(duplicate_encode("Success"),")())())","should ignore case")
print(duplicate_encode("(( @"),"))((")