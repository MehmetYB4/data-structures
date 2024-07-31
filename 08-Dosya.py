f=open("deneme.txt","w")
f.write("BilgisayarKavramlari\n")
f.close()

f=open("deneme.txt","r")
print(f.read())
f.close()

f = open("deneme.txt", "r")
print(f.read(1))
f.seek(1, 0)
print(f.read())
f.close()
