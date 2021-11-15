import math

array = [170, 45, 75, 90, 802, 24, 2, 66]

for index in range ( 0, len(array)-1 ) :
    min_element = math.inf
    min_element_index = -1
    
    for find_min_index in range ( index , len(array) ) :
        
        if array [ find_min_index ] < min_element : 
            min_element = array [ find_min_index ]
            min_element_index = find_min_index
            
    array [ min_element_index ] = array [ index ]
    array [ index ] = min_element
    
print (array)