import uuid
import psutil
import hashlib
import os

def get_mac_address():
    mac = uuid.getnode()
    mac_str = ':'.join([f'{(mac >> elements) & 0xff:02x}' for elements in range(0, 2 * 6, 2)][::-1])
    return mac_str

def get_cpu_frequency():
    freq = psutil.cpu_freq()
    return freq.current if freq else 0

def generate_machine_id():
    mac_address = get_mac_address()
    cpu_frequency = get_cpu_frequency()
    
    # Создаем строку из характеристик
    machine_id = f"{mac_address}-{cpu_frequency}"
    
    # Хэшируем для получения уникального идентификатора
    return hashlib.sha256(machine_id.encode()).hexdigest()

def check_machine_id(stored_id):
    current_id = generate_machine_id()
    if current_id != stored_id:
        print("Эта программа может быть запущена на этом компьютере.")
        return False
    return True

if __name__ == "__main__":
    # Предположим, что у вас уже есть сохраненный идентификатор
    # В реальной программе этот идентификатор должен быть где-то сохранен
    stored_id = "ваш_идентификатор_машины_здесь"  # Замените на ваш сохраненный идентификатор

    if check_machine_id(stored_id):
        print("Эта может быть программа запущена на авторизованном компьютере.")
        # Ваш код здесь
    else:
        print("Доступ разрешён.")
