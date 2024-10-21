# Meminta input dari pengguna 
nilai = float(input("Masukkan nilai ujian (0-100): ")) 
  
# Menggunakan struktur kontrol if-then-else 
if nilai >= 90: 
    print("Grade: A") 
elif nilai >= 80: 
    print("Grade: B") 
elif nilai >= 70: 
    print("Grade: C") 
elif nilai >= 60: 
    print("Grade: D") 
elif nilai >= 0: 
    print("Grade: F") 
else: 
    print("Nilai tidak valid. Harap masukkan nilai antara 0 hingga 100.") 
