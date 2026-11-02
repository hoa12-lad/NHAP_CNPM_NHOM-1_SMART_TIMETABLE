
import sqlite3
import hashlib
import os

DATABASE_NAME = "thoi_khoa_bieu.db"

# Tai khoan dang dang nhap
tai_khoan_hien_tai = None


# KET NOI CO SO DU LIEU
def ket_noi_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tai_khoan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_dang_nhap TEXT UNIQUE NOT NULL,
            mat_khau TEXT NOT NULL,
            salt TEXT NOT NULL
        )
    """)

    conn.commit()
    return conn


# MA HOA MAT KHAU
def ma_hoa_mat_khau(mat_khau, salt):
    return hashlib.pbkdf2_hmac(
        "sha256",
        mat_khau.encode("utf-8"),
        salt.encode("utf-8"),
        100000
    ).hex()


# 1. DANG KY TAI KHOAN
def dang_ky():
    print("\n========== DANG KY TAI KHOAN ==========")

    ten_dang_nhap = input("Nhap ten dang nhap: ").strip()
    mat_khau = input("Nhap mat khau: ").strip()
    xac_nhan = input("Nhap lai mat khau: ").strip()

    if not ten_dang_nhap or not mat_khau:
        print("Khong duoc de trong thong tin!")
        return

    if mat_khau != xac_nhan:
        print("Mat khau khong khop!")
        return

    conn = ket_noi_database()
    cursor = conn.cursor()

    try:
        salt = os.urandom(16).hex()
        mat_khau_ma_hoa = ma_hoa_mat_khau(mat_khau, salt)

        cursor.execute("""
            INSERT INTO tai_khoan
            (ten_dang_nhap, mat_khau, salt)
            VALUES (?, ?, ?)
        """, (ten_dang_nhap, mat_khau_ma_hoa, salt))

        conn.commit()
        print("DANG KY THANH CONG!")

    except sqlite3.IntegrityError:
        print("Ten dang nhap da ton tai!")

    finally:
        conn.close()


# 2. DANG NHAP TAI KHOAN
def dang_nhap():
    global tai_khoan_hien_tai

    print("\n========== DANG NHAP ==========")

    if tai_khoan_hien_tai is not None:
        print("Ban dang dang nhap voi tai khoan:",
              tai_khoan_hien_tai)
        return

    ten_dang_nhap = input("Nhap ten dang nhap: ").strip()
    mat_khau = input("Nhap mat khau: ").strip()

    conn = ket_noi_database()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT mat_khau, salt
        FROM tai_khoan
        WHERE ten_dang_nhap = ?
    """, (ten_dang_nhap,))

    tai_khoan = cursor.fetchone()
    conn.close()

    if tai_khoan is None:
        print("Tai khoan khong ton tai!")
        return

    mat_khau_luu, salt = tai_khoan
    mat_khau_nhap = ma_hoa_mat_khau(mat_khau, salt)

    if mat_khau_nhap == mat_khau_luu:
        tai_khoan_hien_tai = ten_dang_nhap
        print("DANG NHAP THANH CONG!")
        print("Xin chao:", ten_dang_nhap)
    else:
        print("Mat khau khong chinh xac!")


# 3. DANG XUAT TAI KHOAN
def dang_xuat():
    global tai_khoan_hien_tai

    print("\n========== DANG XUAT ==========")

    if tai_khoan_hien_tai is None:
        print("Ban chua dang nhap!")
        return

    ten_cu = tai_khoan_hien_tai
    tai_khoan_hien_tai = None

    print("Dang xuat thanh cong!")
    print("Tai khoan", ten_cu, "da dang xuat.")


# MENU KIEM TRA
if __name__ == "__main__":

    while True:
        print("\n================================")
        print("       QUAN LY TAI KHOAN")
        print("================================")
        print("1. Dang ky")
        print("2. Dang nhap")
        print("3. Dang xuat")
        print("0. Thoat")
        print("================================")

        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "1":
            dang_ky()

        elif lua_chon == "2":
            dang_nhap()

        elif lua_chon == "3":
            dang_xuat()

        elif lua_chon == "0":
            print("Da thoat chuong trinh!")
            break

        else:
            print("Lua chon khong hop le!")

