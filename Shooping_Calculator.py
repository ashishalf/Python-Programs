sum=0
while(True):
    print("\nIf you want to exit then press double 'Enter'")

    item=input("\nItem: ")
    price=input("\nAmount: ")

    if(item!=""):
        if(price!=""):
            sum=sum+int(price)
    else:
        print("\nTotal Amount: \n",sum)
        break