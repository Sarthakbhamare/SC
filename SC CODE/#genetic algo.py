#genetic algo 
import random

T = "HELLO"
C = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
P = 20
M = 0.1

pop = ["".join(random.choice(C) for _ in range(len(T))) for _ in range(P)]
g = 0

while True:
    pop = sorted(pop, key=lambda s: sum(s[i] == T[i] for i in range(len(T))), reverse=True)
    b = pop[0]
    print(g, b)
    if b == T: 
        break
    new = [b]
    while len(new) < P:
        a = random.choice(pop[:5])
        d = list(a)
        for i in range(len(d)):
            if random.random() < M: 
                d[i] = random.choice(C)
        new.append("".join(d))
    pop = new
    g += 1
