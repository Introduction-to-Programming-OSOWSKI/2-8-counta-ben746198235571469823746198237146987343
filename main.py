def countA(w):
    num=0
    for i in range(0,len(w)):
        if w[i] == "a":
            num=num+1
    print(str(num))