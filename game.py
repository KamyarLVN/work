class Character:      #the class
    def __init__(self,ch_class,level,hp,heal_power,attack_power): #getting the features
        self.ch_class = ch_class
        self.level = level
        self.hp = hp
        self.max_hp = hp
        self.heal_power = heal_power
        self.attack_power = attack_power
    def __str__(self): #to type them all
        return "ch_class:" + " " + self.ch_class + "| level:" + " "+str(self.level)+"| hp:" + " "+str(self.hp) + "| heal_power:" + " "+ str(self.heal_power) +"| attack_power: "+str(self.attack_power)
    def was_attacked(self,other):  #functions for characters attacking each other
        if self.hp <= 0:  #if the hp is already 0 and the character is already dead
            print(self.ch_class,"is already dead")  
            print("after")
            print(wizard)
            print(knight)
            print("______________________________________________________________________________")
        elif self.hp <= other.attack_power:  
            self.hp = 0
            print(other.ch_class,"killed",self.ch_class)
            print("after") 
            print(wizard)
            print(knight)
            print("______________________________________________________________________________")
        elif self.hp > other.attack_power:  
            self.hp -= other.attack_power
            print(self.ch_class,"was damaged",other.attack_power,"from",other.ch_class)  
            print("after")
            print(wizard)
            print(knight)
            print("_______________________________________________________________________________")
    def heal(self):  #creating method for healing
        if self.heal_power + self.hp >= self.max_hp: #if healing leads to the health getting maxed
            print(self.ch_class,"was fully healed")
            print("after")
            print(wizard)
            print(knight)
            print("_______________________________________________________________________________")
        elif self.hp == 0:
            return
        else:
            self.hp += self.heal_power
            print(self.ch_class,"health increased",self.heal_power) 
            print("after")
            print(wizard)
            print(knight)
            print("______________________________________________________________________________")




wizard = Character("wizard",17,50,10,12)        #how the characters are
knight = Character("knight",20,100,7,20)
print("at first")
print(wizard)
print(knight)
print("__________________________________________________________________________________________")


choice = ""
while  choice != "3":  # choosing what to do
    print("CHOOSE")          #choosing the option
    print("1.attack      2.heal       3.exit")
    choice = input(": ") 
    if choice == "1":
        character = ""      #choosing the character
       
        while character != "1" and character != "2": #choosing who you want to be
            print("1.|wizard |    2.|knight|")
            character = input("who do you want to be? ")
            if character == "1": #if you are the wizard
                knight.was_attacked(wizard)
                
                
            if character == "2": #if you are the knight
                wizard.was_attacked(knight)
            
    if choice == "2": #if you choose heling
        character = ""
        while character != "1" and character != "2": #choosing who you wanna heal
         print("who do you wanna heal? ")
         print("1.|wizard      2.|knight|")
         character = input(": ")
         if character == "1": #if you choose wizard
            wizard.heal()
           
         if character == "2": #if you choose knight
            knight.heal()
            
    if choice == "3":  #if you choose to exit the game
        print("come back again")
        break
    
            




            

