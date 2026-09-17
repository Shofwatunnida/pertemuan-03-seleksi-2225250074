# Program menentukan kelulusan berdasarkan nilai dan kehadiran

nilai = float(input("Nilai akhir: "))
kehadiran = float(input("Kehadiran (%): "))

if nilai >= 60 and kehadiran >= 80:
    print("Lulus")
else:
    print("Belum lulus")