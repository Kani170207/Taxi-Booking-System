import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="footballis1710",
        database="taxi_system"
    )

def add_driver(name, phone, license):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO drivers (name, phone, license_number) VALUES (%s, %s, %s)",
        (name, phone, license)
    )
    conn.commit()
    conn.close()

def view_data(table):
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    data = cur.fetchall()
    conn.close()
    return data

def add_vehicle(driver_id, model, plate):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO vehicles (driver_id, model, plate_number) VALUES (%s, %s, %s)",
        (driver_id, model, plate)
    )
    conn.commit()
    conn.close()

def add_ride(driver_id, vehicle_id, pickup, dropoff, fare, status):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO rides (driver_id, vehicle_id, pickup, dropoff, fare, status)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (driver_id, vehicle_id, pickup, dropoff, fare, status))
    conn.commit()
    conn.close()
def delete_driver(driver_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("DELETE FROM drivers WHERE driver_id = %s", (driver_id,))

    conn.commit()
    conn.close()
def login_user(username, password):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT role FROM users WHERE username=%s AND password=%s",
        (username, password)
    )

    result = cur.fetchone()

    conn.close()
    return result    