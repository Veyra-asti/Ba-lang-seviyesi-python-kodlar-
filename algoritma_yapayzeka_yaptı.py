# 1. Adım: Başla

# 2. Adım: Register - kullanıcıdan isim ve şifre al
print("=== REGISTER ===")

kayitli_isim = input("Kullanıcı adınızı girin: ")
kayitli_sifre = input("Şifrenizi girin: ")

print("\nKayıt başarılı!")
print("\n=== GİRİŞ ===")

# 3. Adım: Giriş kısmına git, isim ve şifre iste
giris_isim = input("Kullanıcı adınız: ")
giris_sifre = input("Şifreniz: ")

# 4-5. Adım: Bilgileri kontrol et
if giris_isim == kayitli_isim and giris_sifre == kayitli_sifre:
    print("Giriş başarılı!")
else:
    print("Giriş başarısız, tekrar deneyin.")

# 6. Adım: Bitir
