
from math import gcd
from math import pow
from math import fmod

# Step 1
# Import the message_to_encrypt.txt file 
#file = open("message_to_encrypt.txt","r")
#msg_to_encrypt = file.read()

msg_to_encrypt = input("What is your secret message? ")
split_msg = [char for char in msg_to_encrypt] #split the text into individual characters for easier translation and encryption


# Step 2
#Generating public and private keys
p, q = 17, 19 #selected prime numbers
n = p * q #calculation for RSA modulus
phi_n = int((p-1)*(q-1)) #calculation for euler's toitent

def check_valid_e(a = 5):
    '''
    This function takes in an integer for e and checks whether it is greater than 1, less than phi_n, and not a 
    factor of phi_n. In the event where either of these conditions are not satisfied, a new, valid value for
    e is generated.
        Parameter: a, default = 5, type = int
        Return value: e, type = int 
    '''

    if gcd(a,n) == 1:
        e = a
    else:
        for x in range(2,phi_n):
            if gcd(x,n) == 1:
                e = x
                break
    return e

e = check_valid_e()
i = 3
d = int((i * phi_n + 1)/e)

public_key = [n,e]
private_key = [d,n]

# Step 3
# Creating a translation dictionary for encrypting and decrypting
characters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f",
"g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","\n"]
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,
49,50,51,52,53,54]
encryption_dictionary = dict(zip(characters,numbers))
decryption_dictionary = dict(zip(numbers,characters))


# Step 4
#Writing a function for the encryptor
def encryptor(key, msg):
    '''
    This function takes as input a message, and encrypts it using the public key to generate a cipher.
        Parameter: a_message, type = string
        Return value: encrypted_msg, type = list 
    '''

    encrypted_msg = []
    for char in msg:
        trans_val = encryption_dictionary[char]
        encrypt_val = fmod(pow(trans_val,key[1]),key[0])
        encrypted_msg.append(int(encrypt_val))   
    return encrypted_msg


# Step 5
# Save the cipher, the private key, and the number n to txt files
cipher_to_save = open("cipher.txt","w")
line = str(encryptor(split_msg))
cipher_to_save.write(line)
cipher_to_save.close()

private_key_to_save = open("private_key.txt","w")
line = str(d)
private_key_to_save.write(line)
private_key_to_save.close()

n_to_save = open("n.txt","w")
line = str(n)
n_to_save.write(line)
n_to_save.close()


# Step 6
# Writing a function for the decryptor
def decryptor(key,a_cipher):    
    '''
    This function takes as input a cipher list, decrypts it using the private key, to backtranslate the
    cipher to its orginal message.
        Parameter: a_cipher, type = list
        Return value: decrypted_msg, type = string
    
    '''
    decrypted_msg = []
    for value in a_cipher:
        decrypt_val = value**key[1]%key[2]
        trans_char = decryption_dictionary[decrypt_val]
        decrypted_msg.append(trans_char)   
    decrypted_msg = "".join(decrypted_msg)
    return decrypted_msg


# Step 7
# Save the decrypted message to a file called "decrypted_message.txt"
decrypted_message = open("decrypted_message.txt","w")
line = str(decryptor(encryptor))
decrypted_message.write(line)
decrypted_message.close()


