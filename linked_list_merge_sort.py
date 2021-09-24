from linked_list import LinkedList

def merge_sort(linked_list):
    """Sorts a linked list in ascending order
    recursively divide the linked list into sublists containing a single node
    repeatedly merge the sublists to produce sorted sublists until one remains
    
    Returnsa sorted linked list

    Args:
        linked_list ([type]): [description]
    """
    if linked_list.size()==1 :
        return linked_list
    elif linked_list is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return(left,right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists

    Args:
        linked_list ([type]): [description]
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        
        return left_half, right_half
    else:
        