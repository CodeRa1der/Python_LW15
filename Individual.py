#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# "Словарь" для преобразования русских букв в английские
def vocabulary():
    return {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
            'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
            'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
            'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}

def replace_chars(chars="?!:;,. "):
    def wrapper(func):
        result = ''
        for char in func:
            if char.lower() in vocabulary():
                result += vocabulary()[char.lower()]
            else:
                result += char
        for char in chars:
            result = result.replace(char, '-')
        # Удаление последовательных дефисов, замена на одиночные
        while '--' in result:
            result = result.replace('--', '-')
        return result
    return wrapper

if __name__ == "__main__":
    input_text = input("Введите строку на кириллице: ")
    processed_text = replace_chars()(input_text.lower())  # Низкий регистр, чтобы исключить ошибки, связанные с регистром
    print("Результат:", processed_text)
