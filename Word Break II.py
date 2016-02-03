class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        def helper(s, start, end, wordDict, currentRes, res):
        	if end >= len(s):
        		res.append(currentRes)
        	if s[start:end] in wordDict:
        		currentRes.append(s[start:end])
        		helper(s, start+1, start+2, wordDict, currentRes, res)
        	else:
        		helper(s, start, end+1, wordDict, currentRes, res)
        	return res


        res = []
        helper(s, 0, 1, wordDict, [], res)

a = Solution()
print a.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])