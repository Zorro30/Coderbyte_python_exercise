'''Using the Python language, have the function LongestWord(sen) take the sen parameter being passed and return the
 largest word in the string. If there are two or more words that are the same length, return the first word from the
  string with that length. Ignore punctuation and assume sen will not be empty. 
'''

def LargestWord(s):

    listss = "".join([',',c][int(c.isalnum())] for c in s).split(',')
    maxlen = max([len(i) for i in listss])
    return [w for w in listss if len(w) == maxlen][0]

print(LargestWord(input()))