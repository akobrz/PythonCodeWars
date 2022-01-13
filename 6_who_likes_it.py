def likes(names):
    d={
        0:"no one likes this",
        1:"{} likes this",
        2:"{} and {} like this",
        3:"{}, {} and {} like this",
        4:"{}, {} and {others} others like this"
    }
    return d[min(4, len(names))].format(*names, others=len(names[2:]))

print(likes([]), 'no one likes this')
print(likes(['Peter']), 'Peter likes this')
print(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
print(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
print(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')