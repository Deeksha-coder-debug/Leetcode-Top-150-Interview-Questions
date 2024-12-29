class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res=[]
        cur_line=[]
        cur_length=0
        for word in words:
            if cur_length+len(cur_line)+len(word)>maxWidth:
                for i in range(maxWidth-cur_length):
                    cur_line[i%(len(cur_line) -1 or 1)]+=' '
                res.append(''.join(cur_line))
                cur_line=[]
                cur_length=0
            cur_line.append(word)
            cur_length+=len(word)
        res.append(' '.join(cur_line).ljust(maxWidth))
        return res
