from fbthon import CreateAccount

print (" Daftar Akun Facebook \n")

firstname = input("[?] Nama Depan : ") # Nama Depan
lastname = input("[?] Nama Belakang : ") # Nama Belakang
email = input("[?] Email/Phone : ") # Alamat email / No Hp
gender = input("[?] Jenis Kelamin(Male/Female): ") # Gender
ultah = input("[?] Tanggal Lahir (DD/MM/YYYY): ") # Tanggal lahir
password = input("[?] Password : ")  # Kata Sandi

new_account = CreateAccount(firstname = firstname, lastname = lastname, email = email, gender = gender, date_of_birth = ultah, password = password)

print ("\n Masukkan Kode Verifikasi yang sudah di kirim ke "+ email)
kode = input("[?] Kode Verifikasi : ")

# Method `confirm_account` akan mengembalikan `True` Jika berhasil mengkonfirmasi akun.
konfir = new_account.confirm_account(kode)

if konfir:
  print ("[✓] Berhasil Membuat Akun Facebook :)\n")
  print (" Nama Akun : %s %s" % (firstname,lastname))
  print (" ID Akun : %s" % (new_account.get_cookie_dict()['c_user']))
  print (" Email/Phone : %s" % (email))
  print (" Jenis Kelamin : %s" % (gender))
  print (" Tanggal lahir : %s" % (ultah))
  print (" Password : %s" % (password))
  print (" Cookie Akun : %s" % (new_account.get_cookie_str()))
  print (" Token Akun : %s" % (new_account.get_token()))
  sys.exit(0)
else:
  print ("[!] Gagal Membuat Akun Facebook ")
  sys.exit(1)