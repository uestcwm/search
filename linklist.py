class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic={}
        sub=''  #变化的子串
        if len(s) <2 or s == s[::-1]:
            return s
        else:
            for i in s:
                medium_list = []
                if i not in sub:
                    sub += i
                    if s.index(i) == len(s)-1:
                        if sub == sub[::-1]:
                            return sub
                        else:
                            return sub[0]
                else:
                    sub = i+sub.split(i)[-1]+i
                    print(sub)
                    # if s[s.index(i)+1] == i:
                    #     sub+=s[s.index(i)+1]
                    if sub == sub[::-1]:
                        dic[sub]=len(sub)
                    else:
                        return sub[0]
            return max(dic, key=dic.get)   
