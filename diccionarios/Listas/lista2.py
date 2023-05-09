from subprocess import list2cmdline

from numpy import append


list1 = [1,2,3,4,5]
list2 = list1
print(list2)
list1.append(1)
list1.insert(0,0)
del list1[:]
print(list2)


list3=[1,2,3,4]
list4=list3[:2]
list3.append(5)
if 7 not in list3:
    print(list4)
    print(list3)

