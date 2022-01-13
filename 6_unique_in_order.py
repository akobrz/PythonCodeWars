def unique_in_order(iterable):
    ret = []
    temp = iterable[0]

    for i in range(len(iterable)):
        if i == 0:
            ret.append(iterable[i])
        else:
            if iterable[i] != temp:
                ret.append(iterable[i])
                temp = iterable[i]

    return ret

print(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])
print(unique_in_order('AAĆABbBCcDAąBBb'), ['A','B','C','D','A','B'])
print(unique_in_order([1,2,2,3,3]), [1,2,3])