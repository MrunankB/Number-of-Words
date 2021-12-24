def countWords():
    fileName = input("Enter the file name: ")
    numOfWords = 0
    file = open(fileName, 'r')
    for line in file:
        words = line.split()
        numOfWords = numOfWords + len(words)
    print("Number of words: ", numOfWords)

countWords()

