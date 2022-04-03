
#### RSA ciphering

import rsa
 
public_key, private_key = rsa.newkeys(512) # should be at least 16
 

message = "Is rsa good for encryption?"
 
encrypted_message = rsa.encrypt(message.encode(),
                         public_key)
 


print("original message: ", message)
print("encrypted message: ", encrypted_message)

decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()
 
print("decrypted message: ", decrypted_message)