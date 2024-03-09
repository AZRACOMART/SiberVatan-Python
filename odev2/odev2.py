#floyd üçgenini yazdırmak için python kodunu yazınız.

def floyd(satir):
    number=1
    for i in range(1,satir+1):
        for j in range(1,i+1):
            print(number,end=" ")
            number +=1
        print()    
satir=int(input("satir sayisini giriniz:"))
floyd(satir)
