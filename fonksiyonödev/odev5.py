#Bir sayının palindrom sayı olup olmadığını kontrol eden fonksiyonu yazınız.

sayi = int(input("Bir sayı girin: "))

def palindromkontrol(sayi):
    sayii= str(sayi)
    ters_sayi = sayii[::-1]
    if sayii == ters_sayi:
        return True
    else:
        return False 
if palindromkontrol(sayi):
    print("sayı palindrom")
else:
    print("sayı palindrom değil")
