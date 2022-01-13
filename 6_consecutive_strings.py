def longest_consec(strarr, k):
    max = 0
    ret = ""

    if k < 1 or len(strarr) < k:
        return ""
    else:
        for i in range(len(strarr)):
            length = 0
            s = ""
            for j in range(i, i + k):
                if j < len(strarr):
                    length += len(strarr[j])
                    s += strarr[j]

            if max < length:
                max = length
                ret = s
    return ret


print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3))