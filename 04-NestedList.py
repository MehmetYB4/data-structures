l=[1,2,3]

m=[[1,5,3],[5,6,4],l]

print(m)
l[1]=700
print(m)

mt=[[row[i] for row in m] for i in range(3)]
print(f"transpoz= {mt}")

k=[[0,1],[1,4]]
del(k[1])
print(k)