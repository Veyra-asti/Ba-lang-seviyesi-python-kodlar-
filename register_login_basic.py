# Register Kısmı
print("Kayit  Olunuz")

kullanici_adi_iste = input("\nKullanici Adinizi Giriniz:")
kullanicidan_sifre_iste = input("Şifrenizi Giriniz:")

print("\nKayit Başarili")
# Giriş Kısmı
print("\nGiriş Yapiniz")

kullaninici_adi = input("\nAdinizi Giriniz:")
kullaninici_sifresi = input("Şifrenizi Giriniz:")

if kullaninici_adi == kullanici_adi_iste and kullanicidan_sifre_iste == kullaninici_sifresi:
    print("Giriş Başarili,Hoşgeldiniz!")
else:
    print("Giriş Başarisiz,Tekrar Deneyiniz!")