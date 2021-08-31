def countwordsfromfile():
    filename = input("Enter The File Name:")
    numberofwords=0
    file = open(filename,"r")
    for line in file:
        words=line.split()
        numberofwords=numberofwords +len(words)
    print("number of words:")
    print(numberofwords)
countwordsfromfile()