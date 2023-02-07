a = [1,2,3,4,5,6,7]
n = 7
a2 = [2,3,5,1,4]
n2 = 5


def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

# findZigZagSequence(a, n)

def test(a, n):
    a.sort()
    mid = int((n+1)/2) - 1
    print(mid)

    a[mid], a[n-1] = a[n-1], a[mid]
    print(a)

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[ed], a[st] = a[st], a[ed]
        st = st + 1
        ed = ed - 1
    
    print(a)


test(a,n)
test(a2,n2)

