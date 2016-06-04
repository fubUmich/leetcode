class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.search_next_ip([], s, result, 0)
        return result
        
    
    def search_next_ip(self, list, s, result, start):
        if len(list) == 4 and start == len(s):
            result.append(self.convert_list_to_IP(list))
            return
        if len(s) - start > 3 * (4 - len(list)):
            return
        for i in range(1, 4):
            if start + i > len(s):
                break
            newNum = s[start:start + i]
            if newNum == '0' or (newNum[0] != '0' and int(newNum) < 256):
                list.append(newNum)
                self.search_next_ip(list, s, result, start + i)
                list.pop()
        
        
    def convert_list_to_IP(self, list):
        return '.'.join(list)