# Using a Levenshtein ratio this program 
# gives a percentage similarity between 
# two pieces of text
import Levenshtein as ls

text1 = "Bree likes to have so much fun!"
text2 = "Bree likes to have lots of fun!"

jd = ls.ratio(text1,text2)
jd = '{:.1%}'.format(jd)
print(jd)