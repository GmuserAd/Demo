import re
def removeABC(phrase):
    count1=len(phrase)
    phrase = phrase.replace("a",'')
    phrase = phrase.replace("b",'')
    phrase = phrase.replace("c",'')
    count2=len(phrase)
    if count1==count2:
         print("Null")
    else:print(phrase)


removeABC('sannazmdmnca')