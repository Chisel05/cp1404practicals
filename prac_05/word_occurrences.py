"""
Word Occurrences
Estimate: 20 minutes
Actual:   23 minutes
"""

text = input('Text: ')

words = text.split(" ")
word_count_pairs = [(word, words.count(word)) for word in words]
word_to_count = {word_count_pair[0]: word_count_pair[1] for word_count_pair in word_count_pairs}

longest_word_length = max([len(word) for word in words])
ordered_words = sorted({word for word in word_to_count})
for word in ordered_words:
    print(f"{word:{longest_word_length}} = {word_to_count[word]}")
