def decrypt(encrypted_text, n):
    if encrypted_text == None: return encrypted_text

    a, l = encrypted_text, int(len(encrypted_text) / 2)

    while n > 0:
        b = ""
        for i in range(0, l):
            b += a[i + l] + a[i]
        if len(a) % 2 != 0:
            b += a[-1]
        a = b
        n -= 1

    return a

def encrypt(text, n):
    a = text
    while n > 0:
        b = ""
        for i in range(1, len(a),2):
            b += a[i:i+1]
        for i in range(0, len(a),2):
            b += a[i:i+1]
        a = b
        n -= 1
    return a

print(decrypt("hsi  etTi sats!",1),"?")
# print(decrypt("n;[-+$y7`", 299), "?")

print(encrypt("This is a test!", -1), "This is a test!")
print(encrypt("This is a test!", 0), "This is a test!")
print(encrypt("This is a test!", 1), "hsi  etTi sats!")
print(encrypt("This is a test!", 2), "s eT ashi tist!")
print(encrypt("This is a test!", 3), " Tah itse sits!")
print(encrypt("This is a test!", 4), "This is a test!")
# print(encrypt("This kata is very interesting!", 0), "This kata is very interesting!")
# print(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")
# print(encrypt("This kata is very interesting!", 2), "stsrnenT a ytsghk v et!iaieiri")
# print(encrypt("This kata is very interesting!", 3), "treTaysh  tiiiissnn  tgkve!aer")
# print(encrypt("This kata is very interesting!", 4), "rTyh iisn tkearteas tiisn gv!e")
# print(encrypt("This kata is very interesting!", 5), "This kata is very interesting!")
# print("**********************")
# print(decrypt("This is a test!", -1), "This is a test!")
# print(decrypt("This is a test!", 0), "This is a test!")
# print(decrypt("hsi  etTi sats!", 1), "This is a test!")
# print(decrypt("s eT ashi tist!", 2), "This is a test!")
# print(decrypt(" Tah itse sits!", 3), "This is a test!")
# print(decrypt("This is a test!", 4), "This is a test!")



# print(decrypt("This kata is very interesting!", 0), "This kata is very interesting!")
# print(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")
# print(decrypt("stsrnenT a ytsghk v et!iaieiri", 2), "This kata is very interesting!")
# print(decrypt("treTaysh  tiiiissnn  tgkve!aer", 3), "This kata is very interesting!")
# print(decrypt("rTyh iisn tkearteas tiisn gv!e", 4), "This kata is very interesting!")
# print(decrypt("This kata is very interesting!", 5), "This kata is very interesting!")


# print(decrypt("This is a test!", 0), "This is a test!")
# print(decrypt("hsi  etTi sats!", 1), "This is a test!")
# print(decrypt("s eT ashi tist!", 2), "This is a test!")
# print(decrypt(" Tah itse sits!", 3), "This is a test!")
# print(decrypt("This is a test!", 4), "This is a test!")
# print(decrypt("This is a test!", -1), "This is a test!")
# print(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")

# print(encrypt("", 0), "")
# print(decrypt("", 0), "")
# print(encrypt(None, 0), None)
# print(decrypt(None, 0), None)
