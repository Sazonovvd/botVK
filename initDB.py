import sqlite3

connect = sqlite3.connect('database.sqlite')
cursor = connect.cursor()

cursor.execute("""
CREATE table groups1 (
    id integer primary key autoincrement,
    group_name text,
);
""")

cursor.execute("""
CREATE table user (
    id integer primary key,
    chat_id integer,
    id_group integer,
    FOREIGN KEY (id_group) PREFERENCES groups1 (id)
);
""")



# cursor.execute("""
# CREATE table friends (
#     id integer primary key,
#     name text,
#     phone_number integer
# );
# """)

# cursor.execute("""
# CREATE table cars (
#     id integer primary key,
#     mark text,
#     color text,
#     number integer
# );
# """)

# cursor.execute("""
# CREATE table phrases (
#     id integer primary key,
#     phrase text,
#     answer text
# );
# """)

connect.close()
