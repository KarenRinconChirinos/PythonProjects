my_list=[1,2,3]
for v in range(len(my_list)):
    print(v)
    print(my_list[v])
    my_list.insert(1,my_list[v])
print(my_list)