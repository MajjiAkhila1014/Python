menu={
    'chicken_biryani':555,
    'butter_chicken':450,
    'tandoori_chicken':555,
    'juicy_mandi':700
}
menu['fruit_salad']=786#inserting item in dictionary
menu.pop('chicken_biryani')
print(menu)
print(menu.keys())#keys is for printing only key values
print(menu.values())
for k,v in menu.items():#in dict each item contains key and value 
    print(k,'-->',v)