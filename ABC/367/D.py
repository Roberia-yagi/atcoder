def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    len_from_0 = [0 for i in range(N)]
    mod_dict = {}
    for i in range(N):
        if i == 0:
            len_from_0[i] = A[i]
        else:
            len_from_0[i] = A[i] + len_from_0[i-1]
        mod_M = len_from_0[i] % M
        mod_dict[mod_M] = mod_dict.get(mod_M, 0) + 1

    ans = 0
    for mod_M, count in mod_dict.items():
        if mod_M == 0:
            ans += count
        print(f'mod_M: {mod_M}, count: {count}')
        ans += count * (count - 1) // 2
    
    print(ans)

# 2 1 4 3
# 2 3 7 10
# 2 0 1 1
        
            

if __name__ == "__main__":
    solve()