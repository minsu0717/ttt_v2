from ast import Pass
from argon2 import PasswordHasher
from argon2 import PasswordHasher

def check_password(hashed,password):
    return PasswordHasher().verify(hashed,password)