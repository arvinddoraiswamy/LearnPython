n1 = 10
print("Left shift by 2 bits should be number * (2)^2. Python expands the size automatically.")
print('Original:', n1, bin(n1), 'Shifted:', n1<<2, bin(n1<<2))

n1 = 10
print("Right shift by 2 bits should be number / (2)^2. Size reduced as needed.")
print('Original:', n1, bin(n1), 'Shifted:', n1>>2, bin(n1>>2))

n1 = 10
n2 = 5
print("Binary And")
print("Original:", n1, bin(n1), n2, bin(n2), "Anded", n1 & n2)

n1 = 10
n2 = 5
print("Binary Or")
print("Original:", n1, bin(n1), n2, bin(n2), "Ored", n1 | n2)

n1 = 10
n2 = 6
print("Binary XOR")
print("Original:", n1, bin(n1), n2, bin(n2), "XOR", n1 ^ n2)

n1 = 60
print("Two's complement. One's complement is transparently calculated")
# https://python-forum.io/Thread-Find-the-complement-of-a-number?pid=8593#pid8593
print("Original:", n1, bin(n1), "Two's complement is -(num + 1)", ~n1, bin(~n1))
