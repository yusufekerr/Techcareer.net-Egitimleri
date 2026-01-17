# Soru 1 

sayi = float(input(f"Lütfen bir sayi giriniz: "))

if sayi > 0 and sayi % 2 == 0:
    print ("Pozitif ve çift")
elif sayi > 0 and sayi % 2 != 0:
    print("Pozitif ve tek")
elif sayi <0 and sayi % 2 == 0:
    print ("Negatif ve çift")
elif sayi <0 and sayi % 2 != 0:
    print("Negatif ve tek")

# Soru 2

kelime = input(f"Lütfen bir kelime giriniz: ")

harf_sayilari = {}

for harf in kelime:
    if harf in harf_sayilari:
        harf_sayilari[harf] += 1
    else:
        harf_sayilari[harf] = 1

print(harf_sayilari)

# Soru 3

sifre = input(f"Lütfen bir şifre giriniz: ")

uzunluk_kontrolu = len(sifre) >= 8

buyuk_harf_kontrolu = False

for karakter in sifre:
    if karakter.isupper():
        buyuk_harf_kontrolu = True
        break

rakam_kontrolu = False

for karakter in sifre:
    if karakter.isdigit():
        rakam_kontrolu = True
        break


if uzunluk_kontrolu and buyuk_harf_kontrolu and rakam_kontrolu:
    print("Sifre gecerli")
else:
    print("Sifre gecersiz")
    if not uzunluk_kontrolu:
        print("- Sifre en az 8 karakter olmali")
    if not buyuk_harf_kontrolu:
        print("- Sifrede en az 1 büyük harf bulunmali")
    if not rakam_kontrolu:
        print("- Sifrede en az 1 rakam bulunmali")


# Soru 4

sayilar = [12, 4, 9, 25, 30, 7, 18]

toplam = sum(sayilar)
adet= len(sayilar)
ortalama = toplam / adet

buyukler = []

for sayi in sayilar:
    if sayi > ortalama:
        buyukler.appendd(sayi)

print(f"Listenin ortalamasi: {ortalama: .2f}")
print(f"Ortalamadan büyük sayilar: {buyukler}")


# Soru 5

for satir in range (1, 6):
   for yildiz in range(satir):
        print("*", end="")
print()

# Soru 6

toplam = 0
adet = 0

sayi = int(input("Bir sayi giriniz: "))

while sayi != 0:
    toplam += sayi
    adet += 1
    sayi = int(input("Bir sayi giriniz"))

if adet > 0:
    ortalama = toplam / adet
    print(f"\nToplam: {toplam}")
    print(f"Ortalama: {ortalama: .2f}")
else: 
    print("\nHic sayi girilmedi.")


# Soru 7

kelime = input("Bir kelime giriniz: " )
ters_kelime = kelime[::-1]

if kelime == ters_kelime:
    print("Palindrom")
else:
    print("Palindrom değil")


# Soru 8

sayilar = range (1, 100)

listem = []

for sayi in sayilar:
    if sayi % 3 == 0 and sayi % 5 == 0:
        listem.append(sayi)

print(listem)

# Soru 9

cümle = input("Bir cümle giriniz: ")

kelime_havuzu = cümle.split()
print(kelime_havuzu)

yeni_kelime_listesi = []

for kelime in kelime_havuzu:
    yeni_kelime = kelime.capitalize()
    yeni_kelime_listesi.append(yeni_kelime)

yeni_cümle = " ".join(yeni_kelime_listesi)
print(yeni_cümle)

# Soru 10

print("Lütfen film ile ilgili 6 adet yorum giriniz:")
yorumlar = []

for i in range(6):
    yorum = input(f"{i+1}. yorum: ")
    yorumlar.append(yorum)

print(f"\nFilm ile ilgili yorumlar: {yorumlar}")

uzunluklar = []

for yorum in yorumlar:
    uzunluklar.append(len(yorum))


iyi_sayisi = 0

for yorum in yorumlar:
    if "iyi" in yorum.lower():
        iyi_sayisi += 1

en_uzun_yorum = max(yorumlar, key=len)
en_kisa_yorum = min(yorumlar, key=len)

toplam_karakter = sum(uzunluklar)
ortalama_uzunluk = toplam_karakter / len(yorumlar)

print(f"\n 'iyi' kelimesi geçen yorum sayisi: {iyi_sayisi}")
print(f"En uzun yorum: {en_uzun_yorum}")
print(f"En kisa yorum: {en_kisa_yorum}")
print(f"Yorumlarin ortalama uzunlugu: {ortalama_uzunluk: .2f} karakter")





