# Restoring Division Algorithm

# Take user inputs
dividend = int(input("Enter Dividend (Q): "))
divisor = int(input("Enter Divisor (M): "))

# Determine the number of bits needed based on dividend
n = dividend.bit_length()

# Initialize registers
A = 0
Q = dividend
M = divisor

print(f"\nInitial values:\nA = {A}, Q = {Q}, M = {M}, n = {n}")

for step in range(n):
    print(f"\nStep {step + 1}:")

    # Shift A and Q left together
    A = (A << 1) | ((Q >> (n - 1)) & 1)
    Q = (Q << 1) & ((1 << n) - 1)  # keep Q within n bits

    print(f"After shift left: A = {A}, Q = {Q}")

    # Subtract M from A
    A = A - M
    print(f"After A = A - M: A = {A}")

    if A < 0:
        # Unsuccessful: Q0 = 0 and restore A
        Q = Q & ~1  # set LSB to 0
        A = A + M   # restore A
        print(f"A < 0 → Restore A = A + M: A = {A}, Q0 = 0")
    else:
        # Successful: Q0 = 1
        Q = Q | 1
        print(f"A >= 0 → Q0 = 1: Q = {Q}")

# Final output
print("\nFinal Result:")
print(f"Quotient (Q): {Q} ({format(Q, f'0{n}b')})")
print(f"Remainder (A): {A} ({format(A, f'0{n}b')})")
