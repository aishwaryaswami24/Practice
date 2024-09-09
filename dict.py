dict1={'ID': '101','Name': 'Aishwarya'}
dict2={'ID':'102','Name': 'Shubham'}

#when both dicts attribute names are same then it will replace dict1 attribute to dict2
dict1.update(dict2)
print(dict1)

dict3=dict1 | dict2
print(dict3)


dict3={'id1': 1,'name1':'aish'}
dict4={'id2':2,'name2':'shubh'}

dict3.update(dict4)
print(dict3)