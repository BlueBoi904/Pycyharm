"""

Givalueen a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitivaluee, for example, "Aa" is not considered a palindrome here.

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

"""

from collections import Counter


def longest_palindrome(s):
    c = Counter(s)
    res = 0
    k = 0
    for i, j in c.items():
        print(i, j)
        if j % 2 == 0:
            res += j
        else:
            res += j - 1
            k += 1
    if k >= 1:
        res += 1
    return res


longest_palindrome("dccaccd")
