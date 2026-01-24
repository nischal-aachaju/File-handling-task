with open("history.log","a") as f:
    while True:
        print("Write exit- to exit")
        msg=input("Enter message:")
        if msg=='exit-':
            print("Message saved succesfully")
            break
        else:
            f.write(f"\n{msg}")
            print(" Message Added")

        