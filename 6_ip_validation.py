def is_valid_IP(strng):
    if len(strng.split(".")) != 4: return False
    for s in strng:
        if not s.isdigit() and s != ".": return False
    for n in strng.split("."):
        if n != str(int(n)) or int(n) < 0 or int(n) > 255: return False
    return True



print(is_valid_IP('12.255.56.1'),     True)
print(is_valid_IP(''),                False)
print(is_valid_IP('abc.def.ghi.jkl'), False)
print(is_valid_IP('123.456.789.0'),   False)
print(is_valid_IP('12.34.56'),        False)
print(is_valid_IP('12.34.56 .1'),     False)
print(is_valid_IP('12.34.56.-1'),     False)
print(is_valid_IP('123.045.067.089'), False)
print(is_valid_IP('127.1.1.0'),        True)
print(is_valid_IP('0.0.0.0'),          True)
print(is_valid_IP('0.34.82.53'),       True)
print(is_valid_IP('192.168.1.300'),   False)