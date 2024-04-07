# Regular Expression - (re)

import re

print("a or d is replaced by * :",re.sub('[ad]','*', 'abcdefabdabcdef'))
print("abc is replaced by * :",re.sub( 'abc','*', 'abcdefabdabcdef'))
print("* replaces abc with 123:", re.sub('[abc][123]','*','a1+b2+c3+d4+e5'))
print("AB is replaced by * :", re.sub('A.B','*', 'A2B A*B A**B A5B'))
print("A followed by B anytime is replaced by * :", re.sub('Ab+','*', 'Abc Abbbbb Ac'))
print("A followed by B upto 6th time is replaced by * :", re.sub('AB{3,6}','*', 'ABB ABBB ABBBBBB AC'))
print("* replaces letters starts with abc :", re.sub('^abc','*', 'abcdefabdabcdef'))
print("* replaces letters end with abc :", re.sub('abc$','*', 'abcdefabdabc'))
print("Pattern is searched at the end :", re.search('ab','Here is an absolute string'))
print("Pattern is searched at the beginning ;", re.match('ab','Here is an absolute string'))
      
