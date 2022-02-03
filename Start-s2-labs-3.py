# Author RTS 2/1/22

def comes_after(st, letter): # Defines variable
    letter = letter.lower() # Makes variable lowercase
    return ''.join(b for a, b in zip(st.lower(), st[1:]) if a == letter and b.isalpha()) # Retunrs the letter after 
    