menu=[['Paneer' , ['Paneer Do Pyaza',
            "Paneer Passanda","Paneer Lababdar",
                ]
          ],
      ["Dessert",["Gulab Jaamun",
                 "Rabdi","Kheer"
                 ]
          ],
      ["Shakes",["Cold Coffee",
                "Chocolate Shake","Lassi"
                ]
          ],
      ]
resources={"Paneer" : 750, "Oil":10, "Onion":10, "Tomatoes":10, "Milk":15, "Chocolate":500, "Ice Cream":25, "Curd":25}


def item1():
 f=0
 print("Enter paneer,onion and tomatoes you require")
 paneer=int(input())
 onion=int(input())
 tomatoes=int(input())
 if(resources["Paneer"]>= paneer):
     pass
 else:
     f=-1
     print("Paneer is less than required")

 if(resources["Tomatoes"]>= tomatoes):
     pass
 else:
     f=-1
     print("Tomatoes are less than required")
 if(resources["Onion"]>=onion):
     pass
 else:
     f=-1
     print("Onion is less than required")
 if(f==-1):
     print("Sorry you can't make this dish")
 else:
     resources["Paneer"]-=paneer
     resources["Tomatoes"]-=tomatoes
     resources["Onion"]-=onion
     print("Go ahead start the dish")
def item2():
    f = 0
    print("Enter paneer,onion and tomatoes you require")
    paneer = int(input())
    onion = int(input())
    tomatoes = int(input())
    if (resources["Paneer"] >= paneer):
        resources["Paneer"] -= paneer
    else:
        f = -1
        print("Paneer is less than required")

    if (resources["Tomatoes"] >= tomatoes):
        resources["Tomatoes"] -= tomatoes
    else:
        f = -1
        print("Tomatoes are less than required")
    if (resources["Onion"] >= onion):
        resources["Onion"] -= onion
    else:
        f = -1
        print("Onion is less than required")
    if (f == -1):
        print("Sorry you can't make this dish")
    else:
        print("Go ahead start the dish")
def item3():
    f = 0
    print("Enter paneer,onion and tomatoes you require")
    paneer = int(input())
    onion = int(input())
    tomatoes = int(input())
    if (resources["Paneer"] >= paneer):
        pass
    else:
        f = -1
        print("Paneer is less than required")

    if (resources["Tomatoes"] >= tomatoes):
        pass
    else:
        f = -1
        print("Tomatoes are less than required")
    if (resources["Onion"] >= onion):
        pass
    else:
        f = -1
        print("Onion is less than required")
    if (f == -1):
        print("Sorry you can't make this dish")
    else:
        resources["Paneer"] -= paneer
        resources["Tomatoes"] -= tomatoes
        resources["Onion"] -= onion
        print("Go ahead start the dish")
def item2_1():
    milk=int(input("Enter the quantity of milk you will be requiring in the whole process"))
    if(resources["Milk"]>=milk):
        resources["Milk"]-=milk
        print("Start making the dish")
    else:
        print("Sorry main item missing")
def item2_2():
    milk=int(input("Enter the quantity of milk you will be requiring in the whole process"))
    if(resources["Milk"]>=milk):
        resources["Milk"]-=milk
        print("Start making the dish")
    else:
        print("Sorry main item missing")

def item2_3():
    milk = int(input("Enter the quantity of milk you will be requiring in the whole process"))
    if(resources["Milk"]>=milk):
        resources["Milk"]-=milk
        print("Start making the dish")
    else:
        print("Sorry main item missing")
def item3_1():
    f=0
    milk = int(input("Enter the quantity of milk you will be requiring in the whole process"))
    ic = int(input("Enter the quantity of ice cream you will be requiring in the whole process"))
    if (resources["Milk"] >= milk):
        resources["Milk"] -= milk
    else:
        f = -1
        print("Milk is less")

    if (resources["Ice Cream"] >= ic):
        resources["Ice Cream"] -= ic
    else:
        f = -1
        print("Ice Cream is less")
    if(f==-1):
        print("Sorry you can not make this")
    else:
        print("Go ahead and make it")
def item3_3():
    f=0
    curd = int(input("Enter the quantity of curd you will be requiring in the whole process"))
    if(resources["Curd"]>=curd):
        resources["Curd"]-=curd
        print("Start making the dish")
    else:
        print("Sorry main item missing")

def item3_2():
    f=0
    milk = int(input("Enter the quantity of milk you will be requiring in the whole process"))
    ic = int(input("Enter the quantity of ice cream you will be requiring in the whole process"))
    choco = int(input("Enter the quantity of chocolate you will be requiring in the whole process"))
    if (resources["Milk"] >= milk):
        resources["Milk"] -= milk
    else:
        f = -1
        print("Milk is less")

    if (resources["Ice Cream"] >= ic):
        resources["Ice Cream"] -= ic
    else:
        f = -1
        print("Ice Cream is less")
    if (resources["Chocolate"] >= ic):
        resources["Chocolate"] -= choco
    else:
        f = -1
        print("Chocolate is less")
    if (f == -1):
        print("Sorry you can not make this")
    else:
        print("Go ahead and make it")

if __name__ == '__main__':
    print("Following is the food menu available:\n")
    for i in menu:
        for m in i:
            print(m,end=" ")
    print("Following are the raw resources:")
    for k in resources:
        print(k,":",resources[k])
    choice=1
    while(choice==1):
        dish=input("Enter the dish you want to make?")
        if(dish==menu[0][1][0]):
            item1()
        elif(dish==menu[0][1][1]):
            item2()
        elif(dish==menu[0][1][2]):
            item3()
        elif(dish==menu[1][1][0]):
            item2_1()
        elif(dish==menu[1][1][1]):
            item2_2()
        elif(dish==menu[1][1][2]):
            item2_3()
        elif(dish==menu[2][1][0]):
            item3_1()
        elif(dish==menu[2][1][1]):
            item3_2()
        elif(dish==menu[2][1][2]):
            item3_3()
        else:
            print("Invalid Choice")
        choice=int(input("More dish(1/0)"))



