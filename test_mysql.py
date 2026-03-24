import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="footballis1710",
        database="taxi_system"
    )

    if conn.is_connected():
        print("✅ MySQL Connected Successfully!")

except Exception as e:
    print("❌ Error:", e)