def encrypt(locale, n, base_str):
    if locale == "ru":
        upp = 1071
        low = 1103
        length = 32
    else:
        upp = 90
        low = 122
        length = 26
    encoded_str = ""
    for char in base_str:
        if char.isupper():
            char = ord(char) + n
            if char > upp:
                encoded_str += chr(char - length)
            else:
                encoded_str += chr(char)
        elif char.islower():
            char = ord(char) + n
            if char > low:
                encoded_str += chr(char - length)
            else:
                encoded_str += chr(char)
        else:
            encoded_str += (char)
    return encoded_str


def decrypt(locale, n, base_str):
    if locale == "ru":
        upps, uppe = 1040, 1071
        lows, lowe = 1072, 1103
        length = 32
    else:
        upps, uppe = 65, 90
        lows, lowe = 97, 122
        length = 26
    decoded_str = ""
    for char in base_str:
        if char.isupper():
            char = ord(char) - n
            if char < upps:
                decoded_str += chr(char + length)
            elif char > uppe:
                decoded_str += chr(char - length)
            else:
                decoded_str += chr(char)
        elif char.islower():
            char = ord(char) - n
            if char < lows:
                decoded_str += chr(char + length)
            elif char > lowe:
                decoded_str += chr(char - length)
            else:
                decoded_str += chr(char)
        else:
            decoded_str += (char)
    return decoded_str

print("Конвертер для шифрования/дешифрования любого текста, используя шифр Цезаря.")

type_op = input("Выберите операцию: Зашифровать(EC)/Расшифровать(DC) \n").lower()
lang = input("Выберите алфавит: RU/EN \n").lower()
rot = int(input("Укажите сдвиг(1 - 32): "))
orig_str = input("Введите текст: \n")

if type_op == "ec":
    print("Зашифрованный текст:", encrypt(lang, rot, orig_str), sep="\n")
elif type_op == "dc":
    print("Расшифрованный текст:", decrypt(lang, rot, orig_str), sep="\n")
