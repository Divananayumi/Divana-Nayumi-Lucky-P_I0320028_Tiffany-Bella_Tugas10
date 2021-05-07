print ("PROGRAM BIODATA DIRI")
print ("====================")

# Ambil input dari user
namalengkap = input("Nama lengkap: ")
tempatlahir = input("Tempat lahir: ")
tanggallahir = input("Tanggal lahir: ")
umur = input("Umur: ")
jeniskelamin = input("Jenis kelamin: ")
alamat = input("Alamat: ")

# format teks
teks = "Nama lengkap: {}\nTempat lahir: {}\nTanggal lahir: {}\nUmur: {}\nJenis kelamin: {}\nAlamat: {}".format(namalengkap, tempatlahir, tanggallahir, umur, jeniskelamin, alamat)

# buka file untuk ditulis
file_bio = open("file.txt", "w")

# tulis teks ke file
file_bio.write(teks)

# tutup file
file_bio.close()