from database import connect_db

def them_su_kien(title, date, time, description):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO schedules (title, date, time, description) VALUES (?, ?, ?, ?)",
            (title.strip(), date.strip(), time.strip(), description.strip())
        )
        conn.commit()
        print("Thêm lịch trình thành công!")
    except Exception as e:
        print("Lỗi:", e)
    finally:
        conn.close()

def xem_su_kien():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, date, time, description FROM schedules")
    rows = cursor.fetchall()
    conn.close()
    print("\n===== LỊCH TRÌNH CÁ NHÂN =====")
    for r in rows:
        print(f"ID: {r[0]} | Sự kiện: {r[1]} | Ngày: {r[2]} | Giờ: {r[3]} | Mô tả: {r[4]}")