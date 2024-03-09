#10 elemanlı tamsayı listesine klavyeden değerler girilecek listede yer alan en büyük ilk iki sayıyı bularak ekrana yazdıran programı bulunuz.

toplam=10
sayılar=[]
for i in range(toplam):
    deger=int(input("sayı gir:"))
    sayılar.append(deger)
print(sayılar)
sayılar.sort()
print(sayılar)
print(sayılar[-2:]) 
