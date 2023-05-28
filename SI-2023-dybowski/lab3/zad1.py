# w0 <= 0
# w0 + w2 <= 0 
# w0 + w1 <= 0
# w0 + w1 + w2 > 0

w0, w1, w2 = 0,0,0
def foo():
    results = []
    for i in range(0, -20, -1):
        w0 = i/10
        for j in range(-20, 20, 1):
            w1 = j/10
            for k in range(-20, 20, 1):
                w2 = k/10
                if w0 + w2 <= 0:
                    if w0 + w1 <= 0:
                        if w0 + w1 + w2 > 0:
                            results.append([w0, w1, w2])
    return results

# w0 > 0
# w0 + w1 <= 0

def foo2():
    results = []
    for i in range(0, 20):
        w0 = i/10
        for j in range(-20, 20, 1):
            w1 = j/10
            if w0 + w1 <= 0:
                results.append([w0, w1])
    return results


print(foo2())