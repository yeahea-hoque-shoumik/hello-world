def solve(s1, s2, s3):
    dp=[[None] * len(s2) for _ in range(len(s1))]
    def calc(i,j):
        if i == len(s1) and j == len(s2) and i + j == len(s3):
            return True
        if i+j>=len(s3):
            return False
        if i==len(s1) and j==len(s2):
            return False
        first = False
        second = False
        if i< len(s1) and s1[i] == s3[i + j]:
            first = calc(i + 1, j)
        if j< len(s2) and s2[j] == s3[i + j]:
            second = calc(i, j + 1)
        return first or second
    return calc(0,0)

def solve_dp(s1,s2,s3):
    pass


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbcaa"
    s3 = "aadbbcbcaca"
    print(solve(s1,s2,s3))