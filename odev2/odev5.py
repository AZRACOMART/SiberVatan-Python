#verilen iki dize arsında ortak elemanları bulan bir python fonksiyonu yaznız.

def ortakeleman(l1,l2):
    ortak=list()
    for x in l1:
        if x in l2:
            ortak.append(x)
    return ortak
l1=[5,777,22,17,69]
l2=[22,17,777,99,78]
print(ortakeleman(l1,l2)) 