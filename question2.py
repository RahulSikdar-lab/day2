''' Count Vowels and Consonants in a String
Question:
Take a string input and count the number of vowels and consonants using loops and conditionals.'''
text=input("Enter the text ")
vowels= "aeiouAEIOU"
vowels_count=0
consonant_count=0
for i in text:
    if i.isalpha():
        if i in vowels:
            vowels_count +=1
        else:
            consonant_count +=1
print("vowels count",vowels_count)
print("consonant_count",consonant_count)