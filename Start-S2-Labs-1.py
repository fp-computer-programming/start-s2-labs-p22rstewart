# Author RTS 2/1/22

def odd_number(list): # Defining the odd number
    for i, v in enumerate(list): 
        try:
            if i % 2 != 0: # If the number is not = to 0
                print(int(v)) # Print the string "v"
        except:
            if v == str or bool: # If they enter anthing but a number 
                print("Only input integers") # Display an error message

odd_number([1, "two", 3, 4, 5, 6])
