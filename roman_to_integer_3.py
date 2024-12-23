class Solution:
    # function to convert roman to integer
    def romanToInt(self, s: str) -> int:
        roman=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        num=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
        ind=0
        res=0
        i=0
        while i<=len(s)-1:
            if i!=len(s)-1:
                if s[i]=='I' and (s[i+1]=='V' or s[i+1]=='X'):
                    if s[i+1]=='V':
                        res+=4
                    elif s[i+1]=='X':
                        res+=9
                    i+=2
                elif s[i]=='X' and (s[i+1]=='L' or s[i+1]=='C'):
                    if s[i+1]=='L':
                        res+=40
                    elif s[i+1]=='C':
                        res+=90
                    i+=2
                elif s[i]=='C' and (s[i+1]=='D' or s[i+1]=='M'):
                    if s[i+1]=='D':
                        res+=400
                    elif s[i+1]=='M':
                        res+=900
                    i+=2
                else:
                    ind=roman.index(s[i])
                    res+=num[ind]
                    i+=1
            else:
                ind=roman.index(s[i])
                res+=num[ind]
                i+=1
        return res
