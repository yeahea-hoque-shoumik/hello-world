def valid_palindrome(text):
    left,right=0,len(text)-1
    while(left<right):
        if not text[left].isalnum():
            left+=1
        elif not text[right].isalnum():
            right-=1
        elif text[left].lower() !=text[right].lower():
            return False
        else:
            left+=1
            right-=1
    return True



if __name__ == '__main__':
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "1A@2!3 23!2@a1",
        "No 'x' in Nixon",
        "12321",
    ]
    for text in test_cases:
        print(valid_palindrome(text))