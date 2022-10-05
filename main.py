from Database import Database

# declare functions to use


# declare variables to use
userSets = ""
wd = Database()

# program run until user want to quit
programRunning = True
while programRunning:
    # get user option
    sets = wd.getset()
    print(sets)
    print("Choose your word set or create new one")
    print("1 -> choose set")
    print("2 -> create set")
    print("3 -> terminate program")
    userChoice = input("Enter choice: ")
    print(userChoice)

    # user want to study
    if userChoice == '1':
        userChoice2 = input("Enter set: ")
        for x in sets:  # get set value
            if userChoice2 == x[0]:
                userSets = userChoice2
        if userSets == "":  # get file
            print("invalid value")
        while userChoice != '0':  # user choice to study
            print("1. add another word/definition")
            print("2. study for all words")
            print("3. study for starred words")
            print("0. go back to main menu")
            userChoice = input("Choose your option: ")
            match userChoice:  # add more words on set
                case "1":
                    word = input("word: ")
                    definition = input("definition: ")
                    wd.insertword(userSets, word, definition)
                case "2":
                    rows = wd.getworddef(userSets)
                    for x in rows:
                        print(x[0])
                        input("press enter to see the definition")
                        print(x[1])
                        input("press enter to see the next word")
                        star = input("Want to star? Y?N ")
                        if star == "Y":
                            wd.startheword(x[0])
                    print("Done studying!")
                case "3":
                    rows = wd.getstaredworddef(userSets)
                    for x in rows:
                        print(x[0])
                        input("press enter to see the definition")
                        print(x[1])
                        input("press enter to see the next word")
                        star = input("Want to remove star? Y?N ")
                        if star == "Y":
                            wd.destartheword(x[0])
                    print("Done studying!")
                case "0":
                    userSets = ""
                    break

    # user want to add a study set
    if userChoice == '2':
        userChoice2 = input("Enter set: ")
        try:
            wd.newset(userChoice2)
        except:
            print("Invalid value option")

    # user want to quit
    if userChoice == '3':
        programRunning = False
