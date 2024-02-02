#Kullanıcıdan bir cümle alın, cümlede geçen kelimelerin içinde en uzun olanını bulun.

cümle = "kimya dersi eğlencelidir"
kelimeler = cümle.split()
enuzun_kelime = max(kelimeler, key=len)
print(enuzun_kelime)


