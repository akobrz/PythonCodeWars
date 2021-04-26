def namelist(names):
    l = len(names)
    if l == 0:
        return ''
    if l == 1:
        return names[0]['name']
    if l == 2:
        return names[0]['name'] + ' & ' + names[1]['name']
    return ', '.join([x['name'] for x in names[0:(l-1)]]) + ' & ' + names[l-1]['name']