"""
https://en.wikipedia.org/wiki/External_sorting
https://en.wikipedia.org/wiki/K-way_merge_algorithm

"""
import numpy as np

L=2

for i in range(8**L):
    f=open("chunk"+str(i).zfill(L)+".csv","w")
    k=0
    while True:
        n = np.random.randn(3)
        ok = f.write(";".join([str(j) for j in n])+"\n")
        k=k+1
        if k==64**L:
            f.close()
            break
