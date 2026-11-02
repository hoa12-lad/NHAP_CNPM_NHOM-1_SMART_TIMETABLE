import sqlite3

def connect_db():
    """Tạo kết nối đến cơ sở dữ liệu SQLite."""
    conn = sqlite3.connect("smart_timetable.db")
    return conn

def init_db():
    """Khởi tạo các bảng dữ liệu cần thiết cho hệ thống."""
    conn = connect_db()
    cursor = conn.cursor()
    
    # Tạo bảng subjects (Môn học)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            credits INTEGER NOT NULL
        )
    """)
    
    # Tạo bảng classes (Lớp học)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS classes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            class_name TEXT NOT NULL
        )
    """)

    # Tạo bảng accounts (Tài khoản)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()
    print("Khởi tạo cơ sở dữ liệu thành công!")

if __name__ == "__main__":
    init_db()