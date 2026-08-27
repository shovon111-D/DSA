def longest_palindrome(s: str) -> str:
    """Find the longest palindromic substring using center expansion."""
    if not s:
        return ""

    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    longest = ""
    for i in range(len(s)):
        # Odd-length palindromes (single character center)
        p1 = expand_around_center(i, i)
        # Even-length palindromes (between two characters)
        p2 = expand_around_center(i, i + 1)

        longest = max(longest, p1, p2, key=len)

    return longest


if __name__ == "__main__":
    
    s = "banana"

    print(longest_palindrome(s))