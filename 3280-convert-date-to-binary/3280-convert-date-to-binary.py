class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        year=bin(int(date[:4])).replace("0b","")
        MM=bin(int(date[5:7])).replace("0b","")
        dd=bin(int(date[8:])).replace("0b","")

        return str(year)+"-"+str(MM)+"-"+str(dd)