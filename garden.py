import spacy
nlp = spacy.load('en_core_web_sm')

gp_sentence_1 = "We painted the wall with cracks"
gp_sentence_2 = "The florist sent the flowers was pleased"
gp_sentence_3 = "The cotton clothing is made of grows in Mississippi"
gp_sentence_4 = "The girl told the story cried"
gp_sentence_5 = "Mary gave the child the dog bit a Band-Aid"

garden_path_sentences = [gp_sentence_1, gp_sentence_2, gp_sentence_3, gp_sentence_4, gp_sentence_5]

for sentence in garden_path_sentences:
    nlp_sentence = nlp(sentence)
    nlp_sentence.text.split()
    print([(token, token.orth_, token.orth) for token in nlp_sentence])
    print([(token, token.label_, token.label) for token in nlp_sentence.ents])

'''
The entity recognition gave me "PERSON" for Mary which was expected, but I didn't recognise "GPE" which represents 
countries, cities and states. I found a full list at https://www.dataknowsall.com/ner.html
'''

