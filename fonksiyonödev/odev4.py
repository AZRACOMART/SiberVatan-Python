#)Bir fonksiyon oluşturun. Fonksiyon içinde bir tane liste olsun ve bu listenin ilk ve son sayısı eşitse ekrana true değilse false yazdırsın.

liste = [90,7,20,90]

def ilkson_esitmi(liste):
    if len(liste) < 2:
        return False
    else:
        return liste[0] == liste[-1]

print(ilkson_esitmi(liste))  

 