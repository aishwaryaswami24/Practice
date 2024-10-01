#remove duplicates from list
lst=[1,2,2,3,4,1]
print(list(set(lst)))


remove_dup=[]
for i in lst:
    if i not in remove_dup:
        remove_dup.append(i)
print(remove_dup)