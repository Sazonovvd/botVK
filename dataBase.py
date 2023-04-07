import sqlite3


def init_db():
    connect = sqlite3.connect('database.sqlite')
    cursor = connect.cursor()
    cursor.execute("""
    CREATE table phrases (
        id integer primary key,
        phrase text,
        answer text
    );
    """)
    connect.close()


def insert_db(phrase, answer):
    connect = sqlite3.connect('database.sqlite')
    cursor = connect.cursor()
    cursor.execute("SELECT id FROM phrases")
    new_id = str(cursor.fetchall()[-1][0] + 1)

    # cursor.execute("insert into phrases values (1, 'Hello', 'И тебе Hello')")
    # cursor.execute("insert into phrases values (2, 'Привет', 'И тебе привет')")
    # cursor.execute("insert into phrases values (3, 'How are u?', 'Better then u')")
    # cursor.execute("insert into phrases values (4, 'Как дела?', 'Лучше чем у тебя')")
    # cursor.execute("insert into phrases values (5, 'Сколько времяни?', 'Меня не для этого создовали!')")
    # cursor.execute("insert into phrases values (6, 'What`s the time?', 'I whon`t answer on this question')")
    # cursor.execute("insert into phrases values (7, 'Morning!', 'И тебе Hello')")
    # cursor.execute("insert into phrases values (8, 'Evening!', 'И тебе Hello')")
    # cursor.execute("insert into phrases values (9, 'Night!', 'И тебе Hello')")
    # cursor.execute("insert into phrases values (10, 'Утро!', 'И тебе Hello')")
    # cursor.execute("insert into phrases values (11, 'Вечер!', 'И тебе Hello')")
    # cursor.execute("insert into phrases values (12, 'Ночь!', 'И тебе Hello')")

    cursor.execute("insert into phrases values (" + new_id + ", '" + phrase + "', '" + answer + "')")

    connect.commit()
    connect.close()


def get_db():
    connect = sqlite3.connect('database.sqlite')
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM phrases")
    result = cursor.fetchall()
    print(result)
    connect.close()
    return result


###########
# cursor.execute("insert into friends values (1, 'Виктор', 8912932154)")
# cursor.execute("insert into friends values (2, 'Тиктор', 8943932154)")
# cursor.execute("insert into friends values (3, 'Никтор', 8939132154)")
# cursor.execute("insert into friends values (4, 'Киктор', 8943212154)")
# cursor.execute("insert into friends values (5, 'Циктор', 8999532154)")
# cursor.execute("insert into friends values (6, 'Фиктор', 8923132154)")
#
# cursor.execute("insert into cars values (1, 'Тик_тор', 'Red', 932154)")
# cursor.execute("insert into cars values (2, 'Цик_тор', 'Black', 891293)")
# cursor.execute("insert into cars values (3, 'Фик_тор', 'White', 932121)")
# cursor.execute("insert into cars values (4, 'Вик_тор', 'Blue',892154)")
# cursor.execute("insert into cars values (5, 'Мик_тор', 'Nightlight-red',891354)")
# cursor.execute("insert into cars values (6, 'Гик_тор', 'Dark-red',895154)")
####
# cursor.execute("SELECT * FROM friends")

# cursor.execute("insert into groups1 values (1, 'friends')")
# cursor.execute("insert into groups1 values (2, 'classmates')")
# cursor.execute("insert into groups1 values (3, 'programmers')")

# connect.close()
