#Dot Product Calculator
#Eirik Valderhaug

import os

while True:
    os.system('clear')
    print("Dot Product Calculation")
    print("Eirik Valderhaug")

    #Enter values for vector a
    a1 = int(input("\nEnter value alla1: "))
    a2 = int(input("Enter value a2: "))
    a3 = int(input("Enter value a3: "))

    #Enter values for vector b
    b1 = int(input("\nEnter value b1: "))
    b2 = int(input("Enter value b2: "))
    b3 = int(input("Enter value b3: "))

    #Calculate the dot product
    c1 = (a2*b3)-(b2*a3)
    c2 = (a3*b1)-(b3*a1)
    c3 = (a1*b2)-(b1*a2)

    #print the result
    print("\nThe dot product of vector a X vector b is\n")
    print([c1,c2,c3])
    print("\n")

    string = "\n[" + str(c1) + "," + str(c2) + "," + str(c3) + "]"

    with open('calculations.txt', 'a') as a_writer:
        a_writer.write(string)

    while True:
        again = str(input("Would you like to perform another dot product calculation? [y]/[n] "))
        if again in ["y","n"]:
            break

    if again == "n":
        print("\nThank you for using the amazing dot product calculator!\n")
        with open('calculations.txt', 'a') as a_writer:
            a_writer.write("\nEnd of session")
        break
