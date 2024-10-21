# List berisi string 
fruits = ["apple", "banana", "cherry"] 
  
# Menambahkan elemen baru 
fruits.append("orange") 
print("Setelah menambahkan 'orange':", fruits) 
  
# Menghapus elemen tertentu 
fruits.remove("banana") 
print("Setelah menghapus 'banana':", fruits) 
  
# Menggunakan tuple untuk informasi tambahan 
fruit_info = ( 
    ("apple", "red", 1.0), 
    ("banana", "yellow", 0.5), 
    ("cherry", "red", 2.0), 
    ("orange", "orange", 1.5) 
) 
  
# Menggunakan dictionary untuk menyimpan stok 
fruit_stock = { 
    "apple": {"stok": 10, "harga": 1.0}, 
    "banana": {"stok": 5, "harga": 0.5}, 
    "cherry": {"stok": 20, "harga": 2.0}, 
    "orange": {"stok": 15, "harga": 1.5} 
} 
  
# Mencetak informasi tambahan dari tuple dan dictionary 
print("\nInformasi Buah:") 
for fruit in fruits: 
    if fruit in fruit_stock: 
        stok = fruit_stock[fruit]["stok"] 
        harga = fruit_stock[fruit]["harga"] 
        print(f"{fruit.capitalize()} - Stok: {stok}, Harga per kg: Rp{harga}") 
