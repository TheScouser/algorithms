def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        chars = {}
        longest = 0
        i = 0
        for j in range(len(s)):
            if chars.get(s[j],None) != None:
                i = max(chars[s[j]],i)
            longest = max(longest,j - i + 1)
            chars[s[j]] = j + 1
        return longest
            

print lengthOfLongestSubstring("abcabcbb")