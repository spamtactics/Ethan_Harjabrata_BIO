def E(index):
    return 2*index
def O(index):
    return 2*index-1
def T(index):
    num=1
    value=0
    while value<index:
        value+=num
        num+=1
    num-=1
    return num


d=input("Enter d")
i=int(input("Enter i"))
depth=0
while depth<3:
    if depth%2==0:
        rightLetter=d[1]
        #check right letter
        if rightLetter=="E":
            i=E(i)
        elif rightLetter=="O":
            i=O(i)
        else:
            i=T(i)
    else:
        leftLetter=d[0]
        #check left letter
        if leftLetter=="E":
            i=E(i)
        elif leftLetter=="O":
            i=O(i)
        else:
            i=T(i)
    depth+=1
print(i)