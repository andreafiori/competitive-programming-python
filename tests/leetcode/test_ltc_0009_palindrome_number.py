from app.leetcode.ltc_0009_palindrome_number import PalindromeNumber

class TestPalindromeNumber:
    def test_is_palindrome(self):
        pn = PalindromeNumber()
        assert pn.isPalindrome(121) == True
        assert pn.isPalindrome(-121) == False
        assert pn.isPalindrome(10) == False
        assert pn.isPalindrome(12321) == True
        assert pn.isPalindrome(0) == True