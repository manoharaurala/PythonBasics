set_1={1,2,3,3,3,3,3,3,2,4,1,44,4,5,6,8}
print(set_1)
set_2=set([1,3,4,4,4,4,4,4,5,5,5])
print(set_2)

set_2.add(25)
print(set_2)
set_2.remove(4)
print(set_2)
set_2.discard(4)
print(set_2)

set_2.clear()
print(set_2)

comp_1={even+2 for even in range(2,11,2)}
print(comp_1)