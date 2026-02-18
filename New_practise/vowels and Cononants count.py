



st=input("Enter the String of Text: ")
def count_vowels_consonants():
    vowels='AEIOUaeiou'
    vowels_count=0
    consonants_count=0
    for i in st:
        if i in vowels:
            vowels_count+=1
        else:
            consonants_count+=1
    print("Vowels Count=",vowels_count)
    print('Consonants Count=',consonants_count)
count_vowels_consonants()
