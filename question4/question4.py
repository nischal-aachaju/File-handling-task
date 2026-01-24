line_count=0
with open("story.txt","r") as f :
    while True:
        text=f.readline()
        if text=="":
            break
        line_count+=1 

print(f"Total line: {line_count}")