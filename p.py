import math
def knapsack(capacity, items):
    # Be greedy!
    lists = []
    items_copy=list(items[:])
    actual_capacity=capacity
    while items_copy:
        big_item_size = -1
        big_item_index = -1
        big_item_value = -1
        index = 0
        for item in items_copy:
            if(item[1] > big_item_value):
                big_item_value = item[1]
                big_item_size = item[0]
                big_item_index = index
            index+=1
                
        if big_item_size <= actual_capacity:
            quantity = math.floor(actual_capacity/big_item_size)
            lists.append(quantity)
            actual_capacity = actual_capacity-quantity*big_item_size
        else:
            lists.append(0)
        items_copy.pop(big_item_index)
    return lists


