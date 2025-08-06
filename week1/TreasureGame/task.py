print(r'''
                   __..-----")
        ,.--._ .-"_..--...-"
       -""". _/_ /  ..--""""-.
       _.--""...:._:(_ ..:"::. \
    .-" ..::--""_(##)#)"":. \ \)    \ _|_ /
   /_:-:"/  :__(##)##)    ): )   "-./"   "\.-"
   "  / |  :" :/""\///)  /:."    --(       )--
     / :( :( :(   (#//)  "       .-"\.___./"-.
    / :/|\ :\_:\   \#//\            /  |  \
    |:/ | ""--":\   (#//)              "
    \/  \ :|  \ :\  (#//)
         \:\   ".":. \#//\
          ":|    "--'(#///)
                     (#///)
                     (#///)         ___/""\     
                      \#///\           oo##
                      (##///)         `-6 #
                      (##///)          ,"`.
                      (##///)         // `.\ 
                      (##///)        ||o   \\
                       \##///\        \-+--//
                       (###///)       :_|_(/
                       (sjw////)__...--:: :...__
                       (#/::"""        :: :     ""--.._
                  __..-"""           __;: :            "-._
          __..--""                  `---/ ;                "._
 ___..--""                             `-"                    "-..___
   (_ ""---....___                                     __...--"" _)
     """--...  ___"""""-----......._______......----"""     --"""
                   """"       ---.....   ___....----

''')
print("Welcome to Treasure Island!")
print("Your mission is to find the buried treasure")
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right"').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for the next boat, or type "swim" to swim across to the other island.').lower()
    if choice2 == "wait":
        choice3 = input("You arrived safely to the island and stumble upon a two houses, one red, and the other blue. Which one do you choose to enter?").lower()
        if choice3 == "red":
            print("Its a room full of fire. Game Over")
        elif choice3 == "blue":
            print("You found the secret treasure. You Win!!")
        elif choice3 == "yellow":
            print("You enter a room full of spikes and die. Game Over")
        else:
            print("You chose to turn back and go home, but got eaten by a wild butterfly. Game Over")
    else:
        print("You got eaten by a pack of wild turtles.")
else:
    print("You fell in to a hole. Game Over")