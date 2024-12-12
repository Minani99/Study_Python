def fac(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output


def fac2(n):
    if n==0:
        return 1
    else:
        return n*fac2(n-1)


print(fac(100))
