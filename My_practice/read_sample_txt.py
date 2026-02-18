

f=open('sample_txt','r')
text=f.read()

lines=text.splitlines()
words=text.split()
chars=len(text)
print('lines:',len(lines))
print('words:',len(words))
print('characters:',chars)