#The module csv is imported to handle the story format in a csv file
import csv
#The module os is imported to check file path and quit application if user chooses
import os
#The module time is imported to have a delay between game ending and starting
import time

#The menu is handled by the function below
def menu():
    #There is a while loop to catch errors
    while True:
        #If the user tries to input anything other than a number the try/except will catch it here
        try:
            #The menu is stored in the menu variable
            menu = "****** Text Adventure Game  v1.0 ****** \n*                                     *\n*           1 - New Game              *\n*           2 - Load Game             *\n*           3 - Quit                  *\n*                                     *\n***************************************"
            #Menu is printed here
            print(menu)
            #Depending on the number the user chooses from the menu, the program will go to the desired option
            choice = int(input("> "))
            #Just a little space to keep things a little separated
            print("\n")
            #If the user chooses a number from 1 to 3 the program will continue
            if choice > 0 and choice < 4:
                #If the user chooses to start a new game the value of choice will be returned to be used in the main function
                if choice == 1:
                    break
                #If the user chooses to load a prevously saved game
                if choice == 2:
                    #The os module will check the folder to see if a save file exists
                    if os.path.exists('saved.txt'):
                        break
                    #If a save file does not exist the game will just start a new game and inform the user
                    else:
                        print("***       No save file exists       ***\n*          Starting new game          *\n")
                        choice = 1
                        break
                #The program will use the built-in exit function from the os module to close the program
                if choice == 3:
                    os._exit(1)
            #If the user tries to enter any number other than a number from 1 to 3, the program will inform them and let them try again
            elif ValueError:
                print(">>>>That is not a number from 1 to 3<<<<\n")
                continue
        #If the user tries to input anything other than a number, the program will catch it here and let them try again
        except ValueError:
            print(">>>>That is not a number<<<<\n")
    #The value of choice is returned here to be used in the main function
    return choice


#The story and canculations are processed here
def story():
    #The program opens the story file that is in the folder
    infile = open('testfile.csv', 'r')
    question = "What do you want to do?"
    #Empty list is declared for a 2D list to be made
    rowData = []
    #The story is assumed to always start on the first line of the csv file, so the currentRow reflects that
    currentRow = 0

    #The csv module is used here to read the csv file
    csv_reader = csv.reader(infile)

    #The for loop loops through the entire csv file and puts it into the empty list from before
    for row in csv_reader:
        rowData.append(row)

    #While loop is used to keep user in a loop to catch any errors
    while True:
        #The program will try this chunk of code and proceed if no errors arise
        try:
            #The first set of prompts are displayed using rowData, currentRow and the appropriate index
            print(rowData[currentRow][0])
            print(question)
            print("1 - ", rowData[currentRow][1])
            print("2 - ", rowData[currentRow][2])
            #Save game option is presented here manually, not stored in a variable previously
            print("3 - ", "Save Game")
        
            #User is presented with the chance to choose an option
            choice = int(input("> "))
            print("\n")
            #If the user chooses an option from 1 to 3 the program will continue as normal
            if choice > 0 and choice < 4:
                break
            #If the user does not choose a number from 1 to 3 the program will inform them and give them and chance to try again
            elif ValueError:
                print("\n>>>>That is not a number from 1 to 3<<<<\n")
                continue
        #If the user gives input that is not a number the program will inform them and let them try again
        except ValueError:
            print("\n>>>>That is not a number<<<<\n")


    #While loop is used again to check for errors
    #This is where the calculations happen
    while True:
        #If the user has chosen option 1 the program will look at the value of option 1 and subtract 1 because the variable for the current line will use that value--
        #--to go to the appropriate line. Since the value of option 1 is the actual csv line and not the index, the program subtracts 1 to get the index, which will--
        #now go to the appropriate line.
        if choice == 1:
            currentRow = int(rowData[currentRow][3]) - 1
        #Same thing that happened with option 1 happens here with option 2
        if choice == 2:
            currentRow = int(rowData[currentRow][4]) - 1
        #If the user want to save the game, there is a text file that is created called saved.txt
        if choice == 3:
            outfile = open('saved.txt', 'w')
            #The value of currentRow is currently an interger, so the program turns it into a string because all elements in a text file are strings
            outfile.write(str(currentRow))
            outfile.close()
            print(">>>>The game has been saved<<<<")
            break
            

        #The program checks to see if the condition for 'game over' has been met. If not, it will run the code below
        if not rowData[currentRow][1] == "":
            #While loop used here to check for errors
            while True:
                try:
                    #The story prompt that the user is currently on will be displayed
                    print(rowData[currentRow][0])
                    print(question)
                    print("1 - ", rowData[currentRow][1])
                    print("2 - ", rowData[currentRow][2])
                    print("3 - ", "Save Game")
                    choice = int(input("> "))
                    print("\n")
                    if choice > 0 and choice < 4:
                        break
                    elif ValueError:
                        print("That is not a number from 1 to 3")
                except ValueError:
                    print("That is not a number")

        #If the user has met 'game over' conditions, the program will go here and run the code below
        else:
            print(rowData[currentRow][0])
            print("\n")
            break
    
    #The program will close the testfile.csv file here
    infile.close()


#If the user has chosen to start from a save file the program will go here and run the code below
def save():
    infile = open('testfile.csv', 'r')
    #The save file will be opened here
    save_reader = open('saved.txt', 'r')
    #The save file will then be read and the string in the file that is currently a number will be converted into an interger. That is the location where the user last was
    currentRow = int(save_reader.read())
    question = "What do you want to do?"
    rowData = []

    csv_reader = csv.reader(infile)

    for row in csv_reader:
        rowData.append(row)

    while True:
        try:
            print(rowData[currentRow][0])
            print(question)
            print("1 - ", rowData[currentRow][1])
            print("2 - ", rowData[currentRow][2])
            print("3 - ", "Save Game")
        
            choice = int(input("> "))
            print("\n")
            if choice > 0 and choice < 4:
                break
            elif ValueError:
                print("\n>>>>That is not a number from 1 to 3<<<<\n")
                continue
        except ValueError:
            print("\n>>>>That is not a number<<<<\n")


    while True:
        if choice == 1:
            currentRow = int(rowData[currentRow][3]) - 1
        if choice == 2:
            currentRow = int(rowData[currentRow][4]) - 1
        if choice == 3:
            outfile = open('saved.txt', 'w')
            outfile.write(str(currentRow))
            outfile.close()
            break
            

        if not rowData[currentRow][1] == "":
            while True:
                try:
                    print(rowData[currentRow][0])
                    print(question)
                    print("1 - ", rowData[currentRow][1])
                    print("2 - ", rowData[currentRow][2])
                    print("3 - ", "Save Game")
                    choice = int(input("> "))
                    print("\n")
                    if choice > 0 and choice < 4:
                        break
                    elif ValueError:
                        print("That is not a number from 1 to 3")
                except ValueError:
                    print("That is not a number")

        else:
            print(rowData[currentRow][0])
            print("\n")
            break
    
    save_reader.close()
    infile.close()


def main():
    #A while loop is used here to run the program repeatedly until the user chooses to quit
    while True:
        #Menu is called here and the value of menu is assigned to the variable 'choice'
        choice = menu()
        #If the user has chosen to start a new game the program will go here
        if choice == 1:
            #The function 'story' is called here and this is where the story begins
            story()
        if choice == 2:
            #The function'save' is called here and this is where the user starts from where they last saved
            save()
        #When the user has either achieved 'game over' or they have saved the game, the program will use the time module to wait 2 seconds before starting up again
        try:
            time.sleep(2)
        except:
            pass

#The main function is called here
main()