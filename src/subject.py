from database import connect_db

def them_mon_hoc(name, credits):
    """Thêm môn học mới vào cơ sở dữ liệu."""
    if not name.strip():
        print("Tên môn học không được để trống!")
        return
    if credits <= 0:
        print("Số tín chỉ phải lớn hơn 0!")
        return
        
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO subjects (name, credits) VALUES (?, ?)",
        (name.strip(), credits)
    )
    conn.commit()
    conn.close()
    print("Thêm môn học thành công!")

def xem_mon_hoc():
    """Hiển thị danh sách môn học."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, name, credits FROM subjects ORDER BY id"
    )
    subjects = cursor.fetchall()
    conn.close()
    
    if not subjects:
        print("Chưa có môn học nào!")
        return
        
    print("\n===== DANH SÁCH MÔN HỌC =====")
    for subject in subjects:
        print(
            f"ID: {subject[0]} | "
            f"Tên: {subject[1]} | "
            f"Tín chỉ: {subject[2]}"
        )

def sua_mon_hoc(subject_id, name, credits):
    """Cập nhật thông tin môn học."""
    if not name.strip():
        print("Tên môn học không được để trống!")
        return
    if credits <= 0:
        print("Số tín chỉ phải lớn hơn 0!")
        return
        
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE subjects
        SET name = ?, credits = ?
        WHERE id = ?
        """,
        (name.strip(), credits, subject_id)
    )
    conn.commit()
    if cursor.rowcount == 0:
        print("Không tìm thấy môn học!")
    else:
        print("Cập nhật môn học thành công!")
    conn.close()

def xoa_mon_hoc(subject_id):
    """Xóa môn học theo ID."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM subjects WHERE id = ?", (subject_id,))
    conn.commit()
    if cursor.rowcount == 0:
        print("Không tìm thấy môn học để xóa!")
    else:
        print("Xóa môn học thành công!")
    conn.close()

def them_lop(class_name):
    """Thêm lớp học mới."""
    if not class_name.strip():
        print("Tên lớp học không được để trống!")
        return
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO classes (class_name) VALUES (?)", (class_name.strip(),))
    conn.commit()
    conn.close()
    print("Thêm lớp học thành công!")

def xem_lop():
    """Hiển thị danh sách lớp học."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, class_name FROM classes ORDER BY id")
    classes = cursor.fetchall()
    conn.close()
    
    if not classes:
        print("Chưa có lớp học nào!")
        return
        
    print("\n===== DANH SÁCH LỚP HỌC =====")
    for c in classes:
        print(f"ID: {c[0]} | Tên lớp: {c[1]}")