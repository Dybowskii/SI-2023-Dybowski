# w0 <= 0
# w0 + w2 <= 0 
# w0 + w1 <= 0
# w0 + w1 + w2 > 0


w0, w1, w2 = 0,0,0
def foo():
    for i in range(0, -20, -1):
        w0 = i/10
        for j in range(-20, 20, 1):
            w1 = j/10
            for k in range(-20, 20, 1):
                w2 = k/10
                print(w0, w1, w2)
                if w0 + w2 <= 0:
                    if w0 + w1 <= 0:
                        if w0 + w1 + w2 > 0:
                            return w0, w1, w2


print(foo())
