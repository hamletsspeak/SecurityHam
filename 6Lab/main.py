import random



# Таблица символов
char_table = {chr(i + 1039): i for i in range(1, 33)}
char_table[' '] = 0  # Пробел
char_table['Ё'] = 33  # Добавим "Ё" для полноты
reverse_table = {v: k for k, v in char_table.items()}

# Преобразование текста в числовой формат
def text_to_numbers(text):
    return [char_table[char] for char in text.upper() if char in char_table]

# Преобразование чисел обратно в текст
def numbers_to_text(numbers):
    return ''.join(reverse_table[num] for num in numbers)

# Генерация гаммы
def generate_gamma(length, seed=48):
    random.seed(seed)
    return [random.randint(0, 33) for _ in range(length)]

# Шифрование методом гаммирования
def encrypt_gamma(text, gamma):
    text_numbers = text_to_numbers(text)
    encrypted_numbers = [(text_numbers[i] + gamma[i]) % 34 for i in range(len(text_numbers))]
    return encrypted_numbers

# Расшифровка методом гаммирования
def decrypt_gamma(encrypted_numbers, gamma):
    decrypted_numbers = [(encrypted_numbers[i] - gamma[i]) % 34 for i in range(len(encrypted_numbers))]
    return numbers_to_text(decrypted_numbers)

# Функция для чтения текста из файла
def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Функция для записи текста в файл
def write_text_to_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

# Функция для шифрования с записью в файл
def encrypt_file(input_file, output_file, gamma_seed):
    text = read_text_from_file(input_file)
    print("Исходный текст:", text)

    text_numbers = text_to_numbers(text)
    gamma = generate_gamma(len(text_numbers), seed=gamma_seed)
    encrypted_numbers = encrypt_gamma(text, gamma)

    # Сохраняем зашифрованный текст (числа) в файл
    write_text_to_file(output_file, ' '.join(map(str, encrypted_numbers)))
    print("Зашифрованный текст сохранен в файл:", output_file)

    # Сохраняем гамму для расшифровки
    write_text_to_file("gamma.txt", ' '.join(map(str, gamma)))

# Функция для расшифровки с записью в файл
def decrypt_file(input_file, output_file, gamma_file):
    encrypted_numbers = list(map(int, read_text_from_file(input_file).split()))
    gamma = list(map(int, read_text_from_file(gamma_file).split()))

    decrypted_text = decrypt_gamma(encrypted_numbers, gamma)
    write_text_to_file(output_file, decrypted_text)
    print("Расшифрованный текст сохранен в файл:", output_file)

# Основной код
if __name__ == "__main__":
    # Шифрование
    encrypt_file("input_text.txt", "encrypted_text.txt", gamma_seed=123)
    
    # Расшифровка
    decrypt_file("encrypted_text.txt", "decrypted_text.txt", "gamma.txt")
