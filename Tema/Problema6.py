# Introduceti un cuvant (fara majuscule): rabdare
# r apare de 2 ori.


# def find_duplicates(string):
#     duplicates=[]
#     for letter in string:
#         if string.coun(letter)>1 and letter not in duplicates:
#             duplicates.append(letter)
#     return duplicates
# string = input('Introduceti cuvantul: ')
# duplicates = find_duplicates(string)
# print(duplicates)
#
#
# # Problema 6
# cuvant = input("Introduceti textul ")
# duplicate_char = []
# for character in cuvant:
#     if cuvant.count(character) > 1:
#         if character not in duplicate_char:
#             duplicate_char.append(character)
# print(*duplicate_char)


word = input("Enter a word:")
count = 0

for letter in word:
    if word [0] == letter:
        count +=1
print(f"'{word[0]}' appears {count} times.")