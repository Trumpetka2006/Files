import unicodedata as unc
chartable = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def string_shift(text: str, key: int):
    resolut = ""
    text = unc.normalize("NFKD",text).encode("ascii", "ignore").decode("ascii")
    text = text.upper()
    for char in text:
        position = ord(char) -65
        position += key
        position = position % 26
        resolut += chr(position +65)
    return resolut
    

print(string_shift(input(), 4))
print(string_shift("elsn", -4))