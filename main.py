# -*- coding: utf-8 -*-
import math
import doctest

#By : Sepand Haghighi & Mohammad Abassi

def IntegerSquaring(Input_integer,Base=10):
    '''
     Integer Squaring Algorithm
     Book : Cryptographic Engineering (Serdar S¨ uer Erdem, Tuˇ grul Yanık, and C ¸ etin Kaya Koc)
     Chapter : 5
     Page : 80
    :param Input_integer : Input Integer as string with space separation between digit "0 11 12" in base 13
    :type Input_integer : str
    '''
    try:
        IntegerList=list(map(int,list(Input_integer.split(" "))))
        for number in IntegerList:
            if number>Base-1:
                raise Exception("[Erro] Bad Number In This Base")
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
            L=UHL%Base
            U=UHL//(Base**2)
            H=(UHL-U*(Base**2)-L)//Base
            d.append(L)
            L=H
            H=U
            U=0
            UHLPrev=H*Base+L
            UHL=0
        if L!=0:
            d.append(L)
        d.reverse()
        d=list(map(str,d))
        return " ".join(d)
    except Exception as e:
        print(str(e))
        return 0

def IntegerMultiplication(Input_integer_1,Input_integer_2,Base=10):
    '''
    Integer Squaring Algorithm
    Book : Cryptographic Engineering (Serdar S¨ uer Erdem, Tuˇ grul Yanık, and C ¸ etin Kaya Koc)
    Chapter : 5
    Page : 79
    :param Input_integer_1 : Input Integer as string with space separation between digit "0 11 12" in base 13
    :param Input_integer_2 : Input Integer as string with space separation between digit "0 11 12" in base 13
    :type Input_integer_1 : str
    :type Input_integer_2 : str
    '''
    IntegerList1 = list(map(int, list(Input_integer_1.split(" "))))
    IntegerList2 = list(map(int, list(Input_integer_2.split(" "))))
    IntegerList1.reverse()
    IntegerList2.reverse()
    IntegerLength = max(len(IntegerList1),len(IntegerList2))
    IntegerList1.extend([0]*(IntegerLength-len(IntegerList1)))
    IntegerList2.extend([0] * (IntegerLength - len(IntegerList2)))
    I = []
    UHL=0
    d=[]
    for k in range((2*IntegerLength-2)+1):
        if k<IntegerLength:
            I = list(range(k+1))
        else:
            I=list(range(k-IntegerLength+1,IntegerLength))
        for i in I:
            UHL = UHL + IntegerList1[i] * IntegerList2[k - i]
        L = UHL % Base
        U = UHL // Base**2
        H = (UHL - U * (Base**2) - L) // Base
        d.append(L)
        L = H
        H = U
        U = 0
        UHL = H*Base+L
    if L!=0:
        d.append(L)
    d.reverse()
    d = list(map(str, d))
    return " ".join(d)







if __name__=="__main__":
    doctest.testfile("test.py", optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)






