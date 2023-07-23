# 회문
"""
import re
def isPalindrome(s) -> bool:
    #영문자를 모두 대문자로 변경
    s = s.upper()
    #문자와 숫자가 아니면 제거
    s = re.sub('[^A-Z가-힣0-9]', '', s)
    return s == s[::-1]

print(isPalindrome("우영우"))
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
"""