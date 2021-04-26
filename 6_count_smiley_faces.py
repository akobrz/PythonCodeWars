def count_smileys(arr):
    counter = 0

    for a in arr:
        if (":" in a or ";" in a) and ( ")" in a or "D" in a):
            if len(a)==2 or len(a)==3 and ("-" in a or "~" in a):
                counter += 1

    return counter



print(count_smileys([]), 0)
print(count_smileys([':D',':~)',';~D',':)']), 4)
print(count_smileys([':)',':(',':D',':O',':;']), 2)
print(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)
print(count_smileys([':D', ';-(', ';oD', ':-D', ':D', ':-(', ':-D', ';o(', ':-D', ':-D', ';D', ':D', ';-(', ';(']), 8)