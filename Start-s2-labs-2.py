# Author RTS 2/1/22

def initials(rows): # Defining 
    for row in rows: 
        for a in row:
            if a == 0: # Checking the list 
                row += 1 
                
# Test 
last_intitial = ["B.", "D.", "H.", "E.", "G.", "G.", "H.", "R.", "M.", "L.", "I.", "I.", "N.", "N.", "O.", "P.", "P.", "X.", "T.", "S.", "S.", "P."]

rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin", "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]

print(initials(rows))