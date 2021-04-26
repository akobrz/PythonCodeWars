def longest_repetition(chars):
    ret, last = "", ""

    for i in range(len(chars)):
        if chars[i] not in last: last = chars[i]
        else: last += chars[i]

        if len(ret) < len(last): ret = last

    return ret[0] if len(ret) > 0 else '',len(ret) if len(ret) > 0 else 0

print(longest_repetition("bbbdddaaacccbaaabbb"),('a',4))
print(longest_repetition(""),('',0))