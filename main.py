def countA(word):
    num=0
    for i in range(0,len(word)):
        if word[i] == "a":
            num=num+1
    return num