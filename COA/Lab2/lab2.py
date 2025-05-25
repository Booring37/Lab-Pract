def binAdd(a, b, cin):
    s = a ^b^cin
    cout = (a&b) | (a&cin) | (b&cin)
    return s, cout

def comp1(num):
    return ''.join('0' if bit == '1' else '1' for bit in num)


def comp2(num):
    com1 = (comp1(num))
    comp = com1[::-1]
    cComp = 1
    rComp = ''
    for i in range(4):
        sComp, cComp = binAdd(int(comp[i]),0,cComp)
        rComp=rComp+str(sComp)
    
    return rComp[::-1]


Num1 = input("Enter 1st 4-bit number: ")
Num2 = input("Enter 2nd 4-bit number: ")
carry = 0 

if len(Num1) != 4 or len(Num2) != 4 or not all(c in '01' for c in Num1 + Num2):
    print("Invalid Response")
else:
    N1 = Num1
    N2 = comp2(Num2)

    N1 = N1[::-1]
    N2 = N2[::-1]

    
    result = ['0']*4 
    carry = int(carry)

    for i in range(4):
        s, carry = binAdd(int(N1[i]), int(N2[i]), carry)
        result[i] = str(s)
    result = result[::-1]
    if carry == 1:
        print("Difference =", ''.join(result))
    else:
        Result =''.join(result)
        r = comp2(Result)
        print("Difference = -", ''.join(r))
