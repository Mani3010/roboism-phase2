test_list = [9, 4, 5, 4, 4, 5, 9, 5, 4]
print ("Original list : " + str(test_list))
max = 0
res = test_list[0]
for i in test_list:
    freq = test_list.count(i)
    if freq > max:
        max = freq
        res = i
      
print ("Most frequent number is : " + str(res))