
line=0
with open('story.txt','r') as f:
    
    while True:
        text=f.readline()
        if text=="":
            break
        
        text_lst=text.split()
        line+=1
        word=len(text_lst)
        print(f"line {line}:{word} word")

