import string
import random

if __name__ == '__main__':

    g1 = string.ascii_lowercase
    # print(g1)

    g2 = string.ascii_uppercase
    # print(g2)

    g3 = string.digits
    # print(g3)

    g4 = string.punctuation
    # print(g4)

    pwd_len= int(input("Enter your passward length: "))
    
    p=[]
    p.extend(list(g1))
    p.extend(list(g2))
    p.extend(list(g3))
    p.extend(list(g4))
    # print(p)

    random.shuffle(p)

    print("Your Passward: ")
    print("".join(p[0:pwd_len]))


