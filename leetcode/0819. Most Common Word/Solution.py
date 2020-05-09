# https://leetcode.com/problems/most-common-word/

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        for ps in "!?',;.":
            paragraph = paragraph.replace(ps, " ")
        paragraph_words = [word for word in paragraph.lower().split()]
        word_counts = collections.Counter(paragraph_words)
        
        most_frequent_word = ''
        highest_frequency = 0
        for word, word_count in word_counts.items():
            if word_count > highest_frequency and word not in banned_set:
                most_frequent_word = word
                highest_frequency = word_count
                
        return most_frequent_word