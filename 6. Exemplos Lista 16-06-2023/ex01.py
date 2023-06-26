A = [0] * 8
B = [0] * 8

import random
for i in range(8):
    A[i] = random.randrange(1, 100)
    
for i in range(8):
    B[i] = A[i] * 2
    
for i in range(8):
    print("A na pos", i, "= ", A[i], "\t e B = ", B[i])