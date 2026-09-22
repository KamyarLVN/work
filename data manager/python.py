import json
command = ""

while command != "1" or command != "2" or command != "3" or command != "4" or command != "5" or command != "6":
    back = False
    print("""-------------menu---------------- #the menu part of program
    1. add user
    2. delete user
    3.edit user
    4.search user
    5.show all users
    6.exit
    -----------------------------""")
    command = input("choose: ")
    if command == "1":  #adding 
      while back == False:   # the program wonts stop if answer is wrong
        with open(r"D:\Programs\vscode\user.json","r",encoding="UTF-8") as file:   # imnporting json                                                                                       
          data  = json.load(file)
        name = input("what is the name? /print back to go to menu:  ")
        if name != "back": # if the name isnt back
          city = input("where does he live? ")
          age = (input("how old is he/she? ")) #getting the information
          new_user = {                  # the new info
            "name": name,
            "city" : city,
            "age" : age
            }
          data.append(new_user)  #adding it to the data
          back = True
        if name == "back":        #to allow one to go back to menu
          back = True    #the key to break the loop
      
     
        with open(r"D:\Programs\vscode\user.json","w",encoding="UTF-8") as file:
          json.dump(data,file,ensure_ascii=False,indent =4) #adding the new info to json file

    if command == "2":  #deleting
      with open(r"D:\Programs\vscode\user.json","r",encoding="UTF-8") as file:
        data = json.load(file)  #loading the info
      while back == False: #making a loop so the program doesnt stop
        choice = input("who do you want to delete? / print back to go to menu ")
        for user in data:   # to run the program on all the json file dics
          if user["name"] == choice:
            data.remove(user)  #removing
            with open(r"D:\Programs\vscode\user.json","w",encoding="UTF-8")as file:
              json.dump(data,file,ensure_ascii=False,indent=4) #adding the deleted 
            back =True   #going out of the loop to the main cycle
        if choice == "back": # option to go back to menu
          back = True 
          break
         
    if command == "3":  #editing
        with open(r"D:\Programs\vscode\user.json","r",encoding="UTF-8") as file:
          data = json.load(file) #loading the file

        
        while back == False: #making the loop so the wrong answer doesnt stop the program
          choice = ""
          for user in data:  # everything in the json file
              choice = input("who do you wanna edit? /print back to go to menu")
              if user["name"] == choice:
                  new_name = input("what is the new name? ")
                  new_city = input("what is the new city? ")
                  new_age = int(input("what is th new age? "))
                  user["name"] = new_name
                  user["city"] = new_city
                  user["age"] = new_age        # asking for the new info
                  with open(r"D:\Programs\vscode\user.json","w",encoding="UTF-8") as file:
                    json.dump(data,file,ensure_ascii=False,indent=4)
                  back = True
                  break
              if choice == "back":
                back = True #option to back to menu
                break

    if command == "4":  #searching
      with open(r"D:\Programs\vscode\user.json","r",encoding="UTF-8") as file:
        data = json.load(file) #loading the file
      choice = ""
      while back == False:
        choice = input("who do you want to know about / print back to go to menu")
        for user in data: #seeing all the users
          if user["name"] == choice:
            print(user)
            back = True
          if choice == "back":  #option to go back to menu
            back = True
            break

    if command == "5":  #all users
      with open(r"D:\Programs\vscode\user.json","r",encoding="UTF-8") as file:
        data = json.load(file)
      while back == False:   
          print(data) #showing everything in the json file
          back = True

    if command == "6": #exit
      break