# Time O(n^2)
# Space O(1)
def three_sum(nums):
    nums.sort()
    results = []
    n = len(nums)

    for i in range(n-2):
        if nums[i] > 0: 
            break
        
        if i == 0 or nums[i] != nums[i-1]:
            low, high = i+1, n-1

            while low < high:
                sum = nums[i] + nums[low] + nums[high]
                if sum < 0:
                    low += 1
                elif sum > 0:
                    high -= 1
                else:
                    results.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1

                    if low < high and nums[low] == nums[low - 1]:
                        low += 1
                    if low < high and nums[high] == nums[high + 1]:
                        high -= 1
        
    return results


def main():
    test_cases = [
        [-1, 0, 1, 2, -1, -4],
        [1, 2, 3, 4, 5],
        [0, 0, 0, 0],
        [-4, -1, -1, 0, 1, 2, 2],
        [-10, -7, -3, -1, 0, 3, 7, 10],
        [-3, -5, -7, -9]
    ]

    for i, num in enumerate(test_cases):
        three_sum_result = three_sum(num)
        print(f"Test Case {i + 1}: Input: {num} -> Output: {three_sum_result}")


if __name__ == "__main__":
    main()








                    

    
