with open("input.txt","r") as f1:
    with open("output.txt",'w') as f2:
        data=f1.readlines()
        for i in data:
            f2.write(f"{i.upper()}")
