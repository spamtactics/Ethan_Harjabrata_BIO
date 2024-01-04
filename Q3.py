from functools import lru_cache
lru_cache(maxsize=None)
def findCombinations(goalScore, previousAscii, currentScore):
    #essentially string combinatorics up to the letter itself
    if goalScore==currentScore:
        return 1
    total=0
    for i in range(65,91):
        if i==previousAscii:
            continue
        resultScore=currentScore+i-64
        if resultScore> goalScore:
            break
        total+=findCombinations(goalScore, i, resultScore)
    return total
word=input("Enter the string")
length=len(word)
score=0
for i in range(length):
    score+=ord(word[i])-64
baseLength=0
count=0
currentScore=0
while baseLength<length:
    limitAscii=ord(word[baseLength])
    for i in range(65, limitAscii):
        nextScore=currentScore+i-64
        count+=findCombinations(score, i,nextScore)
    currentScore+=limitAscii-64
    baseLength+=1
print(count+1)