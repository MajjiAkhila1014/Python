'''
try:
    a=10
    b=0
    c=a/b
    print(c)
except Exception:
    print('divide by zero is not possible')
'''
'''
try:
    a=5
    print(b)
except NameError:
    print("variable b is not assigned")

'''
try:
    arr=[1,7,8,12,36]
    print(arr[4])
except IndexError:
    print("cannot access index value")
else:
    print("no exception occur")
finally:
    print("finally wednesday is a last day of training..")
        
