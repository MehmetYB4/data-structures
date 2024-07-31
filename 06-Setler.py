k={1,2,3,5,4,12,4,2,3} #kümeler
#kümelerde eleman var mı yok mu önemlidir. eleman sırası önemli değildir.
#aynı elemandan 2 kere olmaz
print(k)
l=[1,4,2,5,7,5,1,2,3]
k2=set(l)
print(k2)

k4=set("bilgisayart")
k5=set("mehmet")
print(k4)
print(k5)

print(k4|k5)  #set union, birleştirme
print(k4-k5)  #küme farkı
print(k4&k5)  #küme kesişimi
print(k4^k5)  #özel veya, birinde olup birinde olmayanları alır
