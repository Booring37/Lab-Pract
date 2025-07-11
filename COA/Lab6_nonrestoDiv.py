# Non-Restoring Division Algorithm

# Take user inputs
dividend = int(input("Enter Dividend (Q): "))
divisor = int(input("Enter Divisor (M): "))

# Determine number of bits from dividend
n = dividend.bit_length()

# Initialize
A = 0
Q = dividend
M = divisor
operation = "sub"  # start with subtraction

print(f"\nInitial Values:\nA = {A}, Q = {Q}, M = {M}, n = {n}")

for step in range(n):
    print(f"\nStep {step + 1}:")

    # Step 1: Left shift A and Q together
    A = (A << 1) | ((Q >> (n - 1)) & 1)
    Q = (Q << 1) & ((1 << n) - 1)  # keep Q within n bits
    print(f"After shift left: A = {A}, Q = {Q}")

    # Step 2: Perform subtraction or addition
    if operation == "sub":
        A = A - M
        print(f"Operation: A = A - M → A = {A}")
    else:
        A = A + M
        print(f"Operation: A = A + M → A = {A}")

    # Step 3: Check result and decide next operation
    if A < 0:
        Q = Q & ~1  # Q0 = 0
        operation = "add"
        print(f"A < 0 → Q0 = 0, Next Operation = ADD")
    else:
        Q = Q | 1   # Q0 = 1
        operation = "sub"
        print(f"A >= 0 → Q0 = 1, Next Operation = SUB")

# Final correction if remainder A is negative
if A < 0:
    A = A + M
    print(f"\nFinal correction (A was negative): A = A + M → A = {A}")

# Final output
print("\nFinal Result:")
print(f"Quotient (Q): {Q} ({format(Q, f'0{n}b')})")
print(f"Remainder (A): {A} ({format(A, f'0{n}b')})")
