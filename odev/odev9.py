#Kullanıcıdan bir kelime alın ve kelimenin palindrome (tersinden de okunduğunda aynı olan) olup olmadığını kontrol edin.

kelime = "ada"
ters_kelime = kelime[::-1]
print(ters_kelime)
if kelime == ters_kelime:
    print("Bu kelime palindromedir")
    
    


