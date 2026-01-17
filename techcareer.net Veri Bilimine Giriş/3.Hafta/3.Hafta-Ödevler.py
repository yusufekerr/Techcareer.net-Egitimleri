
#1.Soru
notlar = [85, 92, 76, 92, 100, 76, 85, 92]

benzersiz_notlar = list(set(notlar))
print(f"Tekrar etmeyen notlar: {benzersiz_notlar}")

en_yuksek = max(benzersiz_notlar)
en_dusuk = min(benzersiz_notlar)

print(f"En yüksek not: {en_yuksek}")
print(f"En düşük not: {en_dusuk}")


sirali_notlar = sorted(benzersiz_notlar)
print(f"Siralanmiş notlar: {sirali_notlar}")


#2.Soru
def armstrong(sayi):
    toplam = 0
    gecici = sayi

    while gecici > 0:
        basamak = gecici % 10
        toplam += basamak ** 3
        gecici //= 10

    return toplam == sayi

#3.Soru
A = {"Python", "R", "SQL", "Java"}
B = {"C++", "Python", "JavaScript", "SQL"}

ortak_diller = A.intersection(B)
sadece_A = A.difference(B)
birlesim = A.union(B)
sirali_birlesim = sorted(birlesim)

print(f"Ortak diller: {ortak_diller}")
print(f"Sadece A'da olan diller: {sadece_A}")
print(f"Birleşim (alfabetik): {sirali_birlesim}")

#4.Soru
import random
import statistics

sayilar = []

for i in range(10):
    rastgele_sayi = random.randint(1, 100)
    sayilar.append(rastgele_sayi)

ortalama = statistics.mean(sayilar)
standart_sapma = statistics.stdev(sayilar)

print(f"Rastgele sayilar: {sayilar}")
print(f"Ortalama: {ortalama:.2f}")
print(f"Standart sapma: {standart_sapma:.2f}")

#5.Soru
def kelime_sayaci(metin):
    kelimeler = metin.split()
    
    toplam_kelime = len(kelimeler)
    en_uzun_kelime = max(kelimeler, key=len)
    
    frekans = {}
    for kelime in kelimeler:
        kelime = kelime.lower()  
        if kelime in frekans:
            frekans[kelime] += 1
        else:
            frekans[kelime] = 1
    
    en_sik_kelime = max(frekans, key=frekans.get)
    
    return toplam_kelime, en_uzun_kelime, en_sik_kelime

#6.Soru
sayilar = [5, 12, 7, 18, 24, 3, 16]

ciftler = list(filter(lambda x: x % 2 == 0, sayilar))
kareler = list(map(lambda x: x ** 2, ciftler))
sirali_kareler = sorted(kareler, reverse=True)

print(f"Çift sayilar: {ciftler}")
print(f"Kareleri: {kareler}")
print(f"Azalan sirali kareler: {sirali_kareler}")


#7.Soru
kelimeler = ["veri", "bilim", "analiz", "yapayzeka", "python"]

sirali_kelimeler = sorted(kelimeler, key=lambda kelime: len(kelime))

print(f"Uzunluğa göre siralanmiş kelimeler: {sirali_kelimeler}")

#8.Soru
def rakam_toplami(metin):
    toplam = 0
    sayi = ""

    for karakter in metin:
        if karakter.isdigit():
            sayi += karakter
        else:
            if sayi != "":
                toplam += int(sayi)
                sayi = ""

    if sayi != "":
        toplam += int(sayi)

    return toplam

#Proje
kitaplar = [
    {"isim": "Veri Bilimi 101", "yazar": "Ali", "tur": "Bilim", "satis": 1200, "yil": 2021},
    {"isim": "Python ile Yapay Zeka", "yazar": "Ayşe", "tur": "Bilim", "satis": 950, "yil": 2020},
    {"isim": "İstatistik Temelleri", "yazar": "Ali", "tur": "Akademik", "satis": 700, "yil": 2019},
    {"isim": "Makine Öğrenmesi", "yazar": "Can", "tur": "Bilim", "satis": 1800, "yil": 2022},
    {"isim": "Veri Görselleştirme", "yazar": "Deniz", "tur": "Sanat", "satis": 400, "yil": 2018},
    {"isim": "Matematiksel Modelleme", "yazar": "Ali", "tur": "Akademik", "satis": 1500, "yil": 2021},
    {"isim": "Bilgi Toplumu", "yazar": "Ayşe", "tur": "Sosyal", "satis": 600, "yil": 2022}
]

def en_cok_satan(kitaplar):
    return max(kitaplar, key=lambda x: x["satis"])

def yazar_satislari(kitaplar):
    yazarlar = {}
    for kitap in kitaplar:
        yazar = kitap["yazar"]
        yazarlar[yazar] = yazarlar.get(yazar, 0) + kitap["satis"]
    return yazarlar


turler = set(kitap["tur"] for kitap in kitaplar)

populer_kitaplar = [kitap["isim"] for kitap in kitaplar if kitap["satis"] > 1000]


yeni_kitaplar = list(filter(lambda x: x["yil"] > 2020, kitaplar))


zamli_satislar = list(map(lambda x: int(x["satis"] * 1.10), kitaplar))


sirali_kitaplar = sorted(kitaplar, key=lambda x: x["satis"], reverse=True)

import statistics


ortalama_satis = statistics.mean([kitap["satis"] for kitap in kitaplar])


from collections import defaultdict
tur_satislari = defaultdict(int)
for kitap in kitaplar:
    tur_satislari[kitap["tur"]] += kitap["satis"]
en_populer_tur = max(tur_satislari, key=tur_satislari.get)


std_sapma = statistics.stdev([kitap["satis"] for kitap in kitaplar])


import random


train_boyutu = int(len(kitaplar) * 0.7)
train_set = random.sample(kitaplar, train_boyutu)
test_set = [kitap for kitap in kitaplar if kitap not in train_set]


yazar_satis = {}
yazar_sayisi = {}

for kitap in train_set:
    yazar = kitap["yazar"]
    yazar_satis[yazar] = yazar_satis.get(yazar, 0) + kitap["satis"]
    yazar_sayisi[yazar] = yazar_sayisi.get(yazar, 0) + 1

yazar_ortalamalari = {yazar: yazar_satis[yazar] / yazar_sayisi[yazar] for yazar in yazar_satis}

ust_ortalama_kitaplar = []
for kitap in test_set:
    yazar = kitap["yazar"]
    ortalama = yazar_ortalamalari.get(yazar, 0)
    if kitap["satis"] > ortalama:
        ust_ortalama_kitaplar.append(kitap["isim"])



print("En çok satan kitap:", en_cok_satan(kitaplar))
print("Yazar satişlari:", yazar_satislari(kitaplar))
print("Kitap türleri:", turler)
print("Popüler kitaplar:", populer_kitaplar)
print("2020 sonrasi çikanlar:", [k["isim"] for k in yeni_kitaplar])
print("Zamli satişlar:", zamli_satislar)
print("Satişa göre sirali kitaplar:", [k["isim"] for k in sirali_kitaplar])
print("Ortalama satiş:", ortalama_satis)
print("En çok satan tür:", en_populer_tur)
print("Satişlarin standart sapmasi:", std_sapma)
print("Train set yazar ortalamalari:", yazar_ortalamalari)
print("Test sette ortalamanin üstünde satan kitaplar:", ust_ortalama_kitaplar)
