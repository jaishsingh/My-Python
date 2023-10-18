# square=[]
# for x in range(1,11):
#     square.append(x**2)
# print(square)

# seq=[x for x in range(1,20) if x%2==0]
# print(seq)
# seq=[x**2 for x in range(1,20)]
# print(seq)
names =(['Jaish Singh','Aditya Thakur','Shivang Singh','Agamya Samuel','Aditya Kumar'])
initials = [name.split()[0][0].upper() + "." +name.split()[1][0].upper() for name in names]
print(initials)
