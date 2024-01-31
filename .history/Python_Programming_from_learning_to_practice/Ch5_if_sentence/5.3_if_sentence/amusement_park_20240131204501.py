# 向哲煜 2024.1.31

#if-elif-else sentence

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $50.")

# 改进

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 50

print(f"Your admission")