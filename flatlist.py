nestedlist = [ [1, 2, 3, 4], ["Ten", ["Twenty",["tywentyone","twentytwo","twentythree"]], "Thirty"], [1.1,  1.0E1, 1+2j, 20.55, 3.142]]
# flatlist=[element for sublist in nestedlist for element in sublist]
# print(flatlist)
original_list = [[1,2], [3], [4,5,[6,[7,8,[9,10]]]]]                                                                                                                         
# def flatten(potential_list): 
#    new_list = [] 
#    for e in potential_list:
#        if isinstance(e, list):
#            new_list.extend(flatten(e))
#        else:
#            new_list.append(e)
#    return new_list
# print(flatten(original_list))

flat_list=sum(original_list,[])
print(flat_list)