# 🚖 Taxi Booking System

A full-stack Taxi Booking System built using **Python, Streamlit, and MySQL**.
This application allows administrators to manage drivers, vehicles, and rides, while users can book rides through a simple interface.

---

## 🌟 Features

### 🔐 Authentication

* Admin Login
* User Login
* Role-based access control

### 👨‍✈️ Driver Management

* Add drivers
* View driver details
* Delete drivers

### 🚗 Vehicle Management

* Assign vehicles to drivers
* View vehicle list

### 🚕 Ride Management

* Book rides
* Track ride history
* View ride details

### 📊 Dashboard

* Clean UI with dark theme
* Data tables for all entities
* Real-time database updates

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Database:** MySQL
* **Libraries:** pandas, mysql-connector-python

---

## 📂 Project Structure

```
taxi_booking_system/
│
├── app.py
├── functions.py
├── database.py
├── requirements.txt
├── test_mysql.py
│
├── pages/
│   ├── 0_Login.py
│   ├── 1_Admin_Dashboard.py
│   ├── 2_Manage_Drivers.py
│   ├── 3_Manage_Vehicles.py
│   ├── 4_Manage_Rides.py
│   └── 5_Book_Ride.py
│
└── .streamlit/
    └── config.toml
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/taxi-booking-system.git
cd taxi-booking-system
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Setup MySQL Database

Create database:

```
CREATE DATABASE taxi_system;
```

Create tables:

```
CREATE TABLE drivers (
    driver_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    phone VARCHAR(20),
    license_number VARCHAR(50)
);

CREATE TABLE vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    driver_id INT,
    model VARCHAR(50),
    plate_number VARCHAR(50)
);

CREATE TABLE rides (
    ride_id INT AUTO_INCREMENT PRIMARY KEY,
    driver_id INT,
    vehicle_id INT,
    pickup VARCHAR(100),
    dropoff VARCHAR(100),
    fare FLOAT,
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(100),
    role VARCHAR(20)
);
```

Insert sample users:

```
INSERT INTO users (username, password, role)
VALUES 
('admin', 'admin123', 'admin'),
('user', 'user123', 'user');
```

---

### 5️⃣ Configure Database Connection

Update `functions.py`:

```
host="localhost"
user="root"
password="yourpassword"
database="taxi_system"
```

---

### 6️⃣ Run the App

```
streamlit run app.py
```

---

## 🎯 Usage

* Login as **Admin** → Manage drivers, vehicles, rides
* Login as **User** → Book rides
* View real-time updates from MySQL database

---

## 🚀 Future Enhancements

* 🔒 Password hashing (security)
* 📍 Live location tracking (Maps API)
* 📊 Analytics dashboard with charts
* 🌐 Cloud deployment with MySQL hosting
* 📱 Mobile-friendly UI

---

## 👨‍💻 Author

Kanish V
