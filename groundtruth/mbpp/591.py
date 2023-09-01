"""
Write a python function to interchange the first and last elements in a list.
"""

def swap_List(newList): 
    assert isinstance(newList, list), "invalid inputs" # $_CONTRACT_$
    assert len(newList) > 0, "invalid inputs" # $_CONTRACT_$
    return newList[-1:] + newList[1:-1] + newList[:1]



assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
assert swap_List([1, 2, 3]) == [3, 2, 1]
assert swap_List([4, 5, 6]) == [6, 5, 4]
