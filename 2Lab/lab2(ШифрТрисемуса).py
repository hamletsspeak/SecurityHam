import getpass

#В таблицу сначала вписывалось по строкам ключевое слово, причем повторяющиеся буквы отбрасывались.\
#Затем эта таблица дополнялась не вошедшими в нее буквами алфавита по порядку.
#Поскольку ключевое слово или фразу легко хранить в памяти, то такой подход упрощал 
#процессы шифрования и расшифрования.



# Создание матрицы Трисемуса на основе ключа
def create_trithemius_square(key):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    # Убираем повторяющиеся символы из ключа
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))
    # Создаем таблицу на основе ключа и алфавита
    square = []
    used_letters = set()
    for char in key + alphabet:
        if char not in used_letters:
            square.append(char)
            used_letters.add(char)
    return square

# Поиск символа в матрице
def find_position(square, char):
    size = len(square)
    index = square.index(char)
    return index // 6, index % 6  # координаты строки и столбца

# Функция для шифрования текста с помощью шифра Трисемуса
def encrypt_trithemius(text, square):
    encrypted_text = ""
    for char in text:
        if char in square:
            row, col = find_position(square, char)
            encrypted_text += square[(row * 6 + (col + 1) % 6) % len(square)]
        else:
            encrypted_text += char  # если символ не в алфавите, оставляем его
    return encrypted_text

# Функция для расшифровки текста с помощью шифра Трисемуса
def decrypt_trithemius(text, square):
    decrypted_text = ""
    for char in text:
        if char in square:
            row, col = find_position(square, char)
            decrypted_text += square[(row * 6 + (col - 1) % 6) % len(square)]
        else:
            decrypted_text += char
    return decrypted_text

# Функции для работы с файлами
def encrypt_file_trithemius(input_file, output_file, key):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read().replace('\n', '')
    square = create_trithemius_square(key)
    encrypted_text = encrypt_trithemius(text, square)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(encrypted_text)

def decrypt_file_trithemius(input_file, key):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    square = create_trithemius_square(key)
    decrypted_text = decrypt_trithemius(text, square)
    print("Расшифрованный текст:", decrypted_text)

# Основная логика
def main_trithemius():
    mode = input("Выберите режим (1 - шифрование, 2 - расшифровка): ")
    if mode == '1':
        text = input("Введите текст для шифрования: ")
        key = getpass.getpass("Введите ключ для шифрования (без отображения): ")
        square = create_trithemius_square(key)
        encrypted_text = encrypt_trithemius(text, square)
        with open('ТрисемусШифр.txt', 'w', encoding='utf-8') as f:
            f.write(encrypted_text)
        print("Зашифрованный текст записан в файл 'ТрисемусШифр.txt'.")
    elif mode == '2':
        input_file = input("Введите имя файла для расшифровки: ")
        key = getpass.getpass("Введите ключ для расшифровки (без отображения): ")
        decrypt_file_trithemius(input_file, key)

# Вызов программы
main_trithemius()
