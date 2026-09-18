class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        ip4=queryIP.split('.')
        ip6=queryIP.split(':')
        if len(ip4)==4:
            for i in ip4:
                if not i.isdigit():
                    return "Neither"
                if len(i)>3 or (len(i)!=1 and i[0]=="0"):
                    return "Neither"
                if not (0<=int(i)<=255):
                    return "Neither"

            return "IPv4"
        if len(ip6)==8:
            character=set('abcdefABCDEF')
            for i in ip6:
                if len(i)>4 or len(i)==0:
                    return "Neither"                
                for j in i :
                    if not (j.isdigit() or j in character):
                        return "Neither"                        
            return "IPv6"
        return "Neither"