t=(1,2,3)
print(t)
#tuple tanımlandıgı zaman degisemez(inmutebile)

#t[1]=770 çalışmaz

x,y,z=t
print(x)
z=10
print(t)
t=(x,y,z) #paketleme değeri günceller!! yeni tuple oluşturur
print(t)

v=([1,2,3],[4,5,6])
print(v)
v[0][1]=100 #liste değişti, tuple değişmez!! Tuple 2 tane pointer tutuyor
print(v)

t2=1,2,3,"konya"
print(t2)