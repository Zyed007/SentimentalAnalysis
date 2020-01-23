from textblob import TextBlob
fp=open("test.txt")
lst=list()
for line in fp:
    lst.append(line)

polarity_lst=list()
for elem in lst:
        blob=TextBlob(elem)
        polarity_lst.append(blob.sentiment)
fp.close()
with open('result.txt','w') as fp:
        for i in range(0, len(lst)):
              fp.write(lst[i]+"\n["+str(polarity_lst[i])+"]\n")
with open('po.txt','w') as fp:
        for i in range(0,len(lst)):
                fp.write(str(polarity_lst[i])+"]\n")
