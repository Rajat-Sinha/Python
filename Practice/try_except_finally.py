#Try and Catch

while True:
    try:
        x = int(input('Enter the number\n'))
        print(18/x)
    except ValueError:
        print('Enter a number')
    except ZeroDivisionError:
        print('Cannot be divided by Zero')
    except:
        break
    finally:
        print('Loop Completed')
