#backpropogation 
import math

# sigmoid
def s(x): 
    return 1 / (1 + math.exp(-x))

# sigmoid derivative
def sd(y): 
    return y * (1 - y)

X = [(0,0), (0,1), (1,0), (1,1)]
T = [0,1,1,0]

w1, w2 = 0.5, -0.5   # simple weights
lr = 0.5             # learning rate

print("x1 x2 exp pred")

for (a, b), t in zip(X, T):
    # forward pass
    z = a*w1 + b*w2
    o = s(z)
    print(a, b, " ", t, " ", round(o,4))

    # backprop update
    e = t - o
    d = e * sd(o)

    w1 += lr * d * a
    w2 += lr * d * b
