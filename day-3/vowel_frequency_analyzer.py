sentence=input("Enter the sentence : ")
count=0
sentence=sentence.lower()
for i in sentence:
    if i=="a" or i=='e' or i=='i' or i=='o' or i=='u':
        count+=1
print(count)