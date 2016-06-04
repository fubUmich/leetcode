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
            new_num = s[start:start + i]
            if new_num == '0' or (new_num[0] != '0' and int(new_num) < 256):
                self.search_next_ip(list + [new_num], s, result, start + i)
        
        
    def convert_list_to_IP(self, list):
        return '.'.join(list)