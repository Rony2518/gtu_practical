import numpy as np
rn = np.random.rand(3, 3)
for i in  rn:
    for j in i:
        print(f"{j:.2f}",end=' ')
    print()
        

rn = np.random.randn(3, 3)
np.set_printoptions(precision=2)
print(rn)