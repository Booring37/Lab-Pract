def binAdd(a,b,cin):
    s = a^b^cin
    cout = (a&b)|(a&cin)|(b&cin)
    return s,cout
 
Num1 = (input("1st 4bit number"))
Num2 = (input("2st 4bit number"))
carry = (input("Carry"))
 
if len(Num1) != 4 or len(Num2) != 4 or len(carry) != 1 or not all(c in '01' for c in Num1+Num2+carry):
    print("Invalid Response")
 
else:
    N1=[0]*4
    N2=[0]*4
    N1,N2= Num1[::-1],Num2[::-1]
    print (N1 , N2)
 
    result=['0']*4
    print(type(result[0]))
    for i in range(4):
        s,cin = binAdd(int(N1[i]),int(N2[i]),int(cin))
        print(s, carry)
        result.append(str(s))
 
    print("".join(result[::-1]))
    print("CarryOut =", carry)
