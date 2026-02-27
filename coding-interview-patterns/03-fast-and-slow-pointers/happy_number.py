def calculate_square_of_digits(n):
    ans=0
    while n>0:
        digit=n%10
        n=n//10
        ans+=(digit*digit)
    return ans
def is_happy_number(n):
    slow=calculate_square_of_digits(n)
    fast = calculate_square_of_digits(calculate_square_of_digits(n))
    while slow!=fast:
        if slow==1 or fast==1:
            return True
        slow=calculate_square_of_digits(slow)
        fast=calculate_square_of_digits(calculate_square_of_digits(fast))
    return False


if __name__ == '__main__':
    for i in range(1,100):
        print(i," is happy: ",is_happy_number(i))


    # replace the number with the sum of the squares of its digits
    # repeat the process until the sum = 1 (return true)or
    # repeating process creates a cycle(return false)