mobiles=['iphone','samsung','oppo','vivo','nothing']
for i in range(0,len(mobiles)):
    if i%2==0:
        rev=mobiles[i]#to store the variable
        print(rev[::-1])
#for reversing element which are even
    else:
        print(mobiles[i])
