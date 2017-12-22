# -*- coding: utf-8 -*-
import math
def IntegerSquaring(Input_integer):
    IntegerList=list(map(int,list(str(Input_integer))))
    IntegerList.reverse()
    IntegerLength=len(IntegerList)
    I=[]
    d=[]
    UHL=0
    UHLPrev=0
    for k in range((2*IntegerLength-2)+1):
        if k<IntegerLength:
            I=list(range(int(math.ceil(k/2))))
        else:
            I=list(range((k//2)+1,IntegerLength))
        for i in I:
            UHL=UHL+IntegerList[i]*IntegerList[k-i]
        if (k%2)==0:
            UHL=2*UHL+IntegerList[int(k/2)]**2
        else:
            UHL=2*UHL
        UHL=UHL+UHLPrev
        L=UHL%10
        U=UHL//100
        H=(UHL-U*100-L)//10
        d.append(L)
        L=int(H)
        H=int(U)
        U=0
        UHLPrev=H*10+L
        UHL=0

    if L!=0:
        d.append(L)
    d.reverse()
    d=list(map(str,d))
    return "".join(d)


if __name__=="__main__":
    Result=IntegerSquaring(4)
    print(Result)






