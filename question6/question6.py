
def square(num_str):
    num=int(num_str)
    square_num=num*num
    f2.write(f'{str(square_num)}\n')


with open("number.txt","r") as f1:

    with open("squared.txt","w") as f2:
        while True:
            num_str=f1.readline()
            if num_str=="":
                break
            
            else:
                square(num_str)