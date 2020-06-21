i = 0
#i + "string"
#i / 0
#4 + x * 5
#2 + "x"
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! It is not a valid number. Try again...")
    except (RuntimeError, TypeError, NameError):
        pass

x = int("z")

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! It is not a valid number. Try again...")
    except (RuntimeError, TypeError, NameError):
        pass
    finally:
        print("You have typed " + str(x))

while True:
    try:
        x = input("Please enter a number: ")
        i = int(x)
        break
    except ValueError:
        print("Oops! It is not a valid number. Try again...")
    except (RuntimeError, TypeError, NameError):
        pass
    finally:
        print("You have typed " + str(x))
