import psycopg2 as psg
import csv



conn = psg.connect(host = "localhost", dbname = "phonebook", user = "postgres", 
                   password = "Nurik_2006", port = 5432)

cur = conn.cursor()

# Create Table
cur.execute(""" CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(50) NOT NULL,
            user_phone VARCHAR(15) NOT NULL
);
""")

# first_name = input()
# number = int(input())

# # inserting data
# cur.execute(
#     "INSERT INTO phonebook (user_name, user_phone) VALUES (%s, %s)",
#     (first_name, number)
# )


# Insert first name and phone by csv file
# with open('text.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     for line in csv_reader:
#         cur.execute(
#             "INSERT INTO users (user_id, user_name, user_phone) VALUES (%s,%s,%s)",
#             (line[0], line[1], line[2])
#         )



# updating data 
# update = int(input("Do you want to update data (1, 0) "))
# if update:
#     field = int(input("Name or number> (1, 0) "))
#     if field:
#         old_name = input("old name:")
#         new_name = input("new name:")
#         cur.execute("UPDATE user SET user_name = %s WHERE user_name = %s", (new_name, old_name))
#     else:
#         old_number = input("old number:")
#         new_number = input("new number:")
#         cur.execute("UPDATE users SET user_phone = %s WHERE user_phone = %s", (new_number, old_number))


# Filters
# filt = int(input("filter by name or phone? (1, 0) "))

# if filt:
#     filter_name = input("filter by name: ")
#     cur.execute("SELECT * FROM users WHERE user_name ILIKE %s", (f"%{filter_name}%"))
# else:
#     filter_phone = input("filter by phone: ")
#     cur.execute("SELECT * FROM users WHERE user_phone = %s", (filter_phone,))
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# # Delete From Table
# delete = int(input("delete name or phone? (1, 0) "))

# if delete:
#     delete_name = input("name to delete: ")
#     cur.execute("DELETE FROM users WHERE user_name = %s", (delete_name,))
# else:
#     delete_phone = input("phone to delete: ")
#     cur.execute("DELETE FROM users WHERE user_phone = %s", (delete_phone,))
conn.commit()

cur.close()
conn.close()