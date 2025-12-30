# Space O(1)
# Time O(n)

def isPalindrome(s: str) -> bool:
    p1 = 0
    p2 = len(s) - 1

    while p1 < p2:
        while(p1 < p2 and not s[p1].isalnum()):
            p1 += 1
        
        while(p1 < p2 and not s[p2].isalnum()):
            p2 -= 1
        
        if(s[p1].lower() != s[p2].lower()):
            return False
            
        p1 += 1
        p2 -= 1

    return True


def main():
    # Test cases
    test_cases = [
        "A man, a plan, a canal: Panama",  # True
        "race a car",                      # False
        " ",                               # True
        "A",                               # True
        "0P",                              # False
        "A man, a plan, a canal: Panama",  # True
        "A1B2 2B1 A"                       # True
    ]

    for test in test_cases:
        print(f'"{test}" -> {isPalindrome(test)}')

if __name__ == "__main__":
    main()