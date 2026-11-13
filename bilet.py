ad_soyad = input("Adınızı Giriniz! ")
tam_sayi = int(input("\nTam Bilet Sayısını Giriniz! "))
tam_fiyat = float(input("Tam Bilet Birim Fiyatını Giriniz! "))

ogrenci_sayisi = int(input("\nÖğrenci Bilet Sayısını Giriniz! "))
ogrenci_fiyat = float(input("Öğrenci Bilet Birim Fiyatını Giriniz! "))

tam_bilet_toplam = (tam_sayi * tam_fiyat)
ogrenci_bilet_toplam = (ogrenci_sayisi * ogrenci_fiyat)

toplam_bilet = (tam_sayi + ogrenci_sayisi)
toplam_tutar = (tam_fiyat + ogrenci_fiyat)
ortalama = (toplam_tutar / toplam_bilet)

print("Adınız Soyadınız:", ad_soyad)
print("Tam Biletlerin Toplamı:", tam_bilet_toplam)
print("Öğrenci Biletlerin Toplamı:", ogrenci_bilet_toplam)
print("Toplam Bilet Sayısı:", toplam_bilet)
print("Toplam Tutar:", toplam_tutar)
print("Ortalaması:", ortalama)
