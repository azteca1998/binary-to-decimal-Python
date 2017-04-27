ipin = str(input("entra una ip vàlida/n"))
macin = input("entra una màscara vàlida/n")

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


mac1 = macin.find(".")
mac1ok=macin[:(mac1)]
print(mac1ok)
mac2 =(macin[(mac1+1):].find("."))

mac2ok = macin[(mac1+1):mac1+1+mac2]
print(mac2ok)

mac3 = macin[(mac1+1+mac2+1):].find(".")
mac3ok= macin[(mac1+1+mac2+1):mac1+1+mac2+1+mac3]
print(mac3ok)

mac4ok = macin[(mac1+1+mac2+1+mac3+1):len(macin)]
print(mac4ok)




