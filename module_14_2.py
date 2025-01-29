import sqlite3

# # Создание базы данных и подключения к ней
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
# Создание таблицы Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(10):
    cursor.execute("INSERT INTO Users(username,email,age,balance) VALUES (?,?,?,?)",
                   (f"User{i + 1}", f"example{i + 1}@gmail.com", f"{(i + 1) * 10}", "1000"))
# Обновление balance
cursor.execute("UPDATE Users SET balance = ? WHERE id%2 != ?", (500, 0))
# ▎Удаление записей
cursor.execute("DELETE FROM Users WHERE id % 3 = 1")
# Выборка записей
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))

users = cursor.fetchall()

for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст:{user[2]} | Баланс: {user[3]}")

# #Удаление из базы данных not_telegram.db запись с id = 6
cursor.execute("SELECT * FROM Users WHERE id = ?", (6,))
user = cursor.fetchone()
if user:
    print("Найден пользователь для удаления:", user)
    cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
    print(f"Удалено строк: {cursor.rowcount}")
else:
    print("Пользователь с id = 6 не найден.")

# Подсчет общего количества записей
cursor.execute("SELECT COUNT(*) FROM Users")
total1=cursor.fetchone()[0]
print(f"Общее количество записей: {total1}")

# Подсчет суммы всех балансов
cursor.execute("SELECT SUM (balance) FROM Users ")
total2=cursor.fetchone()[0]
print(f"Сумма всех балансов:{total2}")

# Подсчет среднего баланса пользователей
cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance=cursor.fetchone()[0]
print(f"Средний баланс пользователей:{avg_balance}")

# Закрытие соединения
connection.commit()
connection.close()