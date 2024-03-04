text = 'Hello world'

encrypted_text = ''
for letter in text:
    encrypted_text += chr(ord(letter) ^ 200)
print(encrypted_text)

decrypted_text = ''
for letter in encrypted_text:
    decrypted_text += chr(ord(letter) ^ 200)
print(decrypted_text)
