while (True):
    a = raw_input("Enter value of 'a' : ")
    b = raw_input("Enter value of 'b' : ")
    try:
        l = int(a)
        m = int (b)
        c = l/m
        print (c)
        break
    except ValueError:
        print ("Incorrect value of 'a', please try again")
    except ZeroDivisionError:
        print ("The value cannot be zero.")
    else:
        print ("In else")
    finally:
        print ("Finally")