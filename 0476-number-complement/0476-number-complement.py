class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary=list(str(bin(num)[2:]))
        for i in range(len(binary)):
            if binary[i]=='1':
                binary[i]='0'
            else:
                binary[i]='1'
        binary="".join(binary)
        return int(binary,2)