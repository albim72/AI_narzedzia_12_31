import numpy as np

print("podstawy biblioteki NUMPY")

print(np.zeros(13))
jedynka = np.ones(22,dtype=int)
print(jedynka)
print(type(jedynka))

mojalista = [34,1,8,3,63]
print(mojalista)
print(type(mojalista))

u = np.arange(1,2.5E8,16)
print(u)

g = np.array([4,5,7,9,0,13,68])
print(g)

h = np.linspace(0,10,num=5)
print(h)

#konkatenacja list pythona
l1 = [5,6,7,8]
l2 = [11,45,24,78]
l3 = [45,28,90,67]

ml = l1+l2+l3
print(ml)

#konkatenacja tablic numpy
a = np.array(l1)
b = np.array(l2)
c = np.array(l3)

s = a+b+c
print(s)

sc = np.concatenate((a,b,c))
print(sc)

#CTRL + D -> duplikacja linii lub bloku kodu
#CTRL + / -> komentowanie/odkomentowanie linii lub bloku kodu

listalist = [[2,7],[8,9]]
print(listalist)

print(listalist[1])
print(listalist[1][0])
# print(listalist[1,0])

npmacierz = np.array([[1,8],[15,6]])
print(npmacierz)
print(npmacierz[1][1])
print(npmacierz[1,1])

tensor3D = np.array([[[1,2,3],[7,5,9],[3,2,4]],[[10,2,6],[45,24,7],[1,1,1]],[[9,11,45],[34,2,1],[8,2,7]]])
print(tensor3D)

dane = np.arange(27)
print(dane)
dane3D = dane.reshape((3,3,3))
print(dane3D)
