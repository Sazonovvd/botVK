import sqlite3

connect = sqlite3.connect('car.sqlite')
cursor = connect.cursor()

cursor.execute("""
    SELECT cars.number,cars.color,owner,models.mark
    FROM cars,owners,models
    WHERE cars.id_owner=owners.id and cars.id_model=models.id
""")
print(cursor.fetchall())


# cursor.execute("""
#    CREATE table owners (
#        id integer primary key,
#        owner text,
#        driver_car integer
#    );
#    """)
#
# cursor.execute("""
#    CREATE table models (
#        id integer primary key,
#        mark text,
#        model integer,
#        prod_country text
#    );
#    """)
#
# cursor.execute("""
#    CREATE table cars (
#        id integer primary key,
#        number integer,
#        color text,
#        id_owner integer,
#        id_model integer,
#        FOREIGN KEY (id_owner) REFERENCES owners (id),
#        FOREIGN KEY (id_model) REFERENCES models (id)
#    );
#    """)

# cursor.execute("insert into owners values (4,'Игорь','122')")
# cursor.execute("insert into owners values (5,'Виктор','121')")
# cursor.execute("insert into owners values (6,'Андрей','125')")
# cursor.execute("insert into owners values (7,'Андрей','126')")
# cursor.execute("insert into owners values (8,'Ира','124')")
#
# cursor.execute("insert into models values (4,'Chevrolet','Camaro','USA')")
# cursor.execute("insert into models values (5,'Chevrolet','Camaro','USA')")
# cursor.execute("insert into models values (6,'Lexus','RX','Russia')")
# cursor.execute("insert into models values (7,'Lada','Kalina','Polsha')")
# cursor.execute("insert into models values (8,'Daewoo','Matiz','Russia')")
#
# cursor.execute("insert into cars values (4,122,'red',4,4)")
# cursor.execute("insert into cars values (5,121,'white',5,5)")
# cursor.execute("insert into cars values (6,125,'black',6,6)")
# cursor.execute("insert into cars values (7,126,'red',7,7)")
# cursor.execute("insert into cars values (8,124,'white',8,8)")
#
# connect.commit()

cursor.execute("""
    SELECT cars.number,cars.color,owner,models.mark
    FROM cars,owners,models
    WHERE cars.id_owner=owners.id and cars.id_model=models.id and models.mark='Chevrolet'
""")
print(cursor.fetchall())

# cursor.execute("SELECT * FROM models")
# print(cursor.fetchall())
# cursor.execute("SELECT * FROM cars")
# print(cursor.fetchall())

connect.close()
