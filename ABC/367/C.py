def solve():
    N, K = map(int, input().split())
    R = list(map(int, input().split()))
    final_sum = 0
    for i in R:
        final_sum += i
        
    sum = N
    curr_R = [1 for i in range(N)]
    while sum < final_sum:
        idx = -1
        if sum % K == 0:
            print(" ".join(map(str, curr_R)))
        while curr_R[idx] == R[idx]:
            sum -= R[idx] - 1
            curr_R[idx] = 1
            idx -= 1
        curr_R[idx] += 1
        sum += 1
    
    if sum % K == 0:
        print(" ".join(map(str, curr_R)))

if __name__ == "__main__":
    solve()