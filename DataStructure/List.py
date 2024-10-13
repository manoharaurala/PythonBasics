list_1=[1,2,3,4,5,6,7,8]
print(str(list_1.count(3)))

if 1 in list_1:
    print("1 is in list")
if 9 not in list_1:
    print("9 is not in the list")

list_2=[1,2,3,bool,"manohara","ruby"]
print(list_2)

list_3=list("ruby 420")
if "a" in list_3:
    print("a is in list")
elif "r" in list_3:
    print('r is in list')

list_4=[1,2,3,4,5,6,7,8,9]
list_4[1:3]=[45,46,47,48]
print(list_4)

list_5=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
del list_5[15]
print(list_5)

list_5.remove(17)
print(list_5)

list_5.append(16)
print(list_5)

list_5.append(17)
print(list_5)

list_5.append(34)
list_5.append(24)
list_5.insert(18,46)
print(list_5)
list_5.sort()
print(list_5)


list_6=["Banana","Apple","Cat","asdfdf","bdfdds","Dog","csdsdsd"]
list_6.sort()
print(list_6)

list_6.sort(key=str.lower)
print(list_6)