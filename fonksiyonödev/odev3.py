# İki fonksiyon oluşturun. İki fonksiyon içinde de listeler olsun ilk fonksiyon içindeki listenin en büyük sayısını ikinci fonksiyon içindeki
# listenin en küçük sayısını toplayıp ekrana bastırın.

liste1 = [99,93,78,22,17]
liste2 = [10,1,21,25,18]

def en_buyuk(liste1):
    return max(liste1)
def en_kucuk(liste2):
    return min(liste2)
en_buyuk_sayi = en_buyuk(liste1)
en_kucuk_sayi = en_kucuk(liste2)

print(en_buyuk_sayi + en_kucuk_sayi)
    