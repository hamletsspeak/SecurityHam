import random
import math

# Определение алфавита
alphabet = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Заглавные буквы
    "abcdefghijklmnopqrstuvwxyz"  # Строчные буквы
    "0123456789"                  # Цифры
    "!\"#$%&'"                    # Специальные символы
)

# Функция для генерации случайного пароля
def generate_password(length, alphabet):
    return ''.join(random.choice(alphabet) for _ in range(length))

# Функция для расчета минимальной длины пароля
def calculate_min_password_length(P, V, T, A=69):
    minutes_in_day = 1440  # Количество минут в дне
    denominator = V * T * minutes_in_day  # знаменатель
    S_star = math.log2((P / denominator) ** -1)  # вычисляем S*
    L = math.ceil(S_star / math.log2(A))  # вычисляем минимальную длину пароля
    return S_star, L

# Основная функция программы
def main():
    # Ввод данных
    P = float(input("Введите вероятность успешной атаки (P): "))
    V = float(input("Введите скорость подбора паролей (V паролей/мин): "))
    T = float(input("Введите время защиты пароля (T дней): "))

    # Расчет минимальной длины пароля
    S_star, L = calculate_min_password_length(P, V, T)

    # Генерация пароля
    password = generate_password(L, alphabet)
    
    # Вывод результатов
    print(f"\nНижняя граница энтропии пароля (S*): {S_star:.2f} бита")
    print(f"Минимальная длина пароля: {L} символов")
    print(f"Сгенерированный пароль: {password}")

# Запуск программы
main()