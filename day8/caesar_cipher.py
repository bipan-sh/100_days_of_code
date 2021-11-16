alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'
, 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'
, 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art
print(art.logo)

def caesar(text, shift, direction):
    
    if shift > 26:
        shift = shift % 26 
    new_word = []

    for i in text:
        
        if i in alphabet:
            li = alphabet.index(i)
            new_index = 0
            if direction == 'encode':
                new_index = li + shift
                new_word.append(alphabet[new_index])
            if direction == 'decode':
                new_index = li - shift
                new_word.append(alphabet[new_index])

            
            

        if i not in alphabet:
            new_word.append(i)

    #print(new_word)
    ciphered = ''.join(new_word)

    print(f"The {direction}d text is {ciphered}")




direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#combined function


caesar(text, shift, direction)
#two functions to encode and decode each
# def encrypt(text, shift) :
#     index= []
#     for i in text:
#         index.append(alphabet.index(i))
   
#     new_index = [i + shift for i in index]
#     new_word = []
#     for l in new_index:
#          new_word.append(alphabet[l])



#     ciphered = ''.join(new_word)
#     print(f"The encrypted text is {ciphered}")


# def decrypt(text, shift):
#     index= []
#     for i in text:
#         index.append(alphabet.index(i))

#     new_index = [i - shift for i in index]
#     new_word = []
#     for l in new_index:
#          new_word.append(alphabet[l])

#     decoded_text = ''.join(new_word)
#     print(f"The decoded text is {decoded_text}")

# if direction == 'encode':
#     encrypt(text, shift)

# if direction == 'decode':
#     decrypt(text, shift)