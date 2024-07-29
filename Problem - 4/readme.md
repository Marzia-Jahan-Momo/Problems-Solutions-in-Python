## Problem - 4: Longest Common Prefix ##

Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

---
## Solution - 4: Longest Common Prefix ##
``` python
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]
    return shortest

print(longest_common_prefix(["flower", "flow", "flowering"]))

```