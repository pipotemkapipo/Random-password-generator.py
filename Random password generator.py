import random
def abc():
    alf = 'qwertyuiopasdfghjkllzxcvbnmQWERTYUIOPASDFGHJKLLZXCVBNM0123456789@$_'

    pas = ''
    for i in range(10):
        sim = random.choice(alf)
        pas += sim
    return pas 
a = True
while a:
    a = abc()
    print(a)
    b = input("Create another password?\nY/If not, press Enter\n")
    if b == 'Y':
        print(a)
    else:
        a = False    
