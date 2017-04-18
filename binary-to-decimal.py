print("ONLY NUMBERS!")
resultat=""

decimalbinary = ""
mode = input("'d' Decimal o 'b' Binary\n")
binarydecimal1 = 0
# DECIMAL SIDE
decimalin1 =""

def decimal():
    resta=""
    decimalin = int(input("Input a decimal number\n"))
    decimalin1 = decimalin
    a = True
    while not a == False:
        resta =str(int(decimalin1 % 2)) + resta
        decimalin1= decimalin1 / 2
        
        # print(resta)       #testing
        # print(decimalin1)   #testing
        # print("separador")   #testing
        if decimalin1 < 1:
            a = False
    print("This is your decimal to binary result " + resta )
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



if mode == ("d"):
    decimal()
elif mode == ("b"):
    binary()

