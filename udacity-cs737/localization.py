# https://classroom.udacity.com/courses/cs373/lessons/48739381/concepts/487293510923

# Modify the empty list, p, so that it becomes a UNIFORM probability
# distribution over five grid cells, as expressed in a list of 
# five probabilities.
import numpy as np

world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1, 1]
p = []
n = 5
#Uniform distribution
for num in range(n):
    p.append(1./n)

pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append((hit * pHit + (1-hit) * pMiss) * p[i])
    s = sum(q, 0)
    for i in range(len(q)):
        q[i] = q[i] / s 
    return q

def move(p, U):
    q = []
    if U > 0:
        for i in range(len(p)):
            q.append(p[(i-U+1)%len(p)]*pUndershoot + p[(i-U)%len(p)]*pExact + p[(i-U-1)%len(p)]*pOvershoot)
    return q

    
for j in range(len(measurements)):
    p = sense(p, measurements[j])
    p = move(p, motions[j])
    
print p

