"""
No Vowels
Description
Write a program to accept a string from the user, delete all vowels from the string and display the result. 
"""

# Take input
s=input()

# Write your code here

vowels = ('a', 'e', 'i', 'o', 'u')

s_vowels_removed = ''.join([letter for letter in s if letter.lower() not in vowels])  # compare after converting to lower case


#Print the result

print(s_vowels_removed)

#
list_letter = []
for letter in s:
    if letter not in vowels:
        list_letter.append(letter)

print(list_letter)




