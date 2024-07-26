def check(s):
    rev=''
    for i in s:
        rev=i+rev
        print(type(rev))
    return rev
s='SRIDEVI WOMENS ENGINEERING COLLEGE'
print(check(s))