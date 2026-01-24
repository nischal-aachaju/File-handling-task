with open("a.txt","r") as f_a:
    with open("b.txt","w") as f_b:
        while True:
            text=f_a.readline()
            f_b.write(text)
            print(text)
            if text=="":
                break
            
            
        
            

