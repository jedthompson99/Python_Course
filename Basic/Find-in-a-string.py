# sentence = "the quick brown fox can jump over those lazy dogs"

# query = sentence.find('quick')
# print(query)

# # returns "4", the index number


# sentence = "the quick brown fox can jump over those lazy dogs"

# query = sentence.index('quick')
# print(query)

# # find returns a "-1" if it doesn't find the substring, and index throws an error

sentence = "the quick brown fox can jump over those lazy dogs"

query = "fox" in sentence
print(query)
