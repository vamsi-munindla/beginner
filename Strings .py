1. Reverse Words in a String
Given a string, reverse the order of words.

Input:
"the sky is blue"

ANS :
        s="the sky is blue"
	words= s.split()
	words.reverse()
	result=" ".join(words)
	print(result)

Complexities : 

Time Complexity = O(n)
Space Complexity = O(n)


2)  Check Anagram
Given two strings, determine if they are anagrams of each other.

Input:
s1 = "listen"
s2 = "silent"


Ans : 
s1 = "listen"
s2 = "silent"
if sorted(s1)==sorted(s2):
   print("Anagram")
else:
    print("Not an  anagram")

Output:
True

Complexities :
Time Complexity = O(n log n)
Space Complexity = O(n)


3) Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Input:
"Abcabcbb"

ANS : 
s = "abcabcbb"
max_length = 0

for i in range(len(s)):
    seen = set()
    for j in range(i, len(s)):
        if s[j] in seen:
            break
        seen.add(s[j])
    max_length = max(max_length, len(seen))

print(max_length)


Output:
3

Complexities :
Time Complexity = O(n²)
Space Complexity = O(n)


4) Longest Palindromic Substring
Given a string, return the longest palindromic substring.

Input:
"Babad"

ANS : 

s = "babad"

def expand(left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]

longest = ""

for i in range(len(s)):
    p1 = expand(i, i)
    p2 = expand(i, i+1)
    
    if len(p1) > len(longest):
        longest = p1
    if len(p2) > len(longest):
        longest = p2

print(longest)

Output:
"bab"

Complexities:
Time Complexity = O(n²)
Space Complexity = O(1)


5) Minimum Window Substring
Given two strings s and t, return the minimum window substring of s such that every character in t is included in the window.

Input:
s = "ADOBECODEBANC"
t = "ABC"

ANS :

from collections import Counter

s = "ADOBECODEBANC"
t = "ABC"

need = Counter(t)
window = {}
have = 0
need_count = len(need)
left = 0
min_len = float("inf")
result = ""
for right in range(len(s)):
    char = s[right]
    window[char] = window.get(char, 0) + 1
    if char in need and window[char] == need[char]:
        have += 1
    while have == need_count:
        if (right - left + 1) < min_len:
            min_len = right - left + 1
            result = s[left:right+1]
     window[s[left]] -= 1
        if s[left] in need and window[s[left]] < need[s[left]]:
            have -= 1
        left += 1
print(result)


Output:
"BANC

Complexities :
Time Complexity = O(n)
Space Complexity = O(n)
