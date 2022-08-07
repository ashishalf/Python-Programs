import random 

def otpgenerate():
    otp=""
    for i in range(4):
        otp=otp+str(random.randint(1,9))

    print("Your One Time Password: ",otp)

otpgenerate()