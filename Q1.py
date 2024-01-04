n=int(input("Enter n"))
i=int(input("Enter i"))
length=len(str(n))
if length<i:
    count=length
    firstDigit=str(n)
    firstDigit=int(firstDigit[0])+1
    power=10**(length-1)
    limit=firstDigit*power
    difference=limit-n-1
    count+=length*difference
    while count<i:
        n=limit
        firstDigit+=1
        if firstDigit==11:
            firstDigit=1
            power=10**length
            length+=1
            limit=power*firstDigit
        count+=power*length
        limit=firstDigit*power
    count-=power*length
    count+=length
    while count<i:
        n += 1
        count+=length
    index=count-i
    string=str(n)
    print(string[len(string)-index-1])
else:
    string=str(n)
    print(string[i-1])
