# Author RTS 2/1/22

def double_every_other(l): # Defining variable
    return [x * 2 if i % 2 else x for i, x in enumerate(l)] # If i % 2 it returns x *2 else it retuens x for i in enumerate the list