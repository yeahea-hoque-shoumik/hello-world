def valid_palindrome(s):
    start,end=0,len(s)-1
    ans=False
    while start<end:
        if s[start]!=s[end]:
            break
        start+=1
        end-=1
    if abs(start-end)<=1:
        return True
    if s[start+1]==s[end]:
        start+=1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        ans=True
    elif s[start]==s[end-1]:
        end-=1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        ans= True
    return False
if __name__ == '__main__':
    s = "aguokepatgbnvfqmgml cupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuc u lmgmqfvnbgtapekouga"
    print(valid_palindrome(s))