while (True):
    a = raw_input("Enter your age : ")
    try:
        print int(a)
        break
    except ValueError:
        print "Ops! That was not a valid number. Try again."