def encrypt(text, value, output=""):
    for char in text:
        output = "{}{}".format(output, chr(ord(char) + value))
    return output

def decrypt(text, value, output=""):
    for char in text:
        output = "{}{}".format(output, chr(ord(char) - value))
    return output

i = int(raw_input("Kac kez sifrelensin: "))

text = raw_input("Sifrelenecek metin: ")
print("Sifreli metin: {}".format(encrypt(text, i)))

text = raw_input("\nDecode edilecek metin: ")
print("Decode edilmis metin: {}".format(decrypt(text, i)))