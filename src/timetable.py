# timetable.py

import database

def them_lich_hoc(ma_mon, ma_giang_vien, ma_phong, ngay_trong_tuan, tiet_bat_dau, tiet_ket_thuc):
    """
    Thêm một lịch học mới vào hệ thống.
    """
    sql = """
        INSERT INTO Schedules (CourseID, TeacherID, RoomID, NgayTrongTuan, TietBatDau, TietKetThuc)
        VALUES (?, ?, ?, ?, ?, ?)
    """
    tham_so = (ma_mon, ma_giang_vien, ma_phong, ngay_trong_tuan, tiet_bat_dau, tiet_ket_thuc)
    
    thanh_cong = database.execute_query(sql, tham_so)
    if thanh_cong:
        print("Đã thêm lịch học thành công!")
    else:
        print("Lỗi: Không thể thêm lịch học.")
    return thanh_cong

def sua_lich_hoc(ma_lich, ma_mon, ma_giang_vien, ma_phong, ngay_trong_tuan, tiet_bat_dau, tiet_ket_thuc):
    """
    Cập nhật thông tin của một lịch học đã tồn tại.
    """
    sql = """
        UPDATE Schedules 
        SET CourseID = ?, TeacherID = ?, RoomID = ?, NgayTrongTuan = ?, TietBatDau = ?, TietKetThuc = ?
        WHERE ScheduleID = ?
    """
    tham_so = (ma_mon, ma_giang_vien, ma_phong, ngay_trong_tuan, tiet_bat_dau, tiet_ket_thuc, ma_lich)
    
    thanh_cong = database.execute_query(sql, tham_so)
    if thanh_cong:
        print(f"Đã cập nhật thành công lịch học mã {ma_lich}!")
    else:
        print(f"Lỗi: Không thể cập nhật lịch học mã {ma_lich}.")
    return thanh_cong

def xoa_lich_hoc(ma_lich):
    """
    Xóa lịch học khỏi hệ thống dựa trên mã lịch.
    """
    sql = "DELETE FROM Schedules WHERE ScheduleID = ?"
    tham_so = (ma_lich,)
    
    thanh_cong = database.execute_query(sql, tham_so)
    if thanh_cong:
        print(f"Đã xóa lịch học mã {ma_lich}.")
    else:
        print(f"Lỗi: Không thể xóa lịch học mã {ma_lich}.")
    return thanh_cong