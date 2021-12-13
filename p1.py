class Solution :
    def isPalindrome(self, x):
        s=str(x);
        meio = (len(s)) // 2
        for index,v in enumerate(s):
            pos = (len(s)-1)-index;
            if pos <= meio:
                if  v != s[pos]:
                    return False
        return True


p =  Solution();
print(p.isPalindrome(123));