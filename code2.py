#remove duplicates from list
lst=[1,2,2,3,4,1]
print(list(set(lst)))


remove_dup=[]
for i in lst:
    if i not in remove_dup:
        remove_dup.append(i)
print(remove_dup)

#using dict.fromkeys()
lst=[0,9,8,7,3,8,9]
unique_list=dict.fromkeys(lst)
print(list(unique_list))

#reverse word
def reverse_word(s):
    return ' '.join(s.split()[::-1])
s='hello world'
print('reverse_word:',reverse_word(s))

#palindrome
def palindrome(s):
    return s==s[::-1]
s='madam'
print(palindrome(s))

#vowels
def vowels(s):
    vowels='aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
s='helloo world'
print('count of vowels:',vowels(s))