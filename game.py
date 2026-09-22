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
    def attack(self,other):  #functions for characters attacking each other
        if other.hp <= 0:  #if the hp is already 0 and the character is already dead
            print(self.ch_class,"is already dead")  
            print("after")
            print(wizard)
            print(knight)
            print(archer)
            print("______________________________________________________________________________")
        elif other.hp <= self.attack_power:  #if other hp is more than the attack
            other.hp = 0
            print(self.ch_class,"killed",other.ch_class)
            print("after") 
            print(wizard)
            print(knight)
            print(archer)
            print("______________________________________________________________________________")
        elif other.hp > self.attack_power:  
            other.hp -= self.attack_power
            print(other.ch_class,"was damaged",self.attack_power,"from",self.ch_class)  
            print("after")
            print(wizard)
            print(knight)
            print(archer)
            print("_______________________________________________________________________________")
    def heal(self):  #creating method for healing
        if self.heal_power + self.hp >= self.max_hp: #if healing leads to the health getting maxed
            print(self.ch_class,"was fully healed")
            print("after")
            print(wizard)
            print(knight)
            print(archer)
            print("_______________________________________________________________________________")
        
            
        elif self.hp == 0: # if the hp is zero
            return
        else:
            self.hp += self.heal_power
            print(self.ch_class,"health increased",self.heal_power) 
            print("after")
            print(wizard)
            print(knight)
            print(archer) 
            print("______________________________________________________________________________")



archer = Character("archer",18,75,12,18)
wizard = Character("wizard",17,50,18,16)        #how the characters are
knight = Character("knight",20,100,8,20)
print("at first")
print(wizard)
print(knight)
print(archer)
print("__________________________________________________________________________________________")


choice = ""
while  choice != "3":  # choosing what to do
    print("CHOOSE")          #choosing the option
    print("1.attack      2.heal       3.exit")
    choice = input(": ") 
    if choice == "1":
        attacker = ""      #choosing the character
       
        while attacker != "1" and attacker != "2" and attacker != "3": #choosing who you want to be
            print("1.|wizard |    2.|knight|      3.|archer|")
            attacker = input("who do you want to attack with? ")
           
            if attacker == "1": #if you pick wizard
                attacked = ""
                while attacked != "1" and attacked != "2": #choosing who you wanna attack to
                    print("who do you wanna attack to ? ")
                    print("1.|knight|      2.|archer|")
                    attacked = input(": ")
                    if attacked == "1": #if u attack knight
                        wizard.attack(knight)
                    elif attacked == "2": #if u attack archer
                        wizard.attack(archer)
            if attacker == "2": #if u pick knight to attack with
                attacked=""
                while attacked != "1" and attacked != "2":
                    print("who do you wanna attack? ")
                    print("1.|wizard|      2.|archer|")
                    attacked = input(": ")
                    if attacked == "1": #if u attack wizard
                        knight.attack(wizard)
                    elif attacked == "2": #if u attack archer
                        knight.attack(archer)
            if attacker == "3": #if u pick archer to attack with
                attacked=""
                while attacked != "1" and attacked != "2":
                    print("who do you wanna attack? ")
                    print("1.|wizard|      2.|knight|")
                    attacked = input(": ")
                    if attacked == "1": #if u attavk wizard
                        archer.attack(wizard)
                    elif attacked == "2": # if u attack knight
                        archer.attack(knight)            

    if choice == "2": #if u wanna heal
        choose = ""
        while choose != "1" and choose != "2" and choose != "3": #creating the loop here
            print("who do you want to heal? ")
            print("1.|wizard |    2.|knight|      3.|archer|")
            choose = input(": ")
            if choose == "1": #if u pick wizard
                wizard.heal()
            elif choose == "2": #if u pick knight
                knight.heal()
            elif choose == "3": # if u picl archer
                archer.heal()    
    if choice == "3":  #if you choose to exit the game
        print("come back again")
        break
    
    
            




            

