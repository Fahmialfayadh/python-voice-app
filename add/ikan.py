def ikan(a, b):  # Koma yang benar dipakai antara a dan b
    hasil = a + b  # Kode di dalam fungsi harus terindentasi
    return hasil  # Jangan lupa untuk return hasil
def kurang(a, b):
    hasil = a - b
    return hasil
def bagi(a, b):
    hasil = a/b
    return hasil
def menu():
    print("menu operasi")
    print("1. ikan")
    print("2. kurang")
    print("3. bagi")
def balek():
    ulang = input("mau ulang atau udah? (udah/ulang)")
    return ulang.lower() == 'ulang'
while True:
#meminta data
  menu()
  n = (int(input("operasi: ")))
  a = (float(input("masukkan a: ")))
  b = (float(input("masukkan b: ")))

#jalankan fungsi
  if n == 1:
     jumlah = ikan(a, b)
     print ("hasil jumlah: ", jumlah) # Memanggil fungsi ikan dengan parameter 2 dan 1
  elif n == 2:
     jumlah = kurang(a, b)
     print ("hasil kurang: ", jumlah)
  elif n == 3: 
     jumlah = bagi(a, b)
     print ("hasil bagi: ", jumlah)

  if not balek():
    import add.calc


