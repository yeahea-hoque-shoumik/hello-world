def reverse_words(s:str)->str:
    result = s.split()
    left, right = 0, len(result) - 1

    while left <= right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1

    return " ".join(result)

# fllow-up : how to solve it in-place with O(1) extra space, If the string data type is mutable in your language,
# Remove extra spaces (leading, trailing, multiple spaces → single space)
# Reverse the whole string
# Reverse each word individually

if __name__ == '__main__':
    s = "a good   example"
    print(reverse_words(s))