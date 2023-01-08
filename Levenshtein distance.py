# Using the Levenshtein distance this program 
# outputs the required number of changes that 
# is required to convert one piece of text 
# into the other, wheter that be an insertion, 
# deletion, substitution.
import Levenshtein as ls

text1 = input("Input first piece of text: ")
text2 = input("Input second piece of text: ")

jd = ls.distance(text1,text2)
print(jd)