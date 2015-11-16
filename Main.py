import OrdInsSel, OrdBurbQuicksort, OrdMezcla

from random import *
import time

l=[]

for i in range(1000):
    l.append(randrange(0,200000))
start_time = time.time()
OrdInsSel.ordIns(l)
end_time = time.time() - start_time
print end_time

l1=[]

for i in range(1000):
    l1.append(randrange(0,200000))
start_time = time.time()
OrdInsSel.ordSel(l1)
end_time = time.time() - start_time
print end_time

l2=[]

for i in range(1000):
    l2.append(randrange(0,200000))
start_time = time.time()
OrdBurbQuicksort.ordBurbuja(l2)
end_time = time.time() - start_time
print end_time

l3=[]

for i in range(1000):
    l3.append(randrange(0,200000))
start_time = time.time()
OrdBurbQuicksort.quickSort(l3,0,len(l3)-1)
end_time = time.time() - start_time
print end_time

l4=[]

for i in range(1000):
    l4.append(randrange(0,200000))
start_time = time.time()
OrdMezcla.OrdenxMezcla(l4)
end_time = time.time() - start_time
print end_time
