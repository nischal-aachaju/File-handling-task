
file=open("sample.txt","r")
first_word_lst=[]

def extract_firstword(words_lst):
    for i in words_lst:
        words=i.split()
        first_word=words[0]
        # print(first_word)
        first_word_lst.append(first_word)

words_lst=file.readlines()
extract_firstword(words_lst)
print(first_word_lst)




