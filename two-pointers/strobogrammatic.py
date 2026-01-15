# Time: O(n) where n is the length of input string
# Space: O(1) because fixed-size map is required to store the strobogrammatic digit mappings, regardless of the input size.

def is_strobogrammatic(num):
    mapping = {
        '0' : '0',
        '1' : '1',
        '8' : '8',
        '6' : '9',
        '9' : '6'
    }

    left, right = 0, len(num) - 1

    while left <= right:
        if num[left] not in mapping or mapping[num[left]] != num[right]:
            return False

        left += 1
        right -= 1

    return True


def main():
    test_cases = [
        "609",   
        "88",   
        "962",  
        "101",  
        "123"   
    ]

    for i, num in enumerate(test_cases):
        print(i + 1, ".\tnum: ", num, sep="")
        print("\n\tIs strobogrammatic: ", is_strobogrammatic(num), sep="")
        print("-" * 50)

if __name__ == "__main__":
    main()