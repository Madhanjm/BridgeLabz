template = "Hello <<UserName>>, How are you?"

while True:
    username=input("Enter Your Name: ").strip()
    if(len(username) >=3):
        break
    else:
        print("Username Must Have At Least 3 Characters")

result=template.replace("<<UserName>>",username)  
print(result)  