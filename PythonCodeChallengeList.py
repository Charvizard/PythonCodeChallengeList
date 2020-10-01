lst = [1,1,2]
def append_sum(lst) : 
    for x in range(len(lst)) :  
        lst.append(lst[-1] + lst[-2])
    return lst

print(append_sum(lst))
