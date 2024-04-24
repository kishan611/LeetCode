class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=""
        for i in s:
            if i.isalnum():
                if i.isalpha():
                    x+=i.lower()
                else:
                    x+=i
        if x==x[::-1]:
            return True
        return False