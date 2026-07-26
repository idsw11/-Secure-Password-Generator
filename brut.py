import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()_+-="

all_chars = letters + digits + symbols

password_length = 14

password = "".join(random.sample(all_chars, password_length))

print("====================================")
print(f"Твой новый надёжный пароль: {password}")
print("====================================")
