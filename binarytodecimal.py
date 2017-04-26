# To choose a converter you need to write the function decimal(num) or binary(num)


# DECIMAL SIDE
def decimal(decimalin):
    a = True #This mades work the while
    rest ="" #needed to work
    while not a == False:
        rest = str(int(decimalin % 2)) + rest #here I grab the rest of the division
        decimalin= decimalin / 2  #here we made the division
        if decimalin < 1:
            a = False #stops the while
    print("This is your decimal to binary result " + rest ) #result output

# BINARY SIDE

def binary():
    binaryin = input("Input a binary number:\n")
    i = len(binaryin) -1
    binarynum = 0
    binarydecimal = 0
    binaryintra = ""
    #
    # The next While turns arround the input
    # Example: if you introduce a 1010 to make easy to use the string and numbers
    # I rotate it to 0101 trying to learn how to make it less botched XDDD
    #
    while i>= 0:
        binaryintra = binaryintra + binaryin[i]
        i = i -1
    #
    # Here I made the binary to decimal, as you can see i use the normal used formula
    # (1, 0) * 2^X 
    # X is for the possision of the binary number
    while not binarynum == len(binaryin):
        
        #print(binarynum)        #test
        binarydecimal1=int(binaryintra[binarynum])*2**binarynum
        #print(binarydecimal1) #test
        binarydecimal=binarydecimal+binarydecimal1
        binarynum = binarynum +1
    print("This is your binary to decimal result " + str(binarydecimal))
