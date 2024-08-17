def solve():
    s = input()
    while s[-1] == '0' or s[-1] == '.':
        if s[-1] == '0':
            s = s[:-1]
        elif s[-1] == '.':
            s = s[:-1]
            break
    print(s) 
        

if __name__ == "__main__":
    solve()