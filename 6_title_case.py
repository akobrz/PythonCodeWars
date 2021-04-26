def title_case(title, minor_words=''):
    ret = ""
    for i, w in enumerate(title.lower().split(" ")):
        if i == 0:
            ret = w.capitalize()
        else:
            found = False
            for m in minor_words.lower().split(" "):
                if w == m:
                    found = True
                    break
            if found:
                ret += " " + w
            else:
                ret += " " + w.capitalize()
    return ret


print(title_case(''), '')
print(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')
print(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')
print(title_case('the quick brown fox'), 'The Quick Brown Fox')
print(title_case('First a of in', 'an often into'), 'First A Of In')