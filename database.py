import sqlite3

conn = sqlite3.connect("taxi.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS drivers (
    driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    license_number TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehicles (
    vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
    driver_id INTEGER,
    model TEXT,
    plate_number TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS rides (
    ride_id INTEGER PRIMARY KEY AUTOINCREMENT,
    driver_id INTEGER,
    vehicle_id INTEGER,
    pickup TEXT,
    dropoff TEXT,
    fare REAL,
    status TEXT
)
""")

conn.commit()
conn.close()