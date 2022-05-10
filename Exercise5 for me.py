z = 1
while z == 1:
    def gettime():
        import datetime
        return datetime.datetime.now()

    def modified():
        print("Chose this Person, Who's you need:")
        person = int(input(" 1. Harry\n 2. Rohan\n 3. Hammad\n Please Input a Number: "))
        # men = 1
        if person == 1:
            def again():
                men = 1
                while men == 1:
                    print("What do you want for Harry!? ")
                    want = int(input(" 1. Diet\n 2. Exercise\n Please Input a Number: "))
                    if want == 1:
                        with open("Harry Diet.txt", "a") as h:
                            input1 = input("Enter the input what has Harry eaten?\n")
                            h.write("\n")
                            h.write(str([str(gettime())]) + input1)
                            # print(a)
                    elif want == 2:
                        with open("Harry Exercise.txt", "a") as H:
                            input2 = input("Enter the input what Exercise is Important for Harry?\n")
                            H.write("\n")
                            H.write(str([str(gettime())]) + input2)
                            # print(b)
                    else:
                        print("Wrong Input, Please Enter a Valid Input!")
                        again()
                    print("Do you want to more about Harry?")
                    men = int(input(" 1. Yes\n 2. No\n Input Number Please: "))
            again()
        elif person == 2:
            def again():
                men = 1
                while men == 1:
                    print('What do you want for Rohan?')
                    want = int(input(" 1. diet\n 2. Exercise\n Please enter a Valid Number: "))
                    if want == 1:
                        with open("Rohan Diet.txt", "a") as r:
                            input1 = input("Write please what has eaten Rohan.\n")
                            r.write("\n")
                            r.write(str([str(gettime())]) + input1)
                    elif want == 2:
                        with open("Rohan Exercise.txt", "a") as R:
                            input2 = input("Write please what exercise is Important for Rohan?\n")
                            R.write("\n")
                            R.write(str([str(gettime())]) + input2)
                    else:
                        print("Wrong Input, Please Enter a Valid Input!")
                        again()
                    print("Do you want to more about of Rohan?")
                    men = int(input(" 1. Yes\n 2. No\n Input a Number Please: "))
            again()
        elif person == 3:
            def again():
                men = 1
                while men == 1:
                    print("What do you want for Hammad?")
                    want = int(input(" 1. Diet\n 2. Exercise\n Please enter a valid Number 1/2: "))
                    if want == 1:
                        with open("Hammad Diet.txt", "a") as m:
                            input1 = input("write please what has eaten Hammad?\n")
                            m.write("\n")
                            m.write(str([str(gettime())]) + input1)
                    elif want == 2:
                        with open("Hammad Exercise.txt", "a") as M:
                            input2 = input("What exercise are important for Hammad?")
                            M.write("\n")
                            M.write(str([str(gettime())]) + input2)
                    else:
                        print("Wrong Input, Please enter a Valid Input!.")
                        again()
                    print("Do you want more about Hammad?")
                    men = int(input(" 1. Yes\n 2. No\n Input a Number Please: "))
            again()
        else:
            print("Wrong Input, Please Enter a Valid input, EX- 1 or 2 or 3")


    def show():
        print("Please choose your Person\n")
        person = int(input(" 1. Harry\n 2. Rohan\n 3. Hammad\n Please enter a Valid Number: "))
        # men = 1
        if person == 1:
            def again():
                men = 1
                while men == 1:
                    want = int(input("What do you want to show? \n 1. diet\n 2. Exercise\n Please enter a Valid Number: "))
                    if want == 1:
                        with open("Harry Diet.txt", "r") as a:
                            b = a.read()
                            print(b)
                    elif want == 2:
                        with open("Harry Exercise.txt", "r") as c:
                            d = c.read()
                            print(d)
                    else:
                        print("Wrong Input, Please Enter a Valid input EX- 1 or 2")
                        again()
                    men = int(input("Do you want to more about Harry?\n 1. Yes \n 2. No\n Please Enter a Valid Number: "))
            again()
        elif person == 2:
            def again():
                men = 1
                while men == 1:
                    want = int(input("What do you want to show? \n 1. Diet\n 2. Exercise\n Please enter a valid number: "))
                    if want == 1:
                        with open("Rohan Diet.txt", "r") as r:
                            a = r.read()
                            print(a)
                    elif want == 2:
                        with open("Rohan Exercise.txt", "r") as R:
                            b = R.read()
                            print(b)
                    else:
                        print("Wrong Input Please enter a Valid input EX- 1 or 2!")
                        again()
                    men = int(input("Do you want to more about Rohan?\n 1. Yes\n 2. No \n Please enter a number: "))
            again()
        elif person == 3:
            # global men
            # men = 1
            def m():
                men = 1
                while men == 1:
                    want = int(input("What do you want to show? \n 1. Diet\n 2. Exercise\n Please Enter a Valid Input: "))
                    if want == 1:
                        with open("Hammad Diet.txt", "r") as h:
                            k = h.read()
                            print(k)
                    elif want == 2:
                        with open("Hammad Exercise.txt", "r") as H:
                            l = H.read()
                            print(l)
                    else:
                        print("Wrong Input! Please enter a Valid input, EX- 1 or 2.")
                        m()
                    men = int(input("Do you want to more about Hammad?\n 1. Yes\n 2. No\n Please Enter a Number: "))
                    # men = men + 1
            m()
        else:
            print("Wrong Input! Please enter a Valid Input, EX- 1, 2 or 3.")
            show()
    print("Wellcome to Health management System!")

    run = int(input("What do you want?\n 1. Modified (Add Something in this files)\n 2. Show (Read all this file)\n Please Enter a valied Input: "))
    if run == 1:
        modified()
    elif run == 2:
        show()
    else:
        print("Wrong Input! Please enter a Valid Input, Choose- 1 or 2")
    z = int(input("Do you want to again Play This?\n 1. Yes \n 2. No\n Please Input Number and Press Enter: "))