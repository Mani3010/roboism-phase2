s=input("enter any string")
sumd=0
digit=""
for i in range(0,len(s)):
    if(s[i].isdigit()):
        digit=digit+s[i]
        sumd=sumd+int(s[i])
        if sumd==0:
            print("no number in string")
        else:
                print("orginal string =",s)
                print("sum of digit=",sumd)
                print("digit found in string",digit)
