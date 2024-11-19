from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import os

#генерируем ключи и сохраняем в файлы
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    with open("private_key.pem", "wb") as priv_file:
        priv_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    with open("public_key.pem", "wb") as pub_file:
        pub_file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

    print("Ключи успешно сгенерированы и сохранены в файлы private_key.pem и public_key.pem.")

#зашифровывем по открытому ключу и сохраняем в новый файл
def encrypt_file(file_path, public_key_path):
    with open(public_key_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())

    with open(file_path, "rb") as f:
        data = f.read()

    encrypted_data = public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    encrypted_file_path = f"{file_path}.encrypted"
    with open(encrypted_file_path, "wb") as f:
        f.write(encrypted_data)

    print(f"Файл успешно зашифрован и сохранен как {encrypted_file_path}.")

#расшифровываем по закрытому ключу и записываем в новый файл
def decrypt_file(encrypted_file_path, private_key_path):
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None)

    with open(encrypted_file_path, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    decrypted_file_path = encrypted_file_path.replace(".encrypted", ".decrypted")
    with open(decrypted_file_path, "wb") as f:
        f.write(decrypted_data)

    print(f"Файл успешно расшифрован и сохранен как {decrypted_file_path}.")


def main():
    print("RSA File Encryption/Decryption Tool")
    print("1. Сгенерировать ключи")
    print("2. Зашифровать файл")
    print("3. Расшифровать файл")
    print("4. Выйти")

    while True:
        choice = input("Выберите действие: ")

        if choice == "1":
            generate_keys()
        elif choice == "2":
            file_path = input("Введите путь к файлу для шифрования: ")
            public_key_path = input("Введите путь к открытому ключу (public_key.pem): ")
            if os.path.exists(file_path) and os.path.exists(public_key_path):
                encrypt_file(file_path, public_key_path)
            else:
                print("Указанный файл или ключ не найден.")
        elif choice == "3":
            encrypted_file_path = input("Введите путь к зашифрованному файлу: ")
            private_key_path = input("Введите путь к закрытому ключу (private_key.pem): ")
            if os.path.exists(encrypted_file_path) and os.path.exists(private_key_path):
                decrypt_file(encrypted_file_path, private_key_path)
            else:
                print("Указанный файл или ключ не найден.")
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
