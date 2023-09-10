def decode(encoded_str):
    charset = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    padd = "="

    while encoded_str and encoded_str[-1] == padd:
        encoded_str = encoded_str[:-1]

    binstr = ""
    for char in encoded_str:
        if char in charset:
            dec = charset.index(char)
            binstr += format(dec, "05b")

    padding = len(binstr) % 8
    if padding != 0:
        binstr = binstr[:-padding]

    decoded_bytes = bytearray()
    for i in range(0, len(binstr), 8):
        byte = int(binstr[i:i + 8], 2)
        decoded_bytes.append(byte)

    return bytes(decoded_bytes)


encoded_str = '''*&(&)<+$*"$%+?_?:.,[;[+~+{](+`#%,|![{[*;.]^@}@,>'.:@)_"<+.:?+`>$'"#$#`=((|};=='''
decoded_data = decode(encoded_str)
print(decoded_data)
