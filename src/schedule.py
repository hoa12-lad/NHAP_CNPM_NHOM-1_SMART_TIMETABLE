from database import connect_db

def them_su_kien(title, date, time, description):
    """Thêm một sự kiện hoặc lịch trình cá nhân mới."""
    if not title.strip() or not date.strip():
        print("Tiêu đề và ngày tháng không được để trống!")
        return
        
    conn = connect_db()
    cursor = conn.cursor()
    try:
        # Đảm bảo bảng schedules tồn tại
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS schedules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                date TEXT NOT NULL,
                time TEXT,
                description TEXT
            )
        """)
        
        cursor.execute(
            """INSERT INTO schedules (title, date, time, description) 
               VALUES (?, ?, ?, ?)""",
            (title.strip(), date.strip(), time.strip(), description.strip())
        )
        conn.commit()
        print("Thêm lịch trình thành công!")
    except Exception as e:
        print("Lỗi khi thêm lịch trình:", e)
    finally:
        conn.close()

def xem_su_kien():
    """Hiển thị toàn bộ danh sách lịch trình cá nhân."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, title, date, time, description FROM schedules ORDER BY date, time")
        schedules = cursor.fetchall()
    except Exception:
        print("Chưa có bảng dữ liệu lịch trình hoặc xảy ra lỗi truy vấn!")
        schedules = []
    finally:
        conn.close()
    
    if not schedules:
        print("Chưa có lịch trình nào trong hệ thống!")
        return
        
    print("\n===== DANH SÁCH LỊCH TRÌNH (SCHEDULE) =====")
    for item in schedules:
        print(f"ID: {item[0]} | Sự kiện: {item[1]} | Ngày: {item[2]} | Giờ: {item[3]} | Mô tả: {item[4]}")