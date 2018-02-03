#Syntax Error and
while True:
    try:
        x = int(input('What is your Fav Number\n'))
        print(18/x)
        break
    except ValueError:
        print('Please Enter A Number')
    except ZeroDivisionError:
        print('Cannot be Divide by 0')
    except:
        break
    finally:#No matter What if runs or throw an exception
        print('Loop Completed')
