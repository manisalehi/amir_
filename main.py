value = input("number")

algin = input("algin")


if algin == "left" :
    if int(value.replace(" ","")) == 0:
        print(">"+value)
    elif int(value.replace(" ","")) > 0:
        print(">"+ "+" +value)
    else:
        print(">"+ "-"+value)
elif algin == "right":
    if int(value.replace(" ","")) == 0:
        print( "                                    "+""+value+"<")
    elif int(value.replace(" ","")) > 0:
        print( "                                    "+"+"+value+"<")
    else:
        print( "                                    "+""+value+"<")
     
     
 # manisalehi 
