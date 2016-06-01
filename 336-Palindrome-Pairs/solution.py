class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        
        result_list = []
        word_dict = {word: index for index, word in enumerate(words)}

        for word in words:
            if word[::-1] in word_dict and word[::-1] != word:
                result_list.append([word_dict[word], word_dict[word[::-1]]])
            for i in range(len(word)):
                if self.is_palindrome(word[i:]):
                    reversed_word = word[:i]
                    reversed_word = reversed_word[::-1]
                    if reversed_word in word_dict and reversed_word != word:
                        result_list.append([word_dict[word], word_dict[reversed_word]])
            for i in range(1, len(word) + 1):
                if self.is_palindrome(word[:i]):
                    reversed_word = word[i:]
                    reversed_word = reversed_word[::-1]
                    if reversed_word in word_dict and reversed_word != word:
                        result_list.append([word_dict[reversed_word], word_dict[word]])
        
        return result_list
    
    @staticmethod
    def is_palindrome(word):
        return word == word[::-1]