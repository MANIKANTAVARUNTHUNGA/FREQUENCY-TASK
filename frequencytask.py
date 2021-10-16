def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    A=list(d.items())
    l=len(A)
    for i in range(l-1):
        for j in range(i+1,l):
            if A[i][1]>A[j][1]:
                t=A[i]
                A[i]=A[j]
                A[j]=t
    A.reverse()
    sortdict=dict(A)
    print(sortdict)

most_frequent("Mississippi")
