data = ('John Doe', '12345678', 'Jakarta, Indonesia')

nama = data[0]
nim = data[1]
alamat = data[2]

print("Data:", data)
print("NIM :", nim)
print("NAMA :", nama)
print("ALAMAT :", alamat)

nim_tuple = tuple(nim)
print("NIM:", nim_tuple)

nama_depan = tuple(nama[1:8])
print("NAMA DEPAN:", nama_depan)

nama_terbalik = tuple(nama.split()[::-1])
print("NAMA TERBALIK:", nama_terbalik)
