while True :
        # Ask user if they are happy to follow the rules
        number = input("How many rounds would you like to play? [3 or 5]")

        if number == "3" or number == "5" :
            break
            """return number - The above code was inside a function i created,
               if your using it without a function,
               you would need to replace the “return number” with break"""
        elif (type(number) == int or float) :
            print("Please enter a value of 3 or 5 rounds")
        else :
            # Invalid Response, Retry
            print("Please enter a numeric response")