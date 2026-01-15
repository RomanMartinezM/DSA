def find_duplicate_number(nums):
    fast = slow = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return fast
    
def main():
    test_cases =[
        [1, 3, 2, 3, 5, 4], 
        [2, 4, 5, 4, 1, 3], 
        [1, 6, 3, 5, 1, 2, 7, 4], 
        [1, 2, 2, 4, 3], 
        [3, 1, 3, 5, 6, 4, 2]
    ]

    for i in range(len(test_cases)):
        print(i + 1, ".\tnums = ", test_cases[i], sep="")
        print("\tDuplicate number = ", find_duplicate_number(test_cases[i]), sep="")
        print("-" * 100)

if __name__ == "__main__":
    main()