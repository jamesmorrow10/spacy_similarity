import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')

# I have added this list to sort the results for easier interpretation
word_similarity_list = []

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
        word_similarity_list.append([token1.text, token2.text, token1.similarity(token2)])

# Sorting and printing the results of the word similarity
word_similarity_list.sort(key=lambda x: x[2], reverse=True)
print("-------------Sorted word similarity list-----------")
for word_word_similarity in word_similarity_list:
    print(word_word_similarity[0], word_word_similarity[1], word_word_similarity[2])
print("-------------End sorted word similarity list-----------")

sentence_similarity_list = []

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence_to_compare + " - " + sentence + " - ", similarity)
    sentence_similarity_list.append([sentence_to_compare, sentence, similarity])

# printing the results of the sorted sentence sentence similarity
sentence_similarity_list.sort(key=lambda x: x[2], reverse=True)
print("-------------Sorted sentence similarity list-----------")
for sentence_sentence_similarity in sentence_similarity_list:
    print(sentence_sentence_similarity[0], sentence_sentence_similarity[1], sentence_sentence_similarity[2])
