liste=[1,2,3,4]
liste.append(55)
liste.insert(2,8)
print(liste)
liste.remove(2)
print(liste)
liste2=[8,7,9]
liste.extend(liste2)
print(liste)
liste.append(liste2)  #liste içine liste ekleme
print(liste)
print(liste.count(8)) #8 den kaç tane var
#liste.sort()
print(liste)
liste2.clear()
print(f"liste2 silindi {liste2}")
liste2=[8,7,9]
liste3=liste2 #bu atama işlemi pointer olarak olur
liste3.append(55)
print(liste3)
print(liste2)
#görüldüğü gibi ikiside de değişti!! liste2 ve liste 3 hafızada aynı yeri gösteriyor
liste4=liste2.copy()
liste4.append(74) #bu atama bellekte yeni bir yer oluşturur
print(liste4)
print(liste2)