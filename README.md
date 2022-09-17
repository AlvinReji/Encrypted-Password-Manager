# Encrypted-Password-Manager
Password Managing Application using python, GUI using the tkinter library, and cryptography using the Fernet method
Passwords are encrypted using a Fernet key, meaning the only way to crack the password is with the provided key. Each key is actually composed of two smaller keys: a 128-bit AES encryption key and a 128-bit SHA256 HMAC signing key. The keys are held in a key repository that keystone passes to a library that handles the encryption and decryption of tokens.

Video of Password Manager: https://youtu.be/c3QbpydVhSU
