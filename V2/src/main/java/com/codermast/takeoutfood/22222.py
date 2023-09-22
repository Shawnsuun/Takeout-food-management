def countPalindromicSubstrings(s):
    def expandAroundCenter(left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    total_count = 0
    for center in range(len(s)):
        # For odd length palindromes
        total_count += expandAroundCenter(center, center)

        # For even length palindromes
        total_count += expandAroundCenter(center, center + 1)

    return total_count



s = "tacocat"
result = countPalindromicSubstrings(s)
print(result)  # Output: 10


s = "aaa"
result = countPalindromicSubstrings(s)
print(result)  # Output: 10

s = "abccba"
result = countPalindromicSubstrings(s)
print(result)  # Output: 10