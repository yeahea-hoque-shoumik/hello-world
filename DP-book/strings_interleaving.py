def solve(s1, s2, s3):
    i,j=0,0
    for k in range(len(s3)):
        if i< len(s1) and s1[i]==s3[k]:
            i+=1
        elif j< len(s2)  and  s2[j]==s3[k]:
            j+=1
    if i==len(s1) and j==len(s2):
        return True
    else: return False


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(solve(s1,s2,s3))