"""
✔ Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
✔ Возвращается строка в нижнем регистре.
"""
from string import ascii_lowercase
LETTERS = ascii_lowercase + ' '


def symbol_deleter(in_str: str) -> str:
    if not isinstance(in_str, str):
        raise TypeError("Аргумент должен быть строкой")
    return ''.join([letter for letter in in_str.lower() if letter in LETTERS])


def main():
    print(symbol_deleter('This text has to saved. А этот текст должен быть удален 1234098765'
                         '!"№;%%::?? ** (() ()( *  ?: %: %;;!@#$%^&*(*)_+=}{[]|\\/?.,<>`~'))


if __name__ == '__main__':
    main()

"""
import string


def remove_chars(text: str) -> str:
    alpha = string.ascii_letters + ' '
    print(alpha)
    result = text
    for t in text:
        if t not in alpha:
            result = result.replace(t, '')
    return result.lower()


if __name__ == '__main__':
    print(remove_chars('sDDsdsd вывывывывы  выввы1323232'))
"""