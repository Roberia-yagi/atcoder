def solve():
    A = list(map(int, input().split()))
    shout = A[0]
    sleep = A[1]
    wake = A[2]
    if sleep < wake:
        if shout < sleep or wake < shout:
            print('Yes')
        else:
            print('No')

    else:
        if sleep < shout or shout < wake:
            print('No')
        else:
            print('Yes')

if __name__ == "__main__":
    solve()