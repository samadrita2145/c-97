sentence=input("Enter the sentence: ")
alphabetCount=0
wordCount=1
for i in sentence: 
    alphabetCount=alphabetCount+1 
    if(i==' '):
        wordCount=wordCount+1
print("No. of words= ",wordCount)
print("No. of alphabets= ",alphabetCount)
