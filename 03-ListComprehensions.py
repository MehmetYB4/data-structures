l=[]
#yan etki söz konusu, liste tanımlandıgı amac dışında kullanılmasıdır
for x in range(1,11):
    l.append(x**2)
print(l)
#alttaki tanım daha doğru FOnksiyonel Programlama
#İsimsiz bir fonksiyon tanımlamak
#map listenin elemanlarını tek tek fonksiyona uygular
#lambda : x parametre al return x**2 yap
squares=list(map(lambda x: x**2,range(1,11)))#bu iyi gösterim
print(squares)
#print(x) biz buna ulaşamayız, bu iyi birşey

squares2=[z**2 for z in range(1,11)] #başka bir kullanım
print(squares2)
print(type(squares2))

listem=[(x,y) for x in [1,2,3] for y in[5,3,7] if x!=y]
print(listem)
listem2=[(x,y,z) for x in [1,2,3] for y,z in[(1,2),(2,4),(7,1)] if x!=y]
print(listem2)

#(1,2,3,4)
#(2,3,4,5)
#(3,4,5,6)
#(4,5,6,7) ödev

