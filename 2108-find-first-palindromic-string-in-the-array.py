class Solution:
	def firstPalindrome(self, words) -> str:
		for each in words:
			if each == each[::-1]:
				return each
		return ""

words = ["abc","car","ada","racecar","cool"]
S = Solution()
print(S.firstPalindrome(words))
