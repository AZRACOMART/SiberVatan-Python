#Rus ruleti oyunu yazın. Random kütüphanesi kullanarak 1-6 arasında bir sayı seçilsin ve kullanıcıdan bir sayı alsın eşit olduğunda oyun biter.
#2 fonksiyon kullanarak yazabilirsiniz.

import random
def oyuncunun_tahmini_al():
    tahmin = int(input("1 ve 6 arasında bir sayı giriniz:"))
    return tahmin
def rus_ruleti_oyunu():
    hedef = random.randint(1, 6)
    print("sayı belirlendi")
    while True:
        tahmin = oyuncunun_tahmini_al()
        if tahmin < 1 or tahmin > 6:
            print("geçersiz giriş yeniden dene")
            continue
        elif tahmin == hedef:
            print("kazandın")
            break
        else:
            print("yanlış tahmin tekrar dene")
            
rus_ruleti_oyunu()
