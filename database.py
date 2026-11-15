import psycopg

connection = psycopg.connect(
    dbname="chargeconnect",
    user="postgres",
    password="jungkook",
    host="localhost",
    port="5432"
)

print("Database connected successfully!")

connection.execute("""
    CREATE TABLE IF NOT EXISTS drivers (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        phone VARCHAR(15),
        vehicle VARCHAR(50)
    )
""")

connection.commit()

print("Drivers table created successfully!")

connection.close()