C = 0
A = 0
mS = str(input("Enter Multiplicant: "))
qS = str(input("Enter Multiplier: "))

M = int(mS,2)
Q = int(qS,2)
count = len(mS) if M>Q else len(qS)
n=count

print(M, Q, count)

while count > 0:
    if (Q & 1 == 1):
        temp = A + M
        C = temp >> n
        A = temp & ((1<<n)-1)
    new_Q = (Q >> 1) | ((A & 1) << (n - 1))
    new_A = (A >> 1) | (C << (n - 1))
    A = new_A
    Q = new_Q
    C = 0
    count -= 1
    
product = (A << n) | Q
print("Product in decimal = ", product) 
print("Product in binary = {:08b}".format(product))
