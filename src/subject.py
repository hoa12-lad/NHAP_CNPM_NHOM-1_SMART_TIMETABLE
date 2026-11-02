
# Danh sách lưu trữ môn học
danh_sach_mon_hoc = []


# 1. Thêm môn học
def them_mon_hoc():
    print("\n--- THEM MON HOC ---")
    ma_mon = input("Nhap ma mon hoc: ").strip()

    for mon in danh_sach_mon_hoc:
        if mon["ma_mon"] == ma_mon:
            print("Ma mon hoc da ton tai!")
            return

    ten_mon = input("Nhap ten mon hoc: ")
    so_tin_chi = int(input("Nhap so tin chi: "))

    mon_hoc = {
        "ma_mon": ma_mon,
        "ten_mon": ten_mon,
        "so_tin_chi": so_tin_chi
    }

    danh_sach_mon_hoc.append(mon_hoc)
    print("Them mon hoc thanh cong!")


# 2. Sửa môn học
def sua_mon_hoc():
    print("\n--- SUA MON HOC ---")
    ma_mon = input("Nhap ma mon hoc can sua: ").strip()

    for mon in danh_sach_mon_hoc:
        if mon["ma_mon"] == ma_mon:
            mon["ten_mon"] = input("Nhap ten mon hoc moi: ")
            mon["so_tin_chi"] = int(input("Nhap so tin chi moi: "))
            print("Sua mon hoc thanh cong!")
            return

    print("Khong tim thay mon hoc!")


# 3. Xóa môn học
def xoa_mon_hoc():
    print("\n--- XOA MON HOC ---")
    ma_mon = input("Nhap ma mon hoc can xoa: ").strip()

    for mon in danh_sach_mon_hoc:
        if mon["ma_mon"] == ma_mon:
            danh_sach_mon_hoc.remove(mon)
            print("Xoa mon hoc thanh cong!")
            return

    print("Khong tim thay mon hoc!")


# 4. Hiển thị môn học
def hien_thi_mon_hoc():
    print("\n--- DANH SACH MON HOC ---")

    if len(danh_sach_mon_hoc) == 0:
        print("Danh sach mon hoc rong!")
        return

    for mon in danh_sach_mon_hoc:
        print("Ma mon:", mon["ma_mon"])
        print("Ten mon:", mon["ten_mon"])
        print("So tin chi:", mon["so_tin_chi"])
        print("--------------------")
