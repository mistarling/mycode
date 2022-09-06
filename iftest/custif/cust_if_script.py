#!/usr/bin/env python3

def main():
    synopsis = "Your book: "
    print("Book list:\n"
    "1. Harry Potter\n"
    "2. Hobbit & Lord of the Rings\n"
    "3. Chronicales of Narnia\n"
    "4. Indiana Jones\n")
    mybook = float(input("Which book or movie would you like a synopsis: ?"))

    messagesel = "Please make a proper selection."
    if mybook == 1:
        print(synopsis + "Harry Potter is a Wizard that likes to cause trouble for muggles.")
    elif mybook == 2:
        print(synopsys + "Haven't seen this movie.")
    elif mybook == 3:
        print(synopsis + "Chronicales of Narnia is ok.")
    elif mybook == 4:
        print(synopsis + "Indiana Jones is a great movie.")
    else:
        print(messagesel)
        
main()