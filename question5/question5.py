# only employees.txt data is copyed from AI 

with open("employees.txt","r") as f1:
    
    with open("management.txt","w") as f2:
        while True:
            text=f1.readline()
            if text=="":
                break
            
            if 'Python' in text:
                f2.write(text)

        