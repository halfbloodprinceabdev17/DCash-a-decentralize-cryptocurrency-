import hashlib
import rsa

# Generate public and private keys
def send(message):
        (pubkey, privkey) = rsa.newkeys(512)
# Sender signs the message with their private key
        signature = rsa.sign(message.encode('utf-8'), privkey, 'SHA-256')
        return signature,pubkey
# Receiver verifies the signature with the sender's public key
def recieve(message,signature,pubkey):
        try:
            rsa.verify(message.encode('utf-8'), signature, pubkey)
            print("Signature is valid. Message is from a trusted source.")
        except:
            print("Signature is invalid. Message may have been tampered with.")     