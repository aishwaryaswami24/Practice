# #remove duplicates from list
# lst=[1,2,2,3,4,1]
# print(list(set(lst)))
#
#
# remove_dup=[]
# for i in lst:
#     if i not in remove_dup:
#         remove_dup.append(i)
# print(remove_dup)
#
# #using dict.fromkeys()
# lst=[0,9,8,7,3,8,9]
# unique_list=dict.fromkeys(lst)
# print(list(unique_list))
#
# #reverse word
# def reverse_word(s):
#     return ' '.join(s.split()[::-1])
# s='hello world'
# print('reverse_word:',reverse_word(s))
#
# #palindrome
# def palindrome(s):
#     return s==s[::-1]
# s='madam'
# print(palindrome(s))
#
# #vowels
# def vowels(s):
#     vowels='aeiouAEIOU'
#     return sum(1 for char in s if char in vowels)
# s='helloo world'
# print('count of vowels:',vowels(s))
#
# #anagrams
# def sorted_anagrams(s1,s2):
#     return sorted(s1)==sorted(s2)
#
# s1='silent'
# s2='listen'
# print(sorted(s1))
# print(sorted(s2))
# print(sorted_anagrams(s1,s2))
#
# #is_digit
# def is_digit(s):
#     return s.isdigit()
# s='aish1234'
# print(is_digit(s))
#
# #remove string
# def remove_duplicates(s):
#     return ''.join(sorted(set(s)))
# s='abracadabra'
# print(remove_duplicates(s))

#even_odd
lst=[1,2,3,4,5,5,9]
odd_count=0
even_lst=[]
for i in lst:
    if i%2==0:
        even_lst.append(i)
    else:
        odd_count -=1

print(even_lst)