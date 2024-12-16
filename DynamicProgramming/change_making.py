
def change_making(d, n):
    f = [0] * n

    for i in range(1, n):
        temp = []
        for j in range(len(d)):
            if i >= d[j]:
                temp.append(f[i - d[j]] + 1)
        f[i] = min(temp)
    return f[-1]


if __name__ == "__main__":
    d=[1,3,4,5,6]
    n=10
    print(change_making(d,n))
    
    d=[1,2,4,6,8,10,22,23]
    n=40
    print(change_making(d,n))

    d=[1,2,10,11,12,15,19,30]
    n=1900
    print(change_making(d,n))

