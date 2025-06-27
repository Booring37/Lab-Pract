while True:
    M = int(input("Multiplicand between -8 to 7 : "))
    if -8<= M <= 7:
        break
    else:
        print("Invalid Input")

while True:
    Q = int(input("Multiplier between -8 to 7 : "))
    if -8<= Q <= 7:
        break
    else:
            print("Invalid Input")

A = 0
Q_1 = 0
count = 4 # bits

# convert to 4-bit two's complement if negative
if M <= 0:
     M = (1 << 4) + M #2's complement
     
if Q <= 0:
     Q = (1 << 4) + Q

print(f"\nInitial -> A: {A:04b}, Q: {Q:04b}, Q_1: {Q_1:04b}, M: {M:04b}, Count: {count}")

# Main Loop
while count > 0:
    Q0 = Q & 1

    #  case 01: A = A + M
    if Q0 == 0 and Q_1 == 1:
        A = A + M
        A = A & 0b1111 #Keep only 4 bits
        print(f"A = A + M: {A:04b}") 

    #  case 10: A = A + M
    elif Q0 == 1 and Q_1 == 0:
        # M_neg = (~M+1) & 0b1111
        # A = A + M_neg # same thing as A = A - M
        # A = A & 0b1111 #Keep only 4 bits
        A = A - M
        A = A & 0b1111 #Keep only 4 bits
        print(f"A = A - M: {A:04b}")
    
    # Arithemetic Right Shift on A Q Q-1
    combined = (A << 5) | (Q << 1) | Q_1
    msb = (combined >> 8) & 1
    combined = (combined >> 1) | (msb << 8)

    A = (combined >> 5) & 0b1111
    Q = (combined >> 1) & 0b1111
    Q_1 = (combined & 1) 

    count -= 1

    print(f"\nAfter shift -> A: {A:04b}, Q: {Q:04b}, Q_1: {Q_1:04b}, M: {M:04b}, Count: {count}")

product = (A << 4) | (Q)

if product & (1 << 7):
    result = product - (1 << 8)
else:
     result = product

print(f"\nFinal Binary Result: {product:08b}")
print(f"\nFinal Decimal Result: {result}")
