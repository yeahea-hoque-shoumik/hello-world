def circularArrayLoop( nums):
    n = len(nums)

    def nxt(i):
        return (i + nums[i]) % n

    for i in range(n):
        if nums[i] == 0:
            continue

        direction = nums[i] > 0
        slow, fast = i, i

        while True:
            # move slow 1 step
            ns = nxt(slow)
            if nums[ns] == 0 or (nums[ns] > 0) != direction or ns == slow:
                break

            # move fast 1 step
            nf = nxt(fast)
            if nums[nf] == 0 or (nums[nf] > 0) != direction or nf == fast:
                break

            # move fast 2nd step
            nf2 = nxt(nf)
            if nums[nf2] == 0 or (nums[nf2] > 0) != direction or nf2 == nf:
                break

            slow = ns
            fast = nf2

            if slow == fast:
                return True

        # Mark the whole path from i as visited (0)
        j = i
        while nums[j] != 0 and (nums[j] > 0) == direction:
            nj = nxt(j)
            nums[j] = 0
            j = nj

    return False

if __name__ == '__main__':
    nums=[1,1,1,1,1,1,1,1,1,-5]
    print(circularArrayLoop(nums))