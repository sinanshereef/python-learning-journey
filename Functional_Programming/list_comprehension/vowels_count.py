

str='liminartechnolab'
vowels='AEIOUaeiou'
count=0
lst=[i for i in str for j in vowels if i==j]
print(len(lst))