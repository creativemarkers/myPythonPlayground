import os
import random

# def storeSalt(salt):


def hasher(pw, salt=None):

    if salt == None:
        salt = saltGenerator()
        #storeSalt()



    fCharArr = [0] * len(pw)
    for i in range(1,100):
        for i in range(len(pw)):

            aChar = ord(pw[i])
            fCharArr[i] += aChar
            
            # print(aChar)

    for i in range(len(fCharArr)):

        newChar = chr(fCharArr[i])
        newChar = ord(newChar)
        newChar //= len(pw)+8
        newChar = chr(newChar)
        newChar = (ord(newChar) // len(pw)) * salt
        newChar = chr(newChar)
        newChar = ord(newChar)
        fCharArr[i] = newChar

    for n in fCharArr:
        print(chr(n))

    return print(fCharArr)



def saltGenerator():

    salt = random.uniform(0.000,1)
    pepper = random.randint(1,10)
    salt += pepper
    salt = int(salt)
    return salt

def main():

    hasher("yoQu2coBeLl")

    pw = "yoQu2coBeLl"
    for char in pw:
        
        print(ord(char))
    
if __name__ == "__main__":
    main()
 