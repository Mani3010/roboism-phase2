def operations(a,symb,b):
        if(symb=="+"):
            print(a+b)
        elif(symb=="-"):
            print(a-b)
        elif(symb=="*"):
            print(a*b)
        elif(symb=="/"):
            print(a/b)
        else:
            print('please enter a valid symbol')

operations(3,"*",9)