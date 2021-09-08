def recursive_binary_search(list, target):
    """[summary]
    This is a recursive solution
    
    This involves a set of stopping conditions and a function that calls itself
    
    The amount of times the function calls itself is called recursion depth
    Python has recursion depth limitations
    
    Args:
        list ([type]): [description]
        target ([type]): [description]

    Returns:
        [type]: [description]
    """
    if len(list) == 0:    # this is stopping condition or base case
        return False
    else:
        midpoint = (len(list))//2
        
        if list[midpoint] == target: # this is stopping condition or base case
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

def verify(result):
    print("Target found: ", result)

numbers = [1,2,3,4,5,6,7,8]
result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 7)
verify(result)