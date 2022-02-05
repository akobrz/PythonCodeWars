
def ordered_count(inp):
    return [c for c in zip({x:inp.count(x) for x in inp}.keys(), {x:inp.count(x) for x in inp}.values())]

tests = (
    ('abracadabra', [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]),
    ('Code Wars', [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)])
)

for t in tests:
    inp, exp = t
    print(ordered_count(inp))