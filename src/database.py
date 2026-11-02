import sqlite3

def init_db():
    # Kết nối đến cơ sở dữ liệu (tự động tạo file smart_timetable.db nếu chưa có)
    conn = sqlite3.connect("smart_timetable.db")
    cursor = conn.cursor()
    
    # 1. Bảng tài khoản (phục vụ cho account.py)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    
    # 2. Bảng môn học và lớp học (phục vụ cho subject.py)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_name TEXT NOT NULL,
            class_name TEXT NOT NULL
        )
    """)
    
    # 3. Bảng thời khóa biểu (phục vụ cho timetable.py và schedule.py)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS timetables (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id INTEGER,
            day_of_week TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL,
            room TEXT NOT NULL,
            FOREIGN KEY (subject_id) REFERENCES subjects (id)
        )
    """)
    
    conn.commit()
    conn.close()
    print("Khởi tạo cơ sở dữ liệu SQLite thành công!")

if __name__ == "__main__":
    init_db()