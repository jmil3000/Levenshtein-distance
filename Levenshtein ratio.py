# Using a Levenshtein ratio this program 
# gives a percentage similarity between 
# two pieces of text
import Levenshtein as ls

text1 = input("Input first piece of text: ")
text2 = input("Input second piece of text: ")

jd = ls.ratio(text1,text2)
jd = '{:.1%}'.format(jd)
print(jd)