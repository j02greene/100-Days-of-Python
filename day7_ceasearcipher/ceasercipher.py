import logo

logo = logo.logo

print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceaser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")
    

#def encrypt(plain_text, shift_amount):
#    cipher_text = ""
#    for letters in plain_text:
#       position = alphabet.index(letters)
#       new_position = position + shift_amount
#       new_letter = alphabet[new_position]
#       cipher_text += new_letter
#    print(f"the encoded text is {cipher_text}.")


#def decrypt(cipher_text, shift_amount):
#    plain_text = ""
#    for letters in cipher_text:
#        position = alphabet.index(letters)
#        old_position = position - shift_amount
#        old_letter = alphabet[old_position]
#        plain_text += old_letter
#    print(f"the decoded text is {plain_text}.")
do_continue = True

while do_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    shift = shift % 26

    ceaser(start_text = text, cipher_direction = direction, shift_amount = shift)

    answer = input("Type 'yes' to continue. Otherwise type 'no'\n")

    if answer == 'no':
        do_continue = False
        print("Goodbye")
