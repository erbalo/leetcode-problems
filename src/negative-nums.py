"""
Implement a function that given an array of integers returns another array with the positive values present in the given array which has its negative equivalent.

Example:
Input: [-1, -2, -3] => Output: []
Input: [-3, 2, -1, -4, 3, -2, 1, 5] => Output: [1, 2, 3]
Input: [-2, -2, 1,-1] => []
"""
array = [-2, -2]
array = [-1, -2, -3] 
array = [-3, 2, -1, -4, 3, -2, 1, 5]

def v3(array):
    map = {}

    for i in range(len(array)):
        current = array[i]    
        map[current] = True # no era put :(

    set_list = set()

    for i in range(len(array)):
        to_find = array[i] * -1
        
        if to_find in map:
            set_list.add(abs(to_find))

    print(list(set_list)) # convertir el set a array


def v1(array):
    set_list = set()

    for i in range(len(array)):
        to_find = array[i] * -1
        
        if findV1(array, to_find):
            set_list.add(abs(to_find))

    print(list(set_list)) # convertir el set a array



def findV1(array, elem: int) -> bool:
    founded = False
    for i in range(len(array)):
        if elem == array[i]:
            founded = True
            break;
            
    return founded

v1(array)
v2(array)