import psycopg2 as psg

""""
CREATE OR REPLACE FUNCTION searchpattern(pattern VARCHAR)
RETURNS TABLE(user_id int, user_name VARCHAR, user_phone VARCHAR) AS
$$
BEGIN
    RETURN QUERY
    SELECT users.user_id, users.user_name, users.user_phone
    FROM users
    WHERE users.user_name ILIKE '%' || pattern || '%'
    OR users.user_phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE insert_element(name VARCHAR, new_phone VARCHAR) AS
$$
BEGIN
    UPDATE users SET user_phone = new_phone WHERE user_name = name;
    IF NOT FOUND THEN
        INSERT INTO users (user_name, user_phone)
        VALUES (name, new_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE insert_lst(name VARCHAR, phone VARCHAR) AS
$$
BEGIN 
    INSERT INTO users (user_name, user_phone)
        VALUES (name, phone);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION querys(a INT, b INT)
RETURNS TABLE(user_id int, user_name VARCHAR, user_phone VARCHAR) AS
$$
BEGIN
    RETURN QUERY
    SELECT users.user_id, users.user_name, users.user_phone
    FROM users
    ORDER BY users.user_id
    LIMIT a OFFSET b;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE PROCEDURE delete_by(name VARCHAR, userphone VARCHAR) AS
$$
BEGIN 
    DELETE FROM users
    WHERE user_name = name;

    IF NOT FOUND THEN
        DELETE FROM users
        WHERE users.user_phone = userphone;
    END IF;
END;
$$ LANGUAGE plpgsql;
"""


conn = psg.connect(
    host="localhost",
    dbname="phonebook",
    user="postgres",
    password="Nurik_2006",
    port="5432"
)
conn.autocommit = True
cur = conn.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(50) NOT NULL,
            user_phone VARCHAR(15) NOT NULL
);
""")

#1 search function
# def search(pattern):
#     cur.callproc('searchpattern', (pattern,))
#     res = cur.fetchall()
#     for row in res:
#         print(row)

# search("Nursultan")


#2 inserting
# def insert(name, new_phone):
#     cur.execute("CALL insert_element(%s, %s)", (name, new_phone,))

# insert('NBA_player', '1234097532')

#3 inserting from list with loop
# lst = [
#     ["AfroAmerican", "+1234567890"],
#     ["SpotlessIndian", "+23582323457"],
#     ["GayActivist", "+2347867834"]
# ]

# for user in lst:
#     cur.execute("CALL insert_lst(%s, %s)", (user[0], user[1]))


#4 Quering by limit and offset

# def pagin(limit, offset):
#     cur.callproc('querys', (limit, offset))
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)

# pagin(2, 4)


#5 deleting from table
def delete(name = None, phone = None):
    cur.execute("CALL delete_by(%s, %s)", (name, phone))

delete(phone=" 77773465905")

