ipin = str(input("entra una ip vàlida/n"))
#maskin = input("entra una màscara vàlida/n")
hola = 0
i = 0
control = 0
ip1 = ipin.find(".")
ip1ok=ipin[:(ip1)]
print(ip1ok)
ip2 =(ipin[(ip1+1):].find("."))

ip2ok = ipin[(ip1+1):ip1+1+ip2]
print(ip2ok)

ip3 = ipin[(ip1+1+ip2+1):].find(".")
ip3ok= ipin[(ip1+1+ip2+1):ip1+1+ip2+1+ip3]
print(ip3ok)

ip4ok = ipin[(ip1+1+ip2+1+ip3+1):len(ipin)]
print(ip4ok)




