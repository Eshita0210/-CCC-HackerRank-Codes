MOD = 1000000007

def num_decodings(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    if n == 1:
        return 1
    count = [0] * (n + 1)
    count[0] = count[1] = 1
    for i in range(2, n + 1):
        if s[i - 1] >= '0':
            count[i] = count[i - 1]
        if s[i - 2] == '0' or s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] < '6'):
            count[i] = (count[i] + count[i - 2]) % MOD
    return count[n]

s = input()
print(num_decodings(s))
