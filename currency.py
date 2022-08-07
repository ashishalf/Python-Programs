with open('cd.txt') as f:
    lines = f.readlines()
    print(lines)
curDict = {}
for line in lines:
    parsed = line.split("\t")
    curDict[parsed[0]] = parsed[1]
amount = int(input("Enter your amount:\n"))
print("Enter the name of currency you want to convert this amount to: \n")
[print(item) for item in curDict.keys()]
currency = input("Please enter one of these values: \n")
print(f"{amount} INR is equal to {amount*float(curDict[currency])} {currency}")
