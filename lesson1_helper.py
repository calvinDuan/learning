import copy
def cryptarSeparate(s):
    temp = s.split(" ")
    num1 = temp[0]
    num2 = temp[2]
    num3 = temp[4]
    return([num1,num2,num3])

def cryptarWord2Num(L,key):
    nums = [0] * 3
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] in key:
                temp = key.index(L[i][j])
                nums[i] += temp*10**(len(L[i])-j-1)
            else:
                return False
    return nums

def wordCreatable(word,hand):
    temp = copy.copy(hand)
    for c in word:
        if c not in temp:
            return False
        else:
            temp.remove(c)
    return True

#print(wordCreatable("zzy",["x","y","z"]))
#print(wordCreatable("bx",["a","b","c"]))

#print(cryptarWord2Num(["SEND","MORE","MONEY"],"OMY--ENDRS"))