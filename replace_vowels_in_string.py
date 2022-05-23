noVowel = 'This sentence is too LONG!!!'



def disemvowel(string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for alphabet in string:
        if alphabet.lower() in vowels:
            string = string.replace(alphabet, '')

    return string

#

def disemvow(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

#

import re
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.sub('', noVowel)
print(vowelRegex.sub('', noVowel))


#print(disemvowel(noVowel))
#print(disemvow(noVowel))


