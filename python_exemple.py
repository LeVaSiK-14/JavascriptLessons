t = True
while t:
    percent = input("Enter percent: ")
    if percent.isdigit():
        percent = int
        t = False
        print(percent)
    else:
        pass