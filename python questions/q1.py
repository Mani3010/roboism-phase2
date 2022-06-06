# question 1 ...
# input 2 parameters and one is a string and other a list. 
# if the string says asc desc none arrange the list in ascending descening or none order recpectively and output the list


def listsorter():
    
    n=int(input("enter the number of elements in the list\n"))

    print("Enter the list of numbers")

    list=[]
    for i in range (0,n):
        x=input(f"enter the {i+1}th number in the list")
        list.append(x)

    string=str(input("enter the string asc to get ascending order of the list of numbers desc to get the\ndescending order of the numbers and none to get the original default list "))

    if(string=="asc"):
        list.sort()
        print(list)

    elif(string=="desc"):
        list.sort(reverse=True)
        print(list)

    elif(string=="none"):
        print(list)

    
listsorter()




