class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        cur=chars[0]
        s=""
        count=1
        for i in chars[1:]:
            if cur==i:
                count+=1
            else:
                if count==1:
                    s+=cur
                else:
                    s=s+cur+str(count)
                count=1
                cur=i
        if count==1:
            s+=cur
        else:
            s=s+cur+str(count)
        chars[:len(s)] = s
        return len(s)