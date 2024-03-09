#eleman frekansı bulma

liste=[1,1,1,1,1,1,1,1,1,0,0,0,0,0]
def eleman_frekansı(liste):
    frekans={}
    for i in liste:
        if i in frekans:
            frekans[i]+=1
        else:
            frekans[i]=1
    return frekans
print(eleman_frekansı(liste))