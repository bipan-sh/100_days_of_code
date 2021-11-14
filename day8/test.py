alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'
, 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'
, 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art
print(art.logo)


direction = 'encode'
text = input("Type your message:\n").lower()
shift = 5

index= []
if shift > 26:
    shift = shift % 26 
new_word = []
new_index= 0
for i in text:
    
    if i in alphabet:
        li = alphabet.index(i)

        if direction == 'encode':
            new_index = li + shift
        if direction == 'decode':
            new_index = new_index - shift
        
        new_word.append(alphabet[new_index])

    if i not in alphabet:
        new_word.append(i)
        
    

print(new_word)