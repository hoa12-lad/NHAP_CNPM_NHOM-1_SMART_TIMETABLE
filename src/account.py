from database import connect_db

def dang_ky_tai_khoan(username, password):
    """Đăng ký tài khoản mới."""
    if not username.strip() or not password.strip():
        print("Tên đăng nhập và mật khẩu không được để trống!")
        return
        
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO accounts (username, password) VALUES (?, ?)",
            (username.strip(), password.strip())
        )
        conn.commit()
        print("Đăng ký tài khoản thành công!")
    except Exception as e:
        print("Tên đăng nhập đã tồn tại hoặc có lỗi xảy ra:", e)
    finally:
        conn.close()

def xem_danh_sach_tai_khoan():
    """Hiển thị danh sách tài khoản."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username FROM accounts ORDER BY id")
    accounts = cursor.fetchall()
    conn.close()
    
    if not accounts:
        print("Chưa có tài khoản nào!")
        return
        
    print("\n===== DANH SÁCH TÀI KHOẢN =====")
    for acc in accounts:
        print(f"ID: {acc[0]} | Username: {acc[1]}")

def xoa_tai_khoan(account_id):
    """Xóa tài khoản theo ID."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM accounts WHERE id = ?", (account_id,))
    conn.commit()
    if cursor.rowcount == 0:
        print("Không tìm thấy tài khoản để xóa!")
    else:
        print("Xóa tài khoản thành công!")
    conn.close()
