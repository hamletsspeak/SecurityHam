import getpass  # Импортируем модуль для скрытого ввода ключа

#Шифрование перестановкой заключается в том, что символы открытого 
#текста переставляются по определенному правилу в пределах некоторого блока этого текста.


# Функция для шифрования текста с помощью перестановки
def encrypt_permutation(text, key):
    key_length = len(key)  # Длина ключа
    # Создаем список строк, количество строк равно длине ключа
    columns = ["" for _ in range(key_length)]
    
    # Заполняем таблицу перестановки: каждую букву вставляем в соответствующую колонку
    for i, char in enumerate(text):
        columns[i % key_length] += char
    
    # Собираем зашифрованный текст, используя сортировку индексов ключа
    encrypted_text = ""
    for index in sorted(range(key_length), key=lambda x: key[x]):
        encrypted_text += columns[index]  # Собираем текст по переставленным колонкам
    
    return encrypted_text  # Возвращаем зашифрованный текст

# Функция для расшифровки текста с помощью перестановки
def decrypt_permutation(text, key):
    key_length = len(key)  # Длина ключа
    nrows = len(text) // key_length  # Количество строк в таблице
    remainder = len(text) % key_length  # Остаток символов, если текст не делится ровно
    
    # Создаем список строк (колонок), чтобы распределить текст по ним
    columns = ["" for _ in range(key_length)]
    index = 0  # Индекс для чтения текста
    
    # Заполняем колонки символами, учитывая, что некоторые могут быть длиннее на 1 символ
    for i in sorted(range(key_length), key=lambda x: key[x]):
        col_length = nrows + (1 if i < remainder else 0)  # Длина каждой колонки
        columns[i] = text[index:index+col_length]  # Заполняем колонку
        index += col_length  # Сдвигаем индекс
    
    # Собираем исходный текст, перебирая символы по колонкам
    decrypted_text = ""
    for i in range(nrows + 1):  # Проходим по строкам
        for j in range(key_length):  # Проходим по колонкам
            if i < len(columns[j]):  # Если колонка не пустая, добавляем символ
                decrypted_text += columns[j][i]
    
    return decrypted_text  # Возвращаем расшифрованный текст

# Функция для шифрования текста из файла
def encrypt_file_permutation(input_file, output_file, key):
    # Открываем файл для чтения и убираем символы новой строки
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read().replace('\n', '')
    encrypted_text = encrypt_permutation(text, key)  # Шифруем текст
    # Записываем зашифрованный текст в новый файл
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(encrypted_text)

# Функция для расшифровки текста из файла
def decrypt_file_permutation(input_file, key):
    # Открываем файл для чтения зашифрованного текста
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    decrypted_text = decrypt_permutation(text, key)  # Расшифровываем текст
    print("Расшифрованный текст:", decrypted_text)  # Выводим расшифрованный текст на экран

# Основная функция для выбора режима
def main_permutation():
    mode = input("Выберите режим (1 - шифрование, 2 - расшифровка): ")  # Запрашиваем режим работы
    if mode == '1':  # Режим шифрования
        text = input("Введите текст для шифрования: ")  # Ввод текста
        key = getpass.getpass("Введите ключ для шифрования (без отображения): ")  # Ввод ключа без отображения
        encrypted_text = encrypt_permutation(text, key)  # Шифруем текст
        # Записываем зашифрованный текст в файл
        with open('перестановкашифр.txt', 'w', encoding='utf-8') as f:
            f.write(encrypted_text)
        print("Зашифрованный текст записан в файл 'перестановкашифр.txt'.")  # Сообщаем о результате
    elif mode == '2':  # Режим расшифровки
        input_file = input("Введите имя файла для расшифровки: ")  # Запрашиваем имя файла
        key = getpass.getpass("Введите ключ для расшифровки (без отображения): ")  # Вводим ключ
        decrypt_file_permutation(input_file, key)  # Расшифровываем текст из файла

# Вызов основной функции
main_permutation()
