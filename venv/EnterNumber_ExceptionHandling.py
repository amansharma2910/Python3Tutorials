while True:
    try:
        num= int(input("PLease neter a number:"))
        break
    except ValueError:
        print("PLease enter a numeric value.")
    except:
        print("An unknown error occured.")

print("Thanks for entering a number.")