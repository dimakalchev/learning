# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = (position + shift_amount) % len(alphabet)
#     new_letter = alphabet[new_position]
#     cipher_text += new_letter
#   print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#   decipher_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     old_position = (position - shift_amount) % len(alphabet)
#     old_letter = alphabet[old_position]
#     decipher_text += old_letter
#   print(f"The decoded text is {decipher_text}")


# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#   decrypt(cipher_text=text, shift_amount=shift)
# else:
#   print("Your direction is wrong. Try again.")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
stop = False
while stop is False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = (position + shift_amount) % len(alphabet)
                end_text += alphabet[new_position]
            else:
                end_text += char
        print(f"Here's the {cipher_direction}d text is {end_text}")


    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    answer = input("Type 'stop', if you want to leave. Type\n 'go', if you want to continue:\n").lower()
    if answer == "stop":
        stop = True
        print("Goodbye")
    else:
        stop = False

